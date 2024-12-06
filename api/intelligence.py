from typing import List
from random import choice
from pprint import pprint

import instructor
from openai import OpenAI
from pydantic import BaseModel
from langchain.text_splitter import RecursiveCharacterTextSplitter

from api.models import QuestionTypes


# Описание базовой JSON-схемы для ответа нейросети.
class TrueFalseAnswer(BaseModel):
    question: str
    answer: bool


class GapAnswer(BaseModel):
    question: str
    word: str


class MultipleChoiceAnswer(BaseModel):
    question: str
    answer: int
    variants: List[str]

MULTIPLE_CHOICE_PROMPT = 'Generate a question about the following video transcript that will require choosing only one variant from following ones.' \
    ' Provide variants and index of the correct answer.'
GAP_PROMPT = 'Take a really super-dooper small contextual part of the following video transcript and replace one interesting word in it with a gap, mark the spot with $.' \
    ' Provide the part with a gap and a missing word.'
TRUE_FALSE_PROMPT = 'Generate a true/false question about the following video transcript.'

PROMPTS = {
    QuestionTypes.true_false: (TRUE_FALSE_PROMPT, TrueFalseAnswer),
    QuestionTypes.gap: (GAP_PROMPT, GapAnswer),
    QuestionTypes.multiple_choice: (MULTIPLE_CHOICE_PROMPT, MultipleChoiceAnswer),
}

client = instructor.from_openai(
    OpenAI(
        base_url='http://localhost:11434/v1',
        api_key='ollama',
    ),
    mode=instructor.Mode.JSON,
)


def generate(transcript, question_types):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
        length_function=len,
        is_separator_regex=False,
    )
    chunks = set(splitter.split_text(transcript))
    results = {}

    text_num = 0
    for question_type, count in question_types.items():
        prompt, model = PROMPTS[question_type]
        current_chunks = set(chunks)
        results[question_type.get_name()] = []
        for _ in range(count):
            text = choice(tuple(current_chunks)) # I know all the bullshit I do with those sets is a war crime, all right?
            user_prompt = f'{prompt} \n{text}'
            response = client.chat.completions.create(
                model='qwen2.5',
                messages=[
                    {
                        'role': 'user',
                        'content': user_prompt,
                    }
                ],
                response_model=model,
            )
            text_num += 1
            current_chunks.remove(text)
            results[question_type.get_name()].append(response.dict())


    pprint(results)
    return results
