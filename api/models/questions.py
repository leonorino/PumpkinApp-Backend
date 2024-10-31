from enum import Enum
from pydantic import BaseModel, PositiveInt


class QuestionTypes(str, Enum):
    """Перечисление возможных типов вопросов"""
    freeform = 'freeform'
    choices = 'choices'


class QuestionsRequest(BaseModel):
    # Поле question_type может принимать только значения из перечисления QuestionTypes.
    question_type: QuestionTypes
    video_id: str
    count: PositiveInt
