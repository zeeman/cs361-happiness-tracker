import unittest
from models import User


class DBAPIMock:
    """
    Mock class fulfilling DB API 2.0, so we don't actually need a DB in order
    to test the User model.
    """
    pass


class TestUserModel(unittest.TestCase):
    def setUp(self):
        self.user_password = "abcde"
        # create user in DB
        self.user = User(db_interface=DBAPIMock)
        self.user.username = "test_user"
        self.user.set_password(self.user_password)  # need to update - not sure how
        self.user.email = "test@example.com"
        self.user.save()

    def test_registration(self):
        """
        Unit test for user creation.
        """
        pass

    def test_change_password(self):
        """
        Unit test for password change.
        """
        pass

    def test_change_email(self):
        """
        Unit test for change email.
        """
        pass

    # some kind of authentication test
    def test_authentication(self):
        """
        Unit test to verify user authentication works.
        """
        # attempt to authenticate user
        unittest.assertTrue(User.authenticate(self.user.username,
                                              self.user_password))

    def test_fail_authentication(self):
        """
        Check that using invalid password fails.
        """

        unittest.assertFalse(User.authenticate(self.user.username, "invalid password"))

    def test_find_user(self):
        """
        Unit test to locate user in Db.
        """
        # use find method
        user2 = User.find(self.user.id)
        unittest.assertEqual(self.user, user2)
