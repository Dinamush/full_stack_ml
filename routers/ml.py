from fastapi import APIRouter, HTTPException
from schemas.ml import (
    Model1Input,
    Model1Output,
    Model2Input,
    Model2Output,
    TitanicInput,
    TitanicOutput
)
from services.ml_service import predict_model1, predict_model2, predict_titanic
from utils.df import format_inputs  # Ensure this path is correct based on your project structure
import pandas as pd


router = APIRouter(prefix="/ml", tags=["Machine Learning"])

@router.post("/model1/predict", response_model=Model1Output)
async def model1_predict(input_data: Model1Input):
    try:
        prediction = predict_model1(input_data)
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

@router.post("/model2/predict", response_model=Model2Output)
async def model2_predict(input_data: Model2Input):
    try:
        sentiment = predict_model2(input_data)
        return {"sentiment": sentiment}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")


@router.post("/titanic/predict", response_model=TitanicOutput, summary="Predict Titanic Survival", description="Predict whether a passenger survived the Titanic disaster based on input features.")
async def titanic_predict(input_data: TitanicInput):
    """
    Predict the survival of a Titanic passenger.

    - **Pclass**: Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)
    - **Sex**: Gender of the passenger ('male' or 'female')
    - **Age**: Age of the passenger
    - **SibSp**: Number of siblings/spouses aboard
    - **Parch**: Number of parents/children aboard
    - **Fare**: Passenger fare
    - **Embarked**: Port of Embarkation ('S', 'C', or 'Q')
    """
    try:
        # Preprocess the input data
        df = format_inputs([input_data])
        
        df.head()
        
        
        # Invoke the prediction service
        prediction = predict_titanic(df)
        
        # Ensure the prediction is in the expected format
        if isinstance(prediction, (list, pd.Series, pd.DataFrame)):
            survived = int(prediction[0])  # Assuming prediction returns a list-like object
        else:
            survived = int(prediction)  # If prediction is a single value
        
        return {"survived": survived}
    
    except Exception as e:
        # Log the exception details if logging is set up
        # logger.error(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")
