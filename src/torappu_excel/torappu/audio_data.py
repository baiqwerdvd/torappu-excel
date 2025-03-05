from .battle_voice_data import BattleVoiceData
from .bgm_bank import BGMBank
from .ducking_data import DuckingData
from .fade_style_data import FadeStyleData
from .music_data import MusicData
from .snapshot_bank import SnapshotBank
from .sound_fx_bank import SoundFXBank
from .sound_fx_ctrl_bank import SoundFXCtrlBank
from .voice_lang_type import VoiceLangType
from ..common import BaseStruct


class AudioData(BaseStruct):
    bgmBanks: list[BGMBank]
    soundFXBanks: list[SoundFXBank]
    soundFXCtrlBanks: list[SoundFXCtrlBank]
    snapshotBanks: list[SnapshotBank]
    battleVoice: BattleVoiceData
    musics: list[MusicData]
    duckings: list[DuckingData]
    fadeStyles: list[FadeStyleData]
    soundFxVoiceLang: dict[str, dict[str, dict[VoiceLangType, str]]]
    bankAlias: dict[str, str]
