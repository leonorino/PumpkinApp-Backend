import ollama

# Описание JSON-схемы для ответа нейросети.
FREEFORM_SCHEMA = '''{
    "questions": [
        {
            "question": "string",
            "answer": "string"
        }
    ]
}'''

def generate_freeform_questions(transcript, count):
    # Текст видео оборачивается в XML-тэг <transcript>, чтобы чётко отделить текст от следующего промпта.
    prompt = f'<transcript>{transcript}</transcript>\n Generate {count} questions about the provided transcript. Answer using the following JSON schema:\n {FREEFORM_SCHEMA}'
    response = ollama.generate(model='llama3.2', prompt=prompt, stream=False, format='json')
    return response['response']
