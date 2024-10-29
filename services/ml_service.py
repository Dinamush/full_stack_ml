from ml_models import model1, titanic_survival
from schemas.ml import Model1Input, Model2Input, TitanicInput, TitanicOutput

def predict_model1(input_data: Model1Input):
    features = [[input_data.feature_a, input_data.feature_b]]
    prediction = model1.model.predict(features)
    return prediction[0]

def predict_model2(input_data: Model2Input):
    # Assuming model2 is a text classification model
    prediction = model2.model.predict([input_data.text])
    sentiment = 'positive' if prediction[0] > 0.5 else 'negative'
    return sentiment

def predict_titanic(input_data: TitanicInput):
    
    pass
