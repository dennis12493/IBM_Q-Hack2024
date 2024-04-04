from fastapi import FastAPI
from pydantic import BaseModel
import create_transcript

app = FastAPI()

@app.get("/")
def get_root():
    return "API is running!"

@app.get("/api/transcript/youtube/{video_id}")
def get_youtube_transcript(video_id: str):
    return create_transcript.get_sanized_transscript(video_id)
