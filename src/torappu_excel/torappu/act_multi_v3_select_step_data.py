from pydantic import BaseModel, ConfigDict

from .act_multi_v3_prepare_step_type import ActMultiV3PrepareStepType


class ActMultiV3SelectStepData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stepType: ActMultiV3PrepareStepType
    sortId: int
    time: int
    hintTime: int
    title: str
    desc: str | None
