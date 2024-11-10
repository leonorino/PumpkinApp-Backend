import ollama
from api.models import QuestionTypes


# Описание базовой JSON-схемы для ответа нейросети.
BASE_SCHEMA = '''{
    "questions": [
        {
            "question": string,
            "answer": string
        }
    ]
}'''

FREEFORM_PROMPT = 'questions about the provided transcript'

TRUE_FALSE_PROMPT = 'true/false questions about the provided transcript'
TRUE_FALSE_SCHEMA = '''{
    "questions": [
        {
            "question": string,
            "answer": boolean
        }
    ]
}'''

GAP_PROMPT = 'gap-filling questions about the provided transcript. Mark the gaps with `*` sign'

ONEWORD_PROMPT = '"one word answer" questions about the provided transcript. Make sure that the answer is just one word'

PROMPTS = {
    QuestionTypes.freeform: (FREEFORM_PROMPT, BASE_SCHEMA),
    QuestionTypes.true_false: (TRUE_FALSE_PROMPT, TRUE_FALSE_SCHEMA),
    QuestionTypes.gap: (GAP_PROMPT, BASE_SCHEMA),
    QuestionTypes.oneword: (ONEWORD_PROMPT, BASE_SCHEMA)
}


def generate(transcript, count, question_type):
    # Текст видео оборачивается в XML-тэг <transcript>, чтобы чётко отделить текст от следующего промпта.
    prompt, schema = PROMPTS[question_type]
    prompt = f'<transcript>{transcript}</transcript>\n Generate {count} {prompt}. Answer using the following JSON schema:\n {schema}'
    response = ollama.generate(model='llama3.2', prompt=prompt, stream=False, format='json')
    return response['response']
