from pydantic import BaseModel

class Model1Input(BaseModel):
    feature_a: float
    feature_b: float

class Model1Output(BaseModel):
    prediction: float

class Model2Input(BaseModel):
    text: str

class Model2Output(BaseModel):
    sentiment: str

class TitanicInput(BaseModel): #replace this with titanic fields
    sentiment: str

class TitanicOutput(BaseModel): 
    sentiment: str
