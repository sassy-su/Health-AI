# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class HealthData(BaseModel):
#     weight: float
#     height: float

# @app.post("/bmi")
# def bmi(data: HealthData):
#     if data.height > 0:
#         bmi_val = data.weight / ((data.height / 100) ** 2)
#         return {"bmi": round(bmi_val, 2)}
#     return {"error": "Invalid height"}
