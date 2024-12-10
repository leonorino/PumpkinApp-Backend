import os

import requests
import fastapi as fast
from bs4 import BeautifulSoup

from youtube_transcript_api import YouTubeTranscriptApi as Transcriber
from youtube_transcript_api.formatters import TextFormatter

from api import models
from .intelligence import generate

router = fast.APIRouter()

@router.post('/questions')
def generate_questions(data: models.QuestionsRequest):
    formatter = TextFormatter()
    transcript = Transcriber.get_transcript(data.video_id)
    result = generate(formatter.format_transcript(transcript), data.question_types)
    return result

@router.get('/title/')
def get_title(video_id: str = None):
    if not video_id:
        return

    response = requests.get(f'https://www.youtube.com/watch?v={video_id}')
    soup = BeautifulSoup(response.text)
    link = soup.find_all(name='title')[0]
    title = str(link)
    title = title.replace('<title>', '')
    title = title.replace('</title>', '')
    title = title.replace(' - YouTube', '')

    return {
        'title': title,
    }
