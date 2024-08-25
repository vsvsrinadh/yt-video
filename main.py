from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development (change in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Define the Pydantic model for the request body
class AddRequest(BaseModel):
    a: int
    b: int

@app.post("/add")
async def add_num(request: AddRequest):
    return {"result": request.a + request.b}
