from pydantic import BaseModel, ConfigDict

from .roguelike_sky_module_consts import RoguelikeSkyModuleConsts
from .roguelike_sky_node_data import RoguelikeSkyNodeData
from .roguelike_sky_node_sub_type_data import RoguelikeSkyNodeSubTypeData


class RoguelikeSkyModuleData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    nodeData: dict[str, RoguelikeSkyNodeData]
    subTypeData: list[RoguelikeSkyNodeSubTypeData]
    moduleConsts: RoguelikeSkyModuleConsts
