#!/user/bin/python3

from fastapi import FastAPI
from routers import delivery_services
from pydantic_models.delivery_services import delivery_services_in as pydantictest


print("**********************************")
print("**********************************")
print(pydantictest.model_fields)
print("**********************************")
print("**********************************")

# app creation statement
app = FastAPI()

# include routers:
app.include_router(delivery_services.router)

# the root route
@app.get("/")
def root():
    return {"message": "the API v1 is active"}
