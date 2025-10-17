from ..common import BaseStruct


class PlayerCrossAppShare(BaseStruct):
    shareMissions: dict[str, "PlayerCrossAppShare.ShareMissionData"]

    class ShareMissionData(BaseStruct):
        counter: int
