import os

# Define the base directory
base_dir = "SarthiAI"

# Define the file structure
file_structure = {
    "ai_models": {
        "sarthi": ["model.py", "sarthi_interaction.py", "requirements.txt", "config.yaml"],
        "yug": ["model.py", "config.yaml"],
        "aadi": ["model.py", "config.yaml"],
        "arth": ["model.py", "config.yaml"],
        "ved": ["model.py", "face_recognition.py", "emotion_detection.py", "config.yaml"],
        "parth": ["model.py", "move_mouse.py", "cursor.py", "README", "config.yaml"],
    },
    "frontend": {
        "web_interface": {
            "pages": ["index.js", "training.js", "output.js", "login.js"],
            "components": ["header.js", "ai_interaction.js", "upload_form.js"],
            "public": {
                "css": [],
                "images": [],
                "js": []
            },
            "next.config.js": None,
            "package.json": None,
        }
    },
    "backend_server": {
        "api": ["sarthi_api.py", "file_upload.py", "output_generation.py", "auth.py"],
        "services": ["ai_manager.py", "audio_recognition.py", "face_emotion_service.py"],
        "database": ["models.py", "db.sqlite"],
        "app.py": None,
        "config.yaml": None,
        "requirements.txt": None,
    },
    "training": {
        "datasets": {
            "code_dataset": [],
            "image_dataset": [],
            "video_dataset": [],
            "music_dataset": [],
            "emotion_dataset": [],
        },
        "scripts": [
            "preprocess.py",
            "train_sarthi.py",
            "train_yug.py",
            "train_aadi.py",
            "train_arth.py",
            "train_ved.py"
        ],
        "logs": [
            "training_log_sarthi.txt",
            "training_log_yug.txt",
            "training_log_ved.txt"
        ],
    },
    "output_files": {
        "websites": [],
        "programs": ["linux/", "mac/", "Sarthi-Os/", "windows/"],
        "images": [],
        "videos": [],
        "3d_objects": [],
        "music": ["track_1.mp3", "track_2.wav"],
        "logs": ["output_generation_logs.txt"],
    },
    "logs": ["server_log.txt", "user_activity_log.txt", "error_log.txt"],
    "README.md": None,
}

# Function to create the structure
def create_structure(base, structure):
    for name, content in structure.items():
        path = os.path.join(base, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        elif isinstance(content, list):
            os.makedirs(path, exist_ok=True)
            for item in content:
                item_path = os.path.join(path, item)
                if "/" in item:  # Handle directories
                    os.makedirs(item_path, exist_ok=True)
                else:
                    open(item_path, 'w').close()  # Create files
        elif content is None:
            open(path, 'w').close()  # Create file
        else:
            raise ValueError("Invalid structure format")

# Create the structure
create_structure(base_dir, file_structure)
print(f"Directory structure for {base_dir} has been created!")
