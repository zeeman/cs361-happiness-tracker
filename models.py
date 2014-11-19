class User:
    def __init__(self, db_interface=None, **kwargs):
        pass

    def save(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    @classmethod
    def find(self, user_id):
        pass

    @classmethod
    def authenticate(self, email, password):
        pass

    def set_password(self, password):
        """
        Handle password hashing
        :param password:
        :return:
        """