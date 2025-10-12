from pydantic import BaseModel, ConfigDict


class SandboxMapConstTable(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    directionNames: list[str]
    homeNodeStageId: str
    homeRushStageCode: str
    homeRushStageName: str
    homeRushDesc: str
    crazyRevengeRushGroup: str
    homeBuildModeBGM: str
