from collections.abc import Callable, Iterable, Iterator
from copy import copy, deepcopy
from enum import Enum
import json
from typing import Any, Self, dataclass_transform

from msgspec import Struct, convert, field, json as mscjson, msgpack as mscmsgpack
from typing_extensions import override


class CustomIntEnum(Enum):
    def __new__(cls, value: str, int_value: int) -> Self:
        obj = object.__new__(cls)
        obj._value_ = value
        obj._int_value_ = int_value
        return obj

    def __init__(self, value: str, int_value: int) -> None:
        self._int_value_: int = int_value

    @override
    def __str__(self) -> str:
        return f"{super().__str__()}:{self._int_value_}"

    def __int__(self) -> int:
        return self._int_value_

    @property
    @override
    def value(self) -> int:
        return self._int_value_

    @property
    @override
    def name(self) -> str:
        return self._value_

    @override
    def __hash__(self) -> int:
        return hash(self._int_value_)

    @override
    def __eq__(self, other: object) -> bool:
        if isinstance(other, int):
            return self._int_value_ == other
        elif isinstance(other, CustomIntEnum):
            return self._int_value_ == other._int_value_
        return False

    def __gt__(self, other: "int | CustomIntEnum") -> bool:
        if isinstance(other, int):
            return self._int_value_ > other
        return self._int_value_ > other._int_value_

    def __ge__(self, other: "int | CustomIntEnum") -> bool:
        if isinstance(other, int):
            return self._int_value_ >= other
        return self._int_value_ >= other._int_value_

    def __lt__(self, other: "int | CustomIntEnum") -> bool:
        if isinstance(other, int):
            return self._int_value_ < other
        return self._int_value_ < other._int_value_

    def __le__(self, other: "int | CustomIntEnum") -> bool:
        if isinstance(other, int):
            return self._int_value_ <= other
        return self._int_value_ <= other._int_value_

    def __and__(self, other: "int | CustomIntEnum") -> int:
        if isinstance(other, int):
            return self._int_value_ & other
        return self._int_value_ & other._int_value_

    def __or__(self, other: "int | CustomIntEnum") -> int:
        if isinstance(other, int):
            return self._int_value_ | other
        return self._int_value_ | other._int_value_

    @classmethod
    @override
    def _missing_(cls, value: object) -> Self:
        for member in cls:
            if member.value == value or member._int_value_ == value:
                return member
        return super()._missing_(value)


@dataclass_transform(field_specifiers=(field,))
class BaseStruct(Struct, forbid_unknown_fields=True, omit_defaults=True, gc=False):
    class Config:
        encoder: mscjson.Encoder = mscjson.Encoder()

    @classmethod
    def convert(
        cls,
        obj: Any,
        *,
        strict: bool = True,
        from_attributes: bool = False,
        dec_hook: Callable[[type, Any], Any] | None = None,
        builtin_types: Iterable[type] | None = None,
        str_keys: bool = False,
    ) -> Self:
        if obj is None:
            return None  # pyright: ignore[reportReturnType]
        if isinstance(obj, BaseStruct):
            if idCheck := getattr(obj, "id_", None):
                if isinstance(idCheck, object):
                    setattr(obj, "id_", str(idCheck))
            obj = obj.model_dump()
        return convert(
            obj=obj,
            type=cls,
            strict=strict,
            from_attributes=from_attributes,
            dec_hook=dec_hook,
            builtin_types=builtin_types,
            str_keys=str_keys,
        )

    def __iter__(self) -> Iterator[tuple[str, Any]]:
        for field_name in self.__struct_fields__:
            yield field_name, getattr(self, field_name)

    def keys(self) -> Iterator[str]:
        yield from self.__struct_fields__

    def values(self) -> Iterator[Any]:
        for field_name in self.__struct_fields__:
            yield getattr(self, field_name)

    def model_dump(self) -> dict[str, Any]:
        return mscjson.decode(mscjson.encode(self))

    def encode(self) -> bytes:
        return mscmsgpack.encode(self)

    def to_string(self) -> str:
        return json.dumps(self.model_dump(), ensure_ascii=False, separators=(",", ":"))

    def dump_child(self, target: str) -> Any:
        return self.model_dump()[target]

    def model_copy(self, *, deep: bool = False) -> Self:
        return deepcopy(self) if deep else copy(self)
