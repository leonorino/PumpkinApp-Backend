import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session, DeclarativeBase

__factory = None
DB_PATH = 'db/database.sqlite'


class Database(DeclarativeBase):
    """Базовый класс, от которого будет наследоваться каждая ORM-модель."""
    pass


def db_init(db_file=DB_PATH):
    """Функция для инициализации подключения к базе данных."""
    global __factory

    # Если инициализация уже была проведена (__factory не None), ничего делать не нужно.
    if __factory:
        return

    # Создаём строку, описывающую путь для подключения к базе данных.
    # Начинаем с sqlite:/// - указываем драйвер, который будет использован для подключения.
    # ?check_same_thread=False разрешает подключаться к файлу БД из разных потоков (если потом появится многопоточность).
    db_file = db_file.strip()
    connection_string = f'sqlite:///{DB_PATH}?check_same_thread=False'

    # Подключаемся к базе данных.
    # Если echo=True, все SQL-команды во время работы будут логироваться в консоль.
    engine = sa.create_engine(connection_string, echo=False)
    # Сохраняем генератор сессий, чтобы использовать его в будущем.
    __factory = orm.sessionmaker(bind=engine)

    # Импортируем, чтобы создались классы, наследующиеся от Database.
    from db import models

    # Просим создать метаданные (таблицы, схемы, ограничения) для всех моделей, которые наследуются от Database.
    Database.metadata.create_all(engine)


def create_session():
    global __factory
    # Вызываем функцию-генератор сессий, чтобы создать новую сессию.
    return __factory()
