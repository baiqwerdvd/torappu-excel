from .arkvent_task_var_seq_compare_operation import ArkventTaskVarSeqCompareOperation
from ..common import BaseStruct


class ArkventTaskShowCondition(BaseStruct):
    conditionType: str
    varSeqList: list[str]
    type: ArkventTaskVarSeqCompareOperation
    value: int
