import datetime
from enum import Enum


class Employee:
    def __init__(self, name, salary, year, month, day):
        self.__name = name
        self.__salary = salary
        self.__hire_day = datetime.date(year, month, day)

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def get_hire_day(self):
        return self.__hire_day

    def raise_salary(self, percent):
        self.__salary += (self.__salary * percent / 100)


class Manager(Employee):
    def __init__(self, name, salary, year, month, day, manager_rating):
        super().__init__(name, salary, year, month, day)
        self.__manager_rating = manager_rating
        self.__bonus = 0

    def improve_manager_rating(self, add_rating):
        self.__manager_rating += add_rating

    def set_bonus(self, bonus):
        self.__bonus = bonus

    def get_salary(self):
        return super().get_salary() + self.__bonus


class ExecutiveManager(Manager):
    def __init__(self, name, salary, year, month, day, manager_rating):
        super().__init__(name, salary, year, month, day, manager_rating)


class Secretary(Employee):
    def __init__(self, name, salary, year, month, day, manager: Manager):
        super().__init__(name, salary, year, month, day)
        self.__manager = manager

    def set_manager(self, new_manager):
        self.__manager = new_manager


class ProgrammerLevel(Enum):
    JUNIOR = 1
    MIDDLE = 2
    SENIOR = 3
    LEAD = 4


class ProgrammerSpecialization(Enum):
    FRONTEND = 1
    BACKEND = 2
    MOBILE = 3
    DATA_SCIENCE = 4
    TESTING = 5


class Programmer(Employee):
    def __init__(self, name, salary, year, month, day,
                       level: ProgrammerLevel,
                       specialization: ProgrammerSpecialization):
        super().__init__(name, salary, year, month, day)
        self.__level = level
        self.__specialization = specialization

    def set_level(self, new_level: ProgrammerLevel):
        self.__level = new_level

    def get_specialization(self):
        return self.__specialization

