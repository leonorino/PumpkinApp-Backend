import fastapi as fast

from db_manager import db_init
from api.routes import router

db_init()
app = fast.FastAPI()
app.include_router(router)
