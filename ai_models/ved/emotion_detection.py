import os
import numpy as np
import cv2
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split

# Path to the dataset
dataset_path = "C:/Users/swana/Desktop/SarthiAI/datasets/emotion_dataset/fer2013/"

# Define the emotion labels
emotion_labels = ["Angry", "Disgust", "Fear", "Happy", "Neutral", "Sad", "Surprise"]


# Load the FER2013 dataset
def load_data(dataset_path):
    data = []
    labels = []
    for emotion_folder in os.listdir(dataset_path):
        emotion_folder_path = os.path.join(dataset_path, emotion_folder)
        if not os.path.isdir(emotion_folder_path):
            continue
        label = emotion_labels.index(emotion_folder)
        for img_file in os.listdir(emotion_folder_path):
            img_path = os.path.join(emotion_folder_path, img_file)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (48, 48))
            data.append(img)
            labels.append(label)
    return np.array(data), np.array(labels)


# Load the data
X, y = load_data(dataset_path)
X = X.reshape(X.shape[0], 48, 48, 1).astype("float32") / 255.0  # Reshape and normalize
y = np.eye(len(emotion_labels))[y]  # One-hot encode labels

# Split the dataset into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Data augmentation to increase dataset diversity
datagen = ImageDataGenerator(
    rotation_range=10,
    width_shift_range=0.1,
    height_shift_range=0.1,
    shear_range=0.1,
    zoom_range=0.1,
    horizontal_flip=True,
)
datagen.fit(X_train)

# Build the CNN model
model = Sequential()

# Convolution + MaxPooling
model.add(Conv2D(64, (3, 3), activation="relu", input_shape=(48, 48, 1)))
model.add(MaxPooling2D(pool_size=(2, 2)))

# Add more layers
model.add(Conv2D(128, (3, 3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(256, (3, 3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

# Flatten the layers and add Dense layers
model.add(Flatten())
model.add(Dense(128, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(len(emotion_labels), activation="softmax"))

# Compile the model
model.compile(
    optimizer=Adam(learning_rate=0.001),
    loss="categorical_crossentropy",
    metrics=["accuracy"],
)

# Train the model
batch_size = 64
epochs = 50

history = model.fit(
    datagen.flow(X_train, y_train, batch_size=batch_size),
    validation_data=(X_val, y_val),
    steps_per_epoch=len(X_train) // batch_size,
    epochs=epochs,
)

# Save the trained model
model.save("C:/Users/swana/Desktop/SarthiAI/ai_models/ved/emotion_model.h5")

print("Model training complete and saved.")
