import joblib
from utils.df import format_inputs
import os

# Define model path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'saved_models', 'titanic.joblib')  # Use .joblib for sklearn models

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
    # Load the model using joblib
    model = joblib.load(MODEL_PATH)
    return model

try:
    model = load_model()
    print("Model loaded successfully.")
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(f"An error occurred: {e}")
