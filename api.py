from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route for the root endpoint
@app.get("/")
async def read_root():
    return {"username": "JYkAlGGbOQSAaInFFk6vQKnH",
            "password": "Z0ucEe7ckXqLXfEeEPjOHjwh"}
