from ..common import CustomIntEnum


class SandboxPermItemType(CustomIntEnum):
    NONE = "NONE", 0
    TACTICAL = "TACTICAL", 1
    BUILDING = "BUILDING", 2
    BUILDINGMAT = "BUILDINGMAT", 3
    FOOD = "FOOD", 4
    FOODMAT = "FOODMAT", 5
    SPECIALMAT = "SPECIALMAT", 6
    COIN = "COIN", 9
    CRAFT = "CRAFT", 10
    PLACEHOLDER = "PLACEHOLDER", 11
    STAMINAPOT = "STAMINAPOT", 12
    ANIMAL = "ANIMAL", 13
    INSECT = "INSECT", 14
    SLUGITEM = "SLUGITEM", 15
