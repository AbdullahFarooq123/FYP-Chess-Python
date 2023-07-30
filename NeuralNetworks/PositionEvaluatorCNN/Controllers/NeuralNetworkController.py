import datetime
import os
import sys

import pandas as pd
import tensorflow as tf
from keras import Model

from NeuralNetworks.PositionEvaluatorCNN import Config
from NeuralNetworks.PositionEvaluatorCNN.Controllers.LoadDataController import load_data
from NeuralNetworks.PositionEvaluatorCNN.Helpers.CustomCallback import CustomModelCheckpoint
from NeuralNetworks.PositionEvaluatorCNN.Helpers.NeuralNetworkConfigHelper import configure_neural_network


class PositionEvalNN:
    def __init__(self,
                 start_learning_rate: float,
                 min_learning_rate: float,
                 max_learning_rate: float,
                 ramp_up_epochs: int,
                 sustain_epochs: int,
                 exp_decay: float,
                 epochs: int,
                 save_interval: int,
                 training_data_limit: int):
        self.start_learning_rate = start_learning_rate
        self.min_learning_rate = min_learning_rate
        self.max_learning_rate = max_learning_rate
        self.ramp_up_epochs = ramp_up_epochs
        self.sustain_epochs = sustain_epochs
        self.exp_decay = exp_decay
        self.inputs, self.labels = load_data(limit=training_data_limit)
        self.parent_dir = f'{os.getcwd()}'
        self.epochs = epochs
        self.save_interval = save_interval
        if 'google.colab' in sys.modules:
            if not os.path.exists(Config.drive_path):
                from google.colab import drive
                drive.mount(Config.drive_path)
            self.parent_dir = f'{Config.drive_path}/MyDrive/NN_Models/'

    def train_position_evaluator(self, model_path: str = '', call_backs=[]):

        nn_model, no_of_tpu_workers = self.__initialize_model(model_path)
        nn_model.summary()

        batch_size = Config.mini_batch_size * no_of_tpu_workers
        training_steps = self.inputs[0].__len__() // batch_size

        history = nn_model.fit(x=self.inputs, y=self.labels, epochs=self.epochs,

                               shuffle=True,
                               batch_size=batch_size,
                               callbacks=call_backs)
        training_history = pd.DataFrame(history.history)
        training_history.to_csv(f'{self.parent_dir}Model (e-{self.epochs}_td_len-{len(self.labels)}).csv')
        nn_model.save(f'{self.parent_dir}Position Evaluator{datetime.datetime.now()}.keras')

    def __initialize_model(self, model_path: str) -> [Model, int]:
        no_of_tpu_workers: int = 1
        try:
            tpu = tf.distribute.cluster_resolver.TPUClusterResolver()  # TPU detection
            tf.config.experimental_connect_to_cluster(tpu)
            tf.tpu.experimental.initialize_tpu_system(tpu)
            tpu_strategy = tf.distribute.TPUStrategy(tpu)
            with tpu_strategy.scope():
                nn_model: Model = configure_neural_network(model_path)
            no_of_tpu_workers = tpu_strategy.num_replicas_in_sync
        except ValueError:
            nn_model: Model = configure_neural_network(model_path)
        return nn_model, no_of_tpu_workers

    def learning_frequency_rate_callback(self, epoch: float):
        if epoch < self.ramp_up_epochs:
            return (
                    self.max_learning_rate - self.start_learning_rate) / self.ramp_up_epochs * epoch + self.start_learning_rate
        elif epoch < self.ramp_up_epochs + self.sustain_epochs:
            return self.max_learning_rate
        else:
            return (self.max_learning_rate - self.min_learning_rate) * self.exp_decay ** (
                    epoch - self.ramp_up_epochs - self.sustain_epochs) + self.min_learning_rate

    def get_checkpoint_callback(self):
        return CustomModelCheckpoint(
            f'{self.parent_dir}',
            monitor='val_accuracy',
            save_best_only=True,
            save_weights_only=False,
            mode='auto',
            save_freq=self.save_interval,
            verbose=1,
            model_name='Model'
        )

    def get_learning_rate_callback(self):
        return tf.keras.callbacks.LearningRateScheduler(
            lambda epoch: self.learning_frequency_rate_callback(epoch),
            verbose=True)
