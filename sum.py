from fastapi import FastAPI

app = FastAPI()

@app.get("/add")
async def add_numbers(num1: int, num2: int):
    return {"result": num1 + num2}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
