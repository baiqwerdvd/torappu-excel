from .sandbox_v2_food_attribute import SandboxV2FoodAttribute
from .sandbox_v2_food_mat_type import SandboxV2FoodMatType
from .sandbox_v2_food_variant_type import SandboxV2FoodVariantType
from ..common import BaseStruct

from msgspec import field


class SandboxV2FoodMatData(BaseStruct):
    id_: str = field(name="id")
    type_: SandboxV2FoodMatType = field(name="type")
    sortId: int
    variantType: SandboxV2FoodVariantType
    bonusDuration: int
    buffDesc: str | None = field(default=None)
    attribute: SandboxV2FoodAttribute | None = field(default=None)
