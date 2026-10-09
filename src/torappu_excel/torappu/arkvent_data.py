from .arkvent_anim_mix_data import ArkventAnimMixData
from .arkvent_audio_source_data import ArkventAudioSourceData
from .arkvent_bark_data import ArkventBarkData
from .arkvent_head_ui_data import ArkventHeadUIData
from .arkvent_interact_btn_style_data import ArkventInteractBtnStyleData
from .arkvent_name_mapping_data import ArkventNameMappingData
from .arkvent_scene_data import ArkventSceneData
from .arkvent_task_data import ArkventTaskData
from ..common import BaseStruct


class ArkventData(BaseStruct):
    taskData: ArkventTaskData
    sceneDataMap: dict[str, ArkventSceneData]
    nameMappingData: ArkventNameMappingData
    interactBtnStyleDict: dict[str, ArkventInteractBtnStyleData]
    headUIData: dict[str, ArkventHeadUIData]
    barkData: ArkventBarkData
    animMixData: ArkventAnimMixData
    sceneAudioMap: dict[str, list[ArkventAudioSourceData]]
