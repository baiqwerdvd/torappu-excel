from typing import Any

from ..common import BaseStruct


class PlayerResLock(BaseStruct):
    consumable: dict[str, Any]
    inventory: dict[str, Any]
