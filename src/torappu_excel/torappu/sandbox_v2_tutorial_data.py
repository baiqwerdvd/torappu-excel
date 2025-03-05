from .sandbox_v2_guide_quest_data import SandboxV2GuideQuestData
from .sandbox_v2_quest_data import SandboxV2QuestData
from .sandbox_v2_quest_line_data import SandboxV2QuestLineData
from .sandbox_v2_tutorial_basic_const import SandboxV2TutorialBasicConst
from .sandbox_v2_tutorial_repo_char_data import SandboxV2TutorialRepoCharData
from ..common import BaseStruct


class SandboxV2TutorialData(BaseStruct):
    charRepoData: dict[str, SandboxV2TutorialRepoCharData]
    questData: dict[str, SandboxV2QuestData]
    guideQuestData: dict[str, SandboxV2GuideQuestData]
    questLineData: dict[str, SandboxV2QuestLineData]
    basicConst: SandboxV2TutorialBasicConst
