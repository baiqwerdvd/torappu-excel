from collections.abc import Callable
from importlib.resources import open_text
import inspect
import json
from typing import Any, cast


def is_valid_async_func(member: Callable[..., Any], exclude_name: list[str]) -> bool:
    return (
        inspect.iscoroutinefunction(member)
        and not member.__name__.startswith("__")
        and member.__name__ not in exclude_name
    )


def read_json(file_name: str) -> dict[str, object]:
    try:
        with open_text("torappu_excel.json", file_name, encoding="UTF-8") as file:
            return cast(dict[str, object], json.load(file))
    except FileNotFoundError as _:
        raise FileNotFoundError(f"Error reading JSON file: {file_name}")
    except json.JSONDecodeError as e:
        raise e
