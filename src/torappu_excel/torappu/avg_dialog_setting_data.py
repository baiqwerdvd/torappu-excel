from .avg_dialog_preset_data import AVGDialogPresetData
from ..common import BaseStruct


class AVGDialogSettingData(BaseStruct):
    defaultPresetId: int
    presetList: list[AVGDialogPresetData]
