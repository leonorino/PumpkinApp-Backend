# PumpkinApp-Backend
**PumpkinApp** is a mobile application designed to help users improve their English language skills. The app allows users to generate personalized quizzes based on video content they choose.
**PumpkinApp-Backend** a web server with several API endpoints, a working horse behind [PumpkinApp-Interface](https://github.com/ellohar/PumpkinApp-Interface).

## Overview
Web server provides 2 main endpoints:

#### `POST /generate`
Generates questions based on the transcript of a specified YouTube video.
Expects a JSON payload with the following structure (by example):
```json
{
    "video_id": "h9Z4oGN89MU",
    "question_types": {
        "multiple_choice": 5,
        "true_false": 5
    }
}
```
Returns the following JSON (by example):
```json
{
  "choice": [
    {
      "question": "Choice Question 1",
      "answer": 0,
      "variants": [
        "Variant 1",
        "Variant 2"
      ]
    },
    {
      "question": "Choice Question 2",
      "answer": 1,
      "variants": [
        "Variant 1",
        "Variant 2"
      ]
    }
  ],
  "true_false": [
    {
      "question": "True/False Question 1",
      "answer": false
    },
    {
      "question": "True/False Question 2",
      "answer": true
    },
  ],
}
```
`question_types` should conform with `api/models/questions.QuestionTypes` dictionary.
Integers should be non-negative. `video_id` should be a vaild YouTube video ID.

#### `GET /title`
Retrieves the title of a specified YouTube video.
Expects a valid YouTube `video_id` as a query parameter.

## Prerequisites
- [Ollama](https://ollama.com/download) - A tool designed to run LLMs locally.

## Project structure
- `app.py` - main entry point with CORS middleware to ensure proper operation with web-browsers.
- `api/routes.py` - main router with valid endpoints for interaction with YouTube and Ollama.
- `api/mock.py` - mock router for interface testing.
- `models/questions.py` - data model for `/questions` endpoint.

### Installation
1. Create a new python virtual environment, or use an existing one for all I care. Python 3.12 was used during development, earlier versions were not tested.
2. Install required packages with `pip install -r requirements.txt`.
3. Ensure that ollama is running, with Qwen 2.5 model installed: `ollama pull qwen2.5`.
4. Launch the server with: `fastapi dev app.py --reload` from root. To run in mock mode, set MOCK environment variable to 1. On UNIX, `MOCK=1`, on Windows, idk.
