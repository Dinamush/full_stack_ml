import tensorflow as tf
import os

# Define model path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'saved_models', 'model2.h5')

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
    # Load the model using TensorFlow 2.14+
    model = tf.keras.models.load_model(MODEL_PATH, compile=False)  # Avoid re-compilation for quicker loading
    return model

try:
    model = load_model()
    print("Model loaded successfully.")
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(f"An error occurred: {e}")
