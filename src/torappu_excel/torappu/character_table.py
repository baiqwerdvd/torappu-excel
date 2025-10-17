from .character_data import CharacterData
from ..common import BaseStruct


class CharacterTable(BaseStruct):
    chars: dict[str, CharacterData]
