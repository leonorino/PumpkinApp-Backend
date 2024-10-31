import sqlalchemy.exc as exc

import db_manager
from db.user import User


if __name__ == '__main__':
    db_manager.db_init()

    session = db_manager.create_session()
    new_user = User(name='Vlad', hashed_password='hellothere')
    session.add(new_user)
    session.commit()

    other_user = User(name='Vlad')
    session.add(other_user)

    try:
        session.commit()
    except exc.IntegrityError:
        session.rollback()
        print('Usernames must be unique!')

    queried_user = session.query(User).first()
    print(queried_user.name)
