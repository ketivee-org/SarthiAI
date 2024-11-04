# train_sarthi.py

import tensorflow as tf

def train_sarthi_model(dataset):
    """Trains the Sarthi model with the provided dataset"""
    # Create the model architecture (simplified for example)
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(128, activation='relu', input_shape=(dataset.shape[1],)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    
    # Train the model
    history = model.fit(dataset['data'], dataset['labels'], epochs=10, validation_split=0.2)
    
    # Save the model
    model.save('ai_models/sarthi/checkpoints/sarthi_model.h5')
    print("Sarthi model trained and saved.")

# Placeholder for dataset loading (you would load actual data here)
dataset = {'data': [[0]*20]*100, 'labels': [0]*100}
train_sarthi_model(dataset)
