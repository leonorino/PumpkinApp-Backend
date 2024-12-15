# PumpkinApp-Backend
**PumpkinApp** is a mobiwe appwication designyed to hewp usews impwuv theiw Engwish wanguage skiwws. The app awwows usews to genyewate personyalized quizzes based on video content they choose.
**PumpkinApp-Backend** a web sewvew with sevewaw API endpoints, a wowking howse behind [PumpkinApp-Intewface](https://github.com/ellohar/PumpkinApp-Interface).

## Ovewview
Web sewvew pwovides 2 main endpoints:

#### `POST /generate`
Genyewates questions based on the twanscwipt of a specified YouTube video.
Expects a JSON payload with the fowwowing stwuctuwe (by exampwe):
```json
{
    "video_id": "h9Z4oGN89MU",
    "question_types": {
        "multiple_choice": 5,
        "true_false": 5
    }
}
```
Wetuwns the fowwowing JSON (by exampwe):
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
`question_types` shouwd confowm with `api/models/questions.QuestionTypes` dictionyawy.
Integews shouwd be nyon-nyegative. `video_id` shouwd be a vaiwd YouTube video ID.

#### `GET /title`
Retwieves the titwe of a specified YouTube video.
Expects a vawid YouTube `video_id` as a quewy pawametew.

## Pwewequisites
- [Owwama](https://ollama.com/download) - A toow designyed to wun WWMs wocawwy.

## Pwoject stwuctuwe
- `app.py` - main entwy point with CORS middwewawe to ensuwe proper opewation with web-bwowsews.
- `api/routes.py` - main woutew with vawid endpoints fow intewaction with YouTube and Owwama.
- `api/mock.py` - mock woutew fow intewface testing.
- `modews/questions.py` - data modew fow `/questions` endpoint.

### Instawwation
1. Cweate a nyew python viwtuaw enviwonment, ow use an existing onye fow all I cawe. Python 3.12 was used during devewopment, eawwiew versions wewe nyot tested.
2. Instaww wequiwed packages with `pip install -w requirements.txt`.
3. Ensuwe that owwama is wunnying, with Qwen 2.5 modew installed: `ollama pull qwen2.5`.
4. Waunch the sewvew with: `fastapi dev app.py --reload` fwom root. To wun in mock mode, set MOCK enviwonment variable to 1. On UNyIX, `MOCK=1`, on Windows, i don't knyow.
