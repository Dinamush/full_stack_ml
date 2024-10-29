import pandas as pd

def format_inputs(inputs: list) -> pd.DataFrame: #takes a list of inputs
    data = [input.dict() for input in inputs]
    return pd.DataFrame(data)
