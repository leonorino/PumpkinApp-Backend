import sqlalchemy as sa
import sqlalchemy.orm as orm
from db_manager import Database


class Card(Database):
    """Класс, описывающий сущность Карточки в базе данных."""

    # Название таблицы в БД.
    __tablename__ = 'cards'

    id = orm.mapped_column(sa.Integer, primary_key=True,
        autoincrement=True, nullable=False)
    name = orm.mapped_column(sa.String, nullable=False)
    content = orm.mapped_column(sa.String, nullable=False)

    # id пользователя, которому принадлежит Карточка. Внешний ключ.
    user_id = orm.mapped_column(sa.ForeignKey('users.id'))

    # Ссылка на ORM-объект класса User, который связан с Карточкой.
    # Не хранится в таблице, является shortcut-ом для запроса
    # SELECT FROM users WHERE id=user_id
    user = orm.relationship('User', back_populates='cards')
