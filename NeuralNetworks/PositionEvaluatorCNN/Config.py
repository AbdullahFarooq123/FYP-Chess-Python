mini_batch_size: int = 64
board_feature_input_shape: tuple = (64,)
player_feature_input_shape: tuple = (6,)
filter_count: int = 64

training_data_path: str = 'chessData.csv'
drive_path: str = '/content/drive'

start_learning_rate: float = 0.01
min_learning_rate: float = 0.01
max_learning_rate: float = 0.1
ramp_up_epochs: int = 5
sustain_epochs: int = 0
exp_decay: float = 0.8
epochs: int = 1000
save_interval = 500
training_data_limit: int = 1000000

