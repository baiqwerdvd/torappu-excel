from pydantic import BaseModel, ConfigDict

from .open_server_chain_login import OpenServerChainLogin
from .open_server_check_in import OpenServerCheckIn
from .open_server_full_open import OpenServerFullOpen


class PlayerOpenServer(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    chainLogin: OpenServerChainLogin
    checkIn: OpenServerCheckIn
    fullOpen: OpenServerFullOpen
