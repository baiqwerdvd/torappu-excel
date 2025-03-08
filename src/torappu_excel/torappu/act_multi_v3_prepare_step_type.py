from ..common import CustomIntEnum


class ActMultiV3PrepareStepType(CustomIntEnum):
    NONE = "NONE", 0
    STAGE_CHOOSE = "STAGE_CHOOSE", 1
    ENTRANCE = "ENTRANCE", 2
    CHAR_PICK = "CHAR_PICK", 3
    SYS_ALLOC = "SYS_ALLOC", 4
    SQUAD_CHECK = "SQUAD_CHECK", 5
