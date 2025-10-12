from pydantic import BaseModel, ConfigDict, Field


class SharedCharData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    charId: str
    potentialRank: int
    mainSkillLvl: int
    evolvePhase: int
    level: int
    favorPoint: int
    currentEquip: str | None = Field(default=None)
    equips: dict[str, "SharedCharData.CharEquipInfo"] | None = Field(alias="equip", default={})
    skillIndex: int | None = Field(default=None)
    skinId: str | None = Field(default=None)
    skin: str | None = Field(default=None)
    skills: list["SharedCharData.SharedCharSkillData"] | None = Field(default=None)
    crisisRecord: dict[str, int] | None = Field(default=None)
    crisisV2Record: dict[str, int] | None = Field(default=None)
    currentTmpl: str | None = Field(default=None)
    tmpl: dict[str, "SharedCharData.TmplData"] | None = Field(default=None)

    class CharEquipInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        hide: int
        locked: bool | int
        level: int

    class SharedCharSkillData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        skillId: str
        specializeLevel: int
        completeUpgradeTime: int | None = Field(default=None)
        unlock: bool | int | None = Field(default=None)
        state: int | None = Field(default=None)

    class TmplData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        skinId: str
        defaultSkillIndex: int
        skills: list["SharedCharData.SharedCharSkillData"]
        currentEquip: str | None
        equip: dict[str, "SharedCharData.SharedCharSkillData"] | None = Field(default=None)
