# SarthiAI

Welcome to Sarthi AI project This program also call as Sarthi Devlopment Program

We all part of this program 












































# Project Stucter 

You can also download structure file 

1. Root Directory (SarthiAI/)

SarthiAI/
│
├── ai_models/
├── web_interface/
├── backend_server/
├── training/
├── output_files/
├── logs/
└── README.md

2. AI Models Directory (ai_models/)


SarthiAI/ai_models/
│
├── sarthi/
│   ├── model.py              # Main Sarthi model script
│   ├── sarthi_interaction.py # User interaction logic
│   ├── requirements.txt      # Dependencies for Sarthi
│   ├── config.yaml           # Configurations for Sarthi AI
│   └── checkpoints/          # Pre-trained weights
│
├── yug/                     
│   ├── model.py              # AI for 3D item generation
│   ├── config.yaml
│   └── checkpoints/
│
├── aadi/
│   ├── model.py              # AI for music and sound generation
│   ├── config.yaml
│   └── checkpoints/
│
├── arth/
│   ├── model.py              # AI for video and multimedia
│   ├── config.yaml
│   └── checkpoints/
│
├── ved/                      
│   ├── model.py              # AI for emotion and facial recognition
│   ├── face_recognition.py
│   ├── emotion_detection.py
│   ├── config.yaml
│   └── checkpoints/




3. Web Interface Directory (web_interface/)

SarthiAI/web_interface/
│
├── next.config.js            # Next.js configuration
├── package.json              # Dependencies
├── pages/
│   ├── index.js              # Main page of Sarthi AI interaction
│   ├── training.js           # Upload training files
│   ├── output.js             # Display generated files (websites, apps, media)
│   └── login.js              # User login or authentication
│
├── components/               
│   ├── header.js             # Navigation bar and header
│   ├── ai_interaction.js      # Component for interacting with Sarthi AI
│   └── upload_form.js        # Form for file uploads
│
└── public/
    ├── css/                  # Styling and CSS files
    ├── images/               # Static images used in the interface
    └── js/                   # Front-end scripts



4. Backend Server Directory (backend_server/)

SarthiAI/backend_server/
│
├── app.py                    # Main server script (Flask/FastAPI/Django)
├── config.yaml               # Server configurations (database, API keys)
├── requirements.txt          # Backend dependencies
├── api/
│   ├── sarthi_api.py         # Endpoint for interacting with Sarthi AI
│   ├── file_upload.py        # Endpoint for uploading code or media
│   ├── output_generation.py  # Logic for managing and returning outputs
│   └── auth.py               # User authentication APIs
├── services/
│   ├── ai_manager.py         # Orchestrates communication between multiple AIs
│   ├── audio_recognition.py  # Audio processing service
│   └── face_emotion_service.py # Ved AI for face and emotion recognition
└── database/
    ├── models.py             # Database models for storing user data, outputs
    └── db.sqlite             # SQLite database (or another DB system)




5. Training Files Directory (training/)

SarthiAI/training/
│
├── datasets/
│   ├── code_dataset/         # Source code datasets from GitHub (e.g., Blender)
│   ├── image_dataset/        # Image datasets for image generation AI
│   ├── video_dataset/        # Video datasets for Arth AI
│   ├── music_dataset/        # Audio datasets for Aadi AI
│   └── emotion_dataset/      # Facial and emotion recognition datasets for Ved AI
│
├── scripts/
│   ├── preprocess.py         # Preprocessing scripts for datasets
│   ├── train_sarthi.py       # Training script for Sarthi
│   ├── train_yug.py          # Training script for Yug
│   ├── train_aadi.py         # Training script for Aadi
│   ├── train_arth.py         # Training script for Arth
│   └── train_ved.py          # Training script for Ved
│
└── logs/
    ├── training_log_sarthi.txt
    ├── training_log_yug.txt
    └── training_log_ved.txt


6. Output Files Directory    # This directory handles the storage of outputs for AI model interactions and user data uploads.

SarthiAI/output_files/
│
├── websites/
│   ├── site_1/
│   ├── site_2/
│   └── ...
├── programs/
│   ├── linux/
│   ├── mac/
│   ├── Sarthi-Os/
│   └── windows/
│   
├── m hj
│   ├── images/
│   ├── videos/
│   └── 3d_objects/
├── music/
│   ├── track_1.mp3
│   └── track_2.wav
└── logs/
    └── output_generation_logs.txt




7. Logs Directory     # This directory handles the storage of log files for AI model interactions and user data uploads.


SarthiAI/logs/
│
├── server_log.txt            # Logs for backend server activities
├── user_activity_log.txt     # Logs for tracking user interactions
└── error_log.txt             # Logs for errors and debugging


Workflow Overview:---
---------------------------------
User Interaction: The user accesses the web interface, uploads code or media, or interacts with Sarthi AI for a specific task (e.g., website generation).
Backend API: The backend manages the interaction between the various AIs (Sarthi, Yug, Aadi, Arth, Ved) and handles requests via REST APIs.
Training & Output: The training folder processes new datasets, and the outputs (websites, apps, media) are stored in the output files directory.
Collaboration of AIs: Ved recognizes faces and emotions, Aadi generates music, Arth handles video and media, and Yug generates 3D items.

------------------------------------- 


