from enum import IntEnum


class UserRole(IntEnum):
    CHAIRMAN = 0
    MEMBER = 1
    WORDCHAIRMAN = 2
    CITIZEN = 3

    @classmethod
    def select_role(cls):
        return [(key.value, key.name) for key in cls]


class Gender(IntEnum):
    MALE = 0
    FEMALE = 1
    OTHERS = 2

    @classmethod
    def select_gender(cls):
        return [(key.value, key.name) for key in cls]
