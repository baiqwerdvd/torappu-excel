from ..common import BaseStruct


class PlayerPushFlags(BaseStruct):
    hasGifts: int
    hasFriendRequest: int
    hasClues: int
    hasFreeLevelGP: int
    status: int
