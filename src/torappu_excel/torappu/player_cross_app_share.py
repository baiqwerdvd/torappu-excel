from pydantic import BaseModel, ConfigDict


class PlayerCrossAppShare(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    shareMissions: dict[str, "PlayerCrossAppShare.ShareMissionData"]

    class ShareMissionData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        counter: int
