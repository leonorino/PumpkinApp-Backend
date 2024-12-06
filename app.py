import os

import fastapi as fast

from api.routes import router
from api.mock import mock_router

app = fast.FastAPI()
if os.environ.get('MOCK', None):
    app.include_router(mock_router)
else:
    app.include_router(router)
