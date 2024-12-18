# This file is automatically generated by pyo3_stub_gen
# ruff: noqa: E501, F401

import os
import pathlib
import typing
from enum import Enum, auto

MY_CONSTANT: int
class A:
    x: int
    def __new__(cls, x:int) -> A:
        ...

    def show_x(self) -> None:
        ...

    def ref_test(self, x:dict) -> dict:
        ...


class Number(Enum):
    FLOAT = auto()
    INTEGER = auto()

def ahash_dict() -> dict[str, int]:
    ...

def create_a(x:int) -> A:
    ...

def create_dict(n:int) -> dict[int, list[int]]:
    ...

def echo_path(path:str | os.PathLike | pathlib.Path) -> str:
    ...

def read_dict(dict:typing.Mapping[int, typing.Mapping[int, int]]) -> None:
    ...

def str_len(x:str) -> int:
    r"""
    Returns the length of the string.
    """
    ...

def sum(v:typing.Sequence[int]) -> int:
    r"""
    Returns the sum of two numbers as a string.
    """
    ...

class MyError(RuntimeError): ...

