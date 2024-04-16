from fastapi import FastAPI

app = FastAPI()

#defining method
@app.get("/api/greeting")

#define function
def greet():
    return{"message": "Hello Everyone"}


if __name__ =="__main__":
    #import uvicorn response
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port =8000)
