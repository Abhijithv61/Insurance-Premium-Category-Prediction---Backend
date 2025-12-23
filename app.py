from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from model.predict import predict_output, model, MODEL_VERSION

# Create a fastapi object
app = FastAPI()
        

# Create home endpoint (human readable)
@app.get('/')
def home():
    return {'message': 'Insurance Premium Categegory Prediction'}

# Create Health check endpoint (for cloud services)
@app.get('/health')
def health():
    return {'status':'OK',
            'version': MODEL_VERSION,
            'model_loaded': model is not None}

# Create the route to predict
@app.post('/predict')
def predict_premium(data: UserInput):

    user_input = {
        'bmi':data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation       
    }

    try:

        prediction = predict_output(user_input)

        return JSONResponse(status_code=200, content={'Predicted Category': prediction})
    
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))