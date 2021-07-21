"""
Models are used to structure a common datatype to be used as object instances
"""


class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password
