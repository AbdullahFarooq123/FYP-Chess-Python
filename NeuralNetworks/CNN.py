from tensorflow import keras

# Define the CNN model architecture
model = keras.Sequential()
model.add(keras.layers.Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(8, 8, 12)))  # Assuming 8x8 chessboard and 12 input channels (bitboards)
model.add(keras.layers.Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(128, activation='relu'))

# Output layer for move prediction
num_moves = 64 * 6
model.add(keras.layers.Dense(num_moves, activation='softmax'))

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Print the model summary
model.summary()