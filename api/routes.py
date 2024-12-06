import os

import requests
import fastapi as fast

from youtube_transcript_api import YouTubeTranscriptApi as Transcriber
from youtube_transcript_api.formatters import TextFormatter

from api import models
from .intelligence import generate

router = fast.APIRouter()

@router.post('/questions')
def generate_questions(data: models.QuestionsRequest):
    print('Kinda there')

    formatter = TextFormatter()
    transcript = Transcriber.get_transcript(data.video_id)
    result = generate(formatter.format_transcript(transcript), data.question_types)

    return result
