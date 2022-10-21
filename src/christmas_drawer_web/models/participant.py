import typing


class Participant:
    def __init__(self, name: str, in_groups: typing.List[int]):
        self.__name = name
        self.__in_groups = in_groups
        self.__pick = None

    def __repr__(self):
        return f'Name: {self.name} - In groups: {self.in_groups} - Picked: {self.pick.name}'

    @property
    def name(self):
        return self.__name

    @property
    def in_groups(self) -> typing.List[int]:
        return self.__in_groups

    @property
    def pick(self):
        return self.__pick

    @pick.setter
    def pick(self, value):
        self.__pick = value
