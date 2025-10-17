from .open_server_chain_login import OpenServerChainLogin
from .open_server_check_in import OpenServerCheckIn
from .open_server_full_open import OpenServerFullOpen
from ..common import BaseStruct


class PlayerOpenServer(BaseStruct):
    chainLogin: OpenServerChainLogin
    checkIn: OpenServerCheckIn
    fullOpen: OpenServerFullOpen
