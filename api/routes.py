import json

import fastapi as fast
from fastapi.responses import JSONResponse

from youtube_transcript_api import YouTubeTranscriptApi as Transcriber
from youtube_transcript_api.formatters import TextFormatter

from db_manager import create_session
from db import models as db_models
from api import models
from .intelligence import generate_freeform_questions

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
    formatter = TextFormatter()

    # Запрашиваем транскрипцию видео с указанным ID.
    transcript = Transcriber.get_transcript(data.video_id)

    # Форматируем транскрипцию, как обычный текст.
    text = formatter.format_transcript(transcript)

    # Генерируем запросы.
    questions_json = generate_freeform_questions(text, count=data.count)

    # Почему-то, если возвращать JSON от нейросети напрямую, получается некрасиво.
    # Поэтому конвертируем JSON-строку в словарь content, а потом передаём его в JSONResponse.
    content = json.loads(questions_json)
    return JSONResponse(content=content)
