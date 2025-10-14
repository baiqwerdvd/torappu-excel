from enum import IntEnum

from pydantic import BaseModel, ConfigDict


class PlayerRecruit(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    normal: "PlayerRecruit.NormalModel"

    class NormalModel(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        slots: dict[str, "PlayerRecruit.NormalModel.SlotModel"]

        class SlotModel(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            state: "PlayerRecruit.NormalModel.SlotModel.State"
            tags: list[int]
            selectTags: "list[PlayerRecruit.NormalModel.SlotModel.TagItem]"
            startTs: int
            maxFinishTs: int
            realFinishTs: int
            durationInSec: int

            class TagItem(BaseModel):
                model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

                tagId: int
                pick: bool

            class State(IntEnum):
                LOCK = 0
                IDLE = 1
                BUSY = 2
                FAST_FINISH = 3
