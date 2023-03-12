# run 'python -m unittest test_app.py'
# 'python -m unittest -v test_app.py' to produce more verbose output
# pep8 --first app.py
import pep8
import unittest
from sqlalchemy.exc import IntegrityError
from models import Users
from app import db


class AppTest(unittest.TestCase):

    def setUp(self):
        db.session.close()
        db.drop_all()
        db.create_all()
        assert len(Users.query.all()) == 0

    def tearDown(self):
        db.session.close()
        db.drop_all()
        db.create_all()
        assert len(Users.query.all()) == 0

    def test_pep8(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide()
        result = pep8style.check_files(['app.py', 'app_factory.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

    def test_create_Users(self):
        email = 'test_email'
        password = 'test_password'
        name = 'test_name'
        users = Users(email=email, password=password, name = name)
        add_to_database(Users)

        assert Users in db.session

        assert len(Users.query.filter_by(email=email).all()) == 1
        Users_from_db = Users.get_Users_by_email(email)
        assert Users_from_db.email == email
        assert Users_from_db.check_password(password)
        Users_from_db.set_password("newpassword")
        db.session.commit()

        assert len(Users.query.filter_by(email=email).all()) == 1
        Users_from_db2 = Users.get_Users_by_email(email)
        assert Users_from_db2.email == email
        assert Users_from_db2.check_password("newpassword")

    def test_get_Users_by_id(self):
        email = 'test_email'
        password = 'test_password'
        users = Users(email=email, password=password)
        add_to_database(users)
        assert users in db.session

        assert len(Users.query.filter_by(id=1).all()) == 1
        Users_from_db = Users.get_Users_by_id(1)
        assert Users_from_db.email == email

    def test_Users_already_exists_raises_integrity_error(self):
        add_to_database(Users(email='email', password='password'))
        l = lambda: add_to_database(Users(email='email', password='another'))
        self.assertRaises(IntegrityError, l)

    def test_Users_doesnt_exist_returns_none(self):
        users = Users.get_Users_by_email("bla")
        assert Users is None
        Users2 = Users.get_Users_by_id(100000)
        assert Users2 is None

    def test_Users_incorrect_password(self):
        email = 'email'
        password = 'password'
        add_to_database(Users(email=email, password=password))
        users = Users.get_Users_by_email(email)
        assert Users.password != password
        # assert not bcrypt.check_password_hash(Users.password, 'temp')
        # assert bcrypt.check_password_hash(Users.password, password)


def add_to_database(object):
    db.session.add(object)
    db.session.commit()

if __name__ == '__main__':
    unittest.main()