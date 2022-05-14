from fastapi import FastAPI, Form
import joblib

app = FastAPI()


pipeline = joblib.load("modelos/pipeline1.joblib")
modelo = joblib.load("modelos/model01.joblib")
@app.post("/predict")
def predict(sexo: str=Form(...), 
			edad: int=Form(...),
			monto: int=Form(...), 
			tipo_vivienda: str=(...)):
			
	X = pipeline.transform([[sexo, edad, monto, tipo_vivienda]])
	print("resultado_pipeline",  X)
	prediction = modelo.predict(X)
    print(prediction)
	return None