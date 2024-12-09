from enum import Enum
from typing import Dict
from pydantic import BaseModel, PositiveInt


class QuestionTypes(str, Enum):
    """Перечисление возможных типов вопросов"""
    true_false = 'true_false'
    gap = 'gap'
    choice = 'choice'

    def get_name(self):
        return self.name


class QuestionsRequest(BaseModel):
    # Поле question_type может принимать только значения из перечисления QuestionTypes.
    question_types: Dict[QuestionTypes, PositiveInt]
    video_id: str
