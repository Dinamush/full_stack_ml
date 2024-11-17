from ml_models import model1, titanic_survival
from schemas.ml import Model1Input, Model2Input, TitanicInput, TitanicOutput
import pandas as pd
from typing import Any

def predict_model1(input_data: Model1Input):
    features = [[input_data.feature_a, input_data.feature_b]]
    prediction = model1.model.predict(features)
    return prediction[0]

def predict_model2(input_data: Model2Input):
    # Assuming model2 is a text classification model
    prediction = model2.model.predict([input_data.text])
    sentiment = 'positive' if prediction[0] > 0.5 else 'negative'
    return sentiment

def predict_titanic(input_data: TitanicInput) -> int:
    """
    Generates survival predictions for Titanic passengers.
    
    Parameters:
    - df (pd.DataFrame): Preprocessed input data.
    
    Returns:
    - prediction: The model's prediction output.
    
    Raises:
    - Exception: If prediction fails.
    """
    try:
        # Generate predictions using the loaded model
        prediction = model.predict(df)
        return prediction
    except Exception as e:
        # Optionally, log the error if logging is set up
        # logger.error(f"Error during prediction: {e}")
        raise e  # Propagate the exception to be handled by the caller
