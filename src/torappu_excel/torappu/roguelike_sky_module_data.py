from .roguelike_sky_module_consts import RoguelikeSkyModuleConsts
from .roguelike_sky_node_data import RoguelikeSkyNodeData
from .roguelike_sky_node_sub_type_data import RoguelikeSkyNodeSubTypeData
from ..common import BaseStruct


class RoguelikeSkyModuleData(BaseStruct):
    nodeData: dict[str, RoguelikeSkyNodeData]
    subTypeData: list[RoguelikeSkyNodeSubTypeData]
    moduleConsts: RoguelikeSkyModuleConsts
