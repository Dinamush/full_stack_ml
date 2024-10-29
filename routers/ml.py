from fastapi import APIRouter
from schemas.ml import Model1Input, Model1Output, Model2Input, Model2Output
from services.ml_service import predict_model1, predict_model2

router = APIRouter(prefix="/ml", tags=["Machine Learning"])

@router.post("/model1/predict", response_model=Model1Output)
async def model1_predict(input_data: Model1Input):
    prediction = predict_model1(input_data)
    return {"prediction": prediction}

@router.post("/model2/predict", response_model=Model2Output)
async def model2_predict(input_data: Model2Input):
    sentiment = predict_model2(input_data)
    return {"sentiment": sentiment}
