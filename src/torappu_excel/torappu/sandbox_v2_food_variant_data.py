from .sandbox_v2_food_variant_type import SandboxV2FoodVariantType
from ..common import BaseStruct


class SandboxV2FoodVariantData(BaseStruct):
    type: SandboxV2FoodVariantType
    name: str
    usage: str
