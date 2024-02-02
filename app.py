from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"World"}
 
@app.post("/api/meraki")
def read_meraki(payload:dict):
    try:
        print("Received Meraki Alert")
        print(payload)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000)
