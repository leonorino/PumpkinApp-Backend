import json
import logging

import requests

import fastapi as fast
from fastapi import HTTPException
from fastapi.responses import JSONResponse

from youtube_transcript_api import YouTubeTranscriptApi as Transcriber
from youtube_transcript_api.formatters import TextFormatter

from db_manager import create_session
from db import models as db_models
from api import models
from .intelligence import generate

YOUTUBE_URL = 'https://youtube.com'

logger = logging.getLogger(__name__)
router = fast.APIRouter()

@router.get('/users')
def create_user():
    # Создаём сессию взаимодействия с базой данных.
    session = create_session()

    # Запрашиваем список всех Пользователей.
    users = session.query(db_models.User).all()
    # Конвертируем ORM-модели в Pydantic-модели, чтобы вернуть корректный JSON.
    return [models.User.from_orm(user) for user in users]

@router.post('/questions')
def generate_questions(data: models.QuestionsRequest):
    print(data)

    youtube_response = requests.get(YOUTUBE_URL)
    if not youtube_response.ok:
        print("YouTube seems to be unreachable")
        raise HTTPException(status_code=503)

    formatter = TextFormatter()

    print("Starting to fetch transcript from YouTube")
    # Запрашиваем транскрипцию видео с указанным ID.
    transcript = Transcriber.get_transcript(data.video_id)

    # Форматируем транскрипцию, как обычный текст.
    text = formatter.format_transcript(transcript)
    print("Successfully fetched transcript from YouTube")

    # Генерируем запросы.
    print("Starting to generate questions using Ollama")
    questions_json = generate(text, data.count, data.question_type)
    print("Successfully generated questions using Ollama")

    # Почему-то, если возвращать JSON от нейросети напрямую, получается некрасиво.
    # Поэтому конвертируем JSON-строку в словарь content, а потом передаём его в JSONResponse.
    content = json.loads(questions_json)
    return JSONResponse(content=content)
