from .anniv7th_clue_const_data import Anniv7thClueConstData
from .anniv7th_clue_data import Anniv7thClueData
from .anniv7th_clue_group_data import Anniv7thClueGroupData
from .anniv7th_clue_reward_data import Anniv7thClueRewardData
from .anniv7th_display_node_data import Anniv7thDisplayNodeData
from ..common import BaseStruct


class Anniv7thMainlineData(BaseStruct):
    clueGroupData: dict[str, Anniv7thClueGroupData]
    clueData: dict[str, Anniv7thClueData]
    clueRewardData: list[Anniv7thClueRewardData]
    displayNodeData: list[Anniv7thDisplayNodeData]
    constData: Anniv7thClueConstData
