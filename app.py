import os

import fastapi as fast
from fastapi.middleware.cors import CORSMiddleware

from api.routes import router
from api.mock import mock_router

app = fast.FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

if os.environ.get('MOCK', None):
    app.include_router(mock_router)
else:
    app.include_router(router)
