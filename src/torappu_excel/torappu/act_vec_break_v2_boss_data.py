from pydantic import BaseModel, ConfigDict


class ActVecBreakV2BossData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    enemyId: str
    name: str
    desc: str | None
    level: int
    iconId: str
    levelDecoFigureId: str | None
    levelDecoSignId: str | None
    decoId: str | None
