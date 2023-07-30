import os

from tensorflow.python.keras.callbacks import Callback


class CustomModelCheckpoint(Callback):
    def __init__(self, checkpoint_path, model_name, monitor='val_accuracy', save_best_only=True,
                 save_weights_only=False, mode='auto', save_freq=1000, verbose=1):
        super(CustomModelCheckpoint, self).__init__()
        self.checkpoint_path = checkpoint_path
        self.model_name = model_name
        self.monitor = monitor
        self.save_best_only = save_best_only
        self.save_weights_only = save_weights_only
        self.mode = mode
        self.save_freq = save_freq
        self.verbose = verbose
        self.epoch_count = 0

    def on_epoch_end(self, epoch, logs=None):
        self.epoch_count += 1
        if self.epoch_count % self.save_freq == 0:
            # Extract the desired log value (e.g., training loss or validation accuracy)
            log_value_str = ''
            if logs is not None:
                for field_name, field_value in logs.items():
                    round_to: int = 1 if 'lr' != field_name else 4
                    log_field = str(field_name).split("_")[-1]
                    log_value = round(float(field_value), round_to)
                    log_value_str += f'{log_field}-{log_value}_'
                log_value_str = log_value_str[:-1]
            filename = os.path.join(self.checkpoint_path,
                                    f"{self.model_name}_(ep-{self.epoch_count}_{log_value_str}).keras")
            self.model.save(filename)
