from .sandbox_v2_food_variant_type import SandboxV2FoodVariantType
from ..common import BaseStruct

from msgspec import field


class SandboxV2FoodVariantData(BaseStruct):
    type_: SandboxV2FoodVariantType = field(name="type")
    name: str
    usage: str
