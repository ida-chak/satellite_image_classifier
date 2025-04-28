# File paths management
import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Data directories
DATA_DIR = os.path.join(BASE_DIR, 'data')
RAW_DATA_DIR = os.path.join(DATA_DIR, 'raw')
INTERIM_DATA_DIR = os.path.join(DATA_DIR, 'interim')
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, 'processed')

# Output directories
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')
MODELS_DIR = os.path.join(BASE_DIR, 'models')

# Ensure directories exist
for directory in [DATA_DIR, RAW_DATA_DIR, INTERIM_DATA_DIR, PROCESSED_DATA_DIR, OUTPUT_DIR, MODELS_DIR]:
    os.makedirs(directory, exist_ok=True)

# Set random seed
random_seed = 42

# Run training of model - set to True or False
train_model = True
model_history_filename = 'satellite_classification_history.pkl'
trained_model_filename = 'satellite_classification_model.keras'