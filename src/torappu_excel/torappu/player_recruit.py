from enum import IntEnum

from ..common import BaseStruct


class PlayerRecruit(BaseStruct):
    normal: "PlayerRecruit.NormalModel"

    class NormalModel(BaseStruct):
        slots: dict[str, "PlayerRecruit.NormalModel.SlotModel"]

        class SlotModel(BaseStruct):
            state: "PlayerRecruit.NormalModel.SlotModel.State"
            tags: list[int]
            selectTags: "list[PlayerRecruit.NormalModel.SlotModel.TagItem]"
            startTs: int
            maxFinishTs: int
            realFinishTs: int
            durationInSec: int

            class TagItem(BaseStruct):
                tagId: int
                pick: int

            class State(IntEnum):
                LOCK = 0
                IDLE = 1
                BUSY = 2
                FAST_FINISH = 3
