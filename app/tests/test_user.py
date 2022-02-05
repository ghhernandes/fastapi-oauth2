import unittest

from ..repository import db, models
from .. import crud
from .. import schemas

class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        self.database = db.DB()
        self.db: db.DB = self.database.LocalSession()
        
    def test_create_user(self):
        user = schemas.UserCreate(nickname="ghhernandes", fullname="Gabriel Hernandes", password="12345")        
        crud.create_user(self.db, user)

        db_user: models.User = crud.get_user_by_nickname(self.db, user.nickname)
        self.assertEqual(db_user.nickname, user.nickname)

    def test_list_all_users(self):
        user1 = schemas.UserCreate(nickname="ghhernandes", fullname="Gabriel Hernandes", password="12345")
        user2 = schemas.UserCreate(nickname="ghhernandes2", fullname="Gabriel Hernandes2",password="12345")
        crud.create_user(self.db, user1)
        crud.create_user(self.db, user2)
        
        users: list[models.User] = crud.list_all_users(self.db)
        self.assertEqual(len(users), 2)

    def test_remove_user(self):
        user = schemas.UserCreate(nickname="ghhernandes", fullname="Gabriel Hernandes", password="12345")
        crud.create_user(self.db, user)

        user_db: models.User = crud.get_user_by_nickname(self.db, user.nickname)
        self.assertIsNotNone(user_db)
        crud.remove_user(self.db, user_db.id)

        db_user: models.User = crud.get_user_by_nickname(self.db, user.nickname)
        self.assertIsNone(db_user)