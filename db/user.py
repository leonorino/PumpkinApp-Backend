import sqlalchemy as sa
import sqlalchemy.orm as orm
from db_manager import Database


class User(Database):
    """Класс, описывающий сущность Пользователя в базе данных."""

    # Название таблицы в БД.
    __tablename__ = 'users'

    id = orm.mapped_column(sa.Integer, primary_key=True,
        autoincrement=True, nullable=False)
    name = orm.mapped_column(sa.String, nullable=False, unique=True)
    hashed_password = orm.mapped_column(sa.String, nullable=False)
    progress = orm.mapped_column(sa.Integer, nullable=False, default=0)

    # Список ORM-объектов Карточек, принадлежащих пользователю.
    # Не хранится в таблице, является shortcut-ом для запроса
    # SELECT FROM cards WHERE user_id=id
    cards = orm.relationship('Card', back_populates='user')
