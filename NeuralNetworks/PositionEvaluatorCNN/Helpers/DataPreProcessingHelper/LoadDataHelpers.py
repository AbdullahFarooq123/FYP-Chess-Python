import tensorflow as tf
import numpy as np

def create_memmap_dataset(board_features_filename, game_features_filename, labels_filename, batch_size=32):
    board_features = np.load(board_features_filename, mmap_mode='r')
    game_features = np.load(game_features_filename, mmap_mode='r')
    labels = np.load(labels_filename, mmap_mode='r')

    board_features_dataset = tf.data.Dataset.from_tensor_slices(board_features)
    game_features_dataset = tf.data.Dataset.from_tensor_slices(game_features)
    labels_dataset = tf.data.Dataset.from_tensor_slices(labels)

    del board_features
    del game_features
    del labels

    combined_dataset = tf.data.Dataset.zip((board_features_dataset, game_features_dataset, labels_dataset))

    del board_features_dataset
    del game_features_dataset
    del labels_dataset
    
    combined_dataset = combined_dataset.batch(batch_size)
    
    return combined_dataset