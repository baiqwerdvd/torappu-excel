from .act_multi_v3_prepare_step_type import ActMultiV3PrepareStepType
from ..common import BaseStruct


class ActMultiV3SelectStepData(BaseStruct):
    stepType: ActMultiV3PrepareStepType
    sortId: int
    time: int
    hintTime: int
    title: str
    desc: str
