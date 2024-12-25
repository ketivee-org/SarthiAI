# Importing necessary libraries
import face_recognition
import cv2
import numpy as np
import os
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report

# Paths for dataset and saving model
DATASET_PATH = "faces_dataset/"  # Folder containing images labeled by subfolders
MODEL_PATH = "face_recognition_model.npy"

# Helper function: Load images and labels from the dataset
def load_dataset(dataset_path):
    images = []
    labels = []
    for label in os.listdir(dataset_path):
        label_path = os.path.join(dataset_path, label)
        if os.path.isdir(label_path):
            for image_file in os.listdir(label_path):
                image_path = os.path.join(label_path, image_file)
                image = face_recognition.load_image_file(image_path)
                face_encodings = face_recognition.face_encodings(image)
                if face_encodings:  # Use only images with a detectable face
                    images.append(face_encodings[0])
                    labels.append(label)
    return np.array(images), np.array(labels)

# Load the dataset
print("[INFO] Loading dataset...")
images, labels = load_dataset(DATASET_PATH)
if len(images) == 0:
    print("[ERROR] No face encodings found in the dataset. Check the images.")
    exit()

# Encode labels
print("[INFO] Encoding labels...")
label_encoder = LabelEncoder()
encoded_labels = label_encoder.fit_transform(labels)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(images, encoded_labels, test_size=0.2, random_state=42)

# Train an SVM classifier
print("[INFO] Training the face recognition model...")
classifier = SVC(kernel="linear", probability=True)
classifier.fit(X_train, y_train)

# Evaluate the model
print("[INFO] Evaluating the model...")
y_pred = classifier.predict(X_test)
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))

# Save the model and label encoder
print("[INFO] Saving the model...")
np.save(MODEL_PATH, {"classifier": classifier, "label_encoder": label_encoder})
print("[INFO] Model saved!")

# Real-time face recognition with expression detection
def recognize_faces_in_video():
    print("[INFO] Starting webcam...")
    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        # Convert the frame to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect faces and compute face encodings
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Predict the identity of the face
            matches = classifier.predict_proba([face_encoding])
            best_match = np.argmax(matches)
            label = label_encoder.classes_[best_match]
            confidence = matches[0][best_match]

            # Add a label and confidence score to the video frame
            label_text = f"{label} ({confidence:.2f})"
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, label_text, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        # Display the video frame
        cv2.imshow("Face Recognition", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Start real-time recognition
    recognize_faces_in_video()
