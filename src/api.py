from fastapi import FastAPI
from rp_handler import generate_image

app = FastAPI()

@app.post("/generate_image")
async def generate_image_endpoint(job: dict):
    return generate_image(job)