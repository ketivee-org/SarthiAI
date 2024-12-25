# Improved File Structure for SarthiAI

## Root Directory (SarthiAI/)

```plaintext
SarthiAI/
│
├── ai_models/               # Contains all AI model implementations
├── frontend/                # Web interface code
├── backend_server/          # Backend server logic
├── training/                # Training files and datasets
├── output_files/            # Storage for AI-generated outputs
├── logs/                    # Logs for debugging and monitoring
├── scripts/                 # Utility scripts for deployment, monitoring, etc.
├── configs/                 # Centralized configuration files
└── README.md                # Project overview and documentation
```

---

## 1. AI Models Directory (ai\_models/)

Organized into subfolders for each AI model with separate folders for preprocessing, model architecture, and utilities.

```plaintext
SarthiAI/ai_models/
│
├── sarthi/                 # Sarthi AI model for orchestration
│   ├── src/                # Source code for model architecture
│   │   ├── model.py        # Main Sarthi model script
│   │   ├── interaction.py  # User interaction logic
│   │   └── utils.py        # Helper functions
│   ├── configs/            # Configuration files
│   │   └── config.yaml     # Configurations for Sarthi AI
│   ├── data/               # Data preprocessing logic
│   │   └── preprocess.py   # Data preprocessing script
│   └── checkpoints/        # Pre-trained weights and checkpoints
│
├── yug/                    # Yug AI for 3D item generation
│   ├── src/
│   │   ├── model.py
│   │   ├── generator.py    # 3D item generator
│   │   └── utils.py
│   ├── configs/
│   │   └── config.yaml
│   └── checkpoints/
│
├── aadi/                   # Aadi AI for texture generation
│   ├── src/
│   │   ├── model.py
│   │   ├── texture_mapper.py # Texture mapping logic
│   │   └── utils.py
│   ├── configs/
│   │   └── config.yaml
│   └── checkpoints/
│
├── arth/                   # Arth AI for video and multimedia
│   ├── src/
│   │   ├── model.py
│   │   ├── video_editor.py  # Multimedia editing logic
│   │   └── utils.py
│   ├── configs/
│   │   └── config.yaml
│   └── checkpoints/
│
├── ved/                    # Ved AI for emotion and facial recognition
│   ├── src/
│   │   ├── model.py
│   │   ├── face_recognition.py
│   │   ├── emotion_detection.py
│   │   └── utils.py
│   ├── configs/
│   │   └── config.yaml
│   └── checkpoints/
│
└── parth/                  # Parth AI for system interaction and automation
    ├── src/
    │   ├── model.py
    │   ├── automation.py    # System automation scripts
    │   ├── cursor_control.py
    │   └── utils.py
    ├── configs/
    │   └── config.yaml
    └── checkpoints/
```

---

## 2. Frontend Directory (frontend/)

Organized for a modular React or Next.js application with reusable components.

```plaintext
SarthiAI/frontend/
│
├── public/                  # Public assets
│   ├── css/                 # Global styles
│   ├── images/              # Static images
│   └── js/                  # Front-end scripts
├── src/                     # Source code for the frontend
│   ├── pages/               # Next.js pages
│   │   ├── index.js         # Main page
│   │   ├── training.js      # File upload page
│   │   ├── output.js        # Display AI-generated outputs
│   │   └── login.js         # Login/authentication
│   ├── components/          # Reusable React components
│   │   ├── Header.js
│   │   ├── Footer.js
│   │   ├── AIInteraction.js
│   │   └── UploadForm.js
│   ├── styles/              # Component-specific styles
│   └── utils/               # Frontend utility functions
├── package.json             # Dependencies
└── next.config.js           # Next.js configuration
```

---

## 3. Backend Server Directory (backend\_server/)

Contains REST API logic, services, and database models.

```plaintext
SarthiAI/backend_server/
│
├── src/                     # Source code for the backend
│   ├── main.py              # Entry point (Flask/FastAPI/Django)
│   ├── api/                 # API endpoints
│   │   ├── sarthi_api.py
│   │   ├── file_upload.py
│   │   ├── output_api.py
│   │   └── auth.py
│   ├── services/            # Backend services for AI models
│   │   ├── ai_manager.py    # Orchestrates AI model interactions
│   │   ├── audio_service.py
│   │   └── emotion_service.py
│   ├── database/            # Database models and migrations
│   │   ├── models.py
│   │   ├── migrations/
│   │   └── db.sqlite
│   └── utils/               # Helper functions for backend
├── configs/                 # Configuration files
│   └── config.yaml
├── requirements.txt         # Backend dependencies
└── Dockerfile               # Docker container configuration
```

---

## 4. Training Directory (training/)

Organized for efficient dataset management and training pipelines.

```plaintext
SarthiAI/training/
│
├── datasets/                # Raw and preprocessed datasets
│   ├── code_dataset/
│   ├── image_dataset/
│   ├── video_dataset/
│   ├── music_dataset/
│   └── emotion_dataset/
├── scripts/                 # Training scripts
│   ├── train_sarthi.py
│   ├── train_yug.py
│   ├── train_aadi.py
│   ├── train_arth.py
│   ├── train_ved.py
│   └── preprocess.py        # Data preprocessing script
├── configs/                 # Training configurations
│   └── training_config.yaml
└── logs/                    # Training logs
    ├── training_log_sarthi.txt
    ├── training_log_yug.txt
    └── training_log_ved.txt
```

---

## 5. Output Files Directory (output\_files/)

Stores all generated outputs categorized by type.

```plaintext
SarthiAI/output_files/
│
├── websites/                # Generated websites
├── programs/                # Generated programs
│   ├── linux/
│   ├── mac/
│   ├── sarthi_os/
│   └── windows/
├── media/                   # Generated multimedia content
│   ├── images/
│   ├── videos/
│   └── 3d_objects/
├── music/                   # Generated music tracks
│   ├── track_1.mp3
│   └── track_2.wav
└── logs/                    # Logs for generated outputs
    └── output_logs.txt
```

---

## 6. Logs Directory (logs/)

Centralized logging for all project activities.

```plaintext
SarthiAI/logs/
│
├── server_logs/             # Backend server logs
│   └── server_log.txt
├── user_activity_logs/      # Logs of user interactions
│   └── user_activity_log.txt
└── error_logs/              # Error tracking logs
    └── error_log.txt
```

---

## 7. Scripts Directory (scripts/)

Utility scripts for deployment, monitoring, and automation.

```plaintext
SarthiAI/scripts/
│
├── deploy.sh                # Deployment automation script
├── monitor.py               # Monitoring script for server and AI models
├── backup.sh                # Backup script for database and outputs
└── cleanup.py               # Cleanup script for temporary files
```

---
