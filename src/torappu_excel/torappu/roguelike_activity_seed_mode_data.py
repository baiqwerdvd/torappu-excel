from ..common import BaseStruct


class RoguelikeActivitySeedModeData(BaseStruct):
    officialSeedDataList: list["RoguelikeActivitySeedModeData.RoguelikeActivityOfficialSeedData"]
    constData: "RoguelikeActivitySeedModeData.RoguelikeActivitySeedModeConstData"

    class RoguelikeActivityOfficialSeedData(BaseStruct):
        seed: str
        sortId: int
        desc: str

    class RoguelikeActivitySeedModeConstData(BaseStruct):
        seedModeIntro: str
        emptyTextHint: str
        errorTextHint: str
        legitimateTextHint: str
        seedModeConfirmReplacement: str
        difficultyLevelTextHint: str
        lockedDifficultyLevelTextHint: str
        setDifficultyLevelTextHint: str
        notEnabledTextHint: str
        enabledTextHint: str
        useSucceededTextHint: str
        officialUseSucceededTextHint: str
        seedModeLockedTextHint: str
