import pandas as pd
import pickle

# Import the ML model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

# Ideally get the model version from the version directories like MlFlow
MODEL_VERSION = '1.0.0'

def predict_output(user_input: dict):

    input_df = pd.DataFrame([user_input])
    
    output = model.predict(input_df)[0]

    return output