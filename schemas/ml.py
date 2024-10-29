from pydantic import BaseModel
from typing import Literal

class Model1Input(BaseModel):
    feature_a: float
    feature_b: float

class Model1Output(BaseModel):
    prediction: float

class Model2Input(BaseModel):
    text: str

class Model2Output(BaseModel):
    sentiment: str
    
    


class TitanicInput(BaseModel): 
    Pclass: int
    Sex: Literal['male', 'female']  # Constraining to specific values
    Age: int
    SibSp: int  # Number of siblings/spouses aboard
    Parch: int  # Number of parents/children aboard
    Fare: float
    Embarked: Literal['S', 'C', 'Q']  # Limiting to valid characters

class TitanicOutput(BaseModel):
    survived: int  # Typically 0 or 1 for binary classification

    
