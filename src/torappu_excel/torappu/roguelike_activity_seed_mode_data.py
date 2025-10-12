from pydantic import BaseModel, ConfigDict


class RoguelikeActivitySeedModeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    officialSeedDataList: list["RoguelikeActivitySeedModeData.RoguelikeActivityOfficialSeedData"]
    constData: "RoguelikeActivitySeedModeData.RoguelikeActivitySeedModeConstData"

    class RoguelikeActivityOfficialSeedData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        seed: str
        sortId: int
        desc: str

    class RoguelikeActivitySeedModeConstData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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
