from ..common import BaseStruct


class ArkventTaskActorTriggerOperation(BaseStruct):
    operationId: str | None
    operationTemplate: str
    operationParams: dict[str, str]
    finishOperation: bool
    preserveBlackout: bool
