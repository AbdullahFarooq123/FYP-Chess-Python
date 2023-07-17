from enum import Enum


class TestsOf(Enum):
    ALL = [True, False]
    PASSED = [True]
    FAILED = [False]
    NONE = []
