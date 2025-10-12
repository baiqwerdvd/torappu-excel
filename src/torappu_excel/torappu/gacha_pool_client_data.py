from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from .gacha_rule_type import GachaRuleType


class GachaPoolClientData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    CDPrimColor: str | None
    CDSecColor: str | None
    freeBackColor: str | None
    endTime: int
    gachaIndex: int
    gachaPoolDetail: str | None
    gachaPoolId: str
    gachaPoolName: str
    gachaPoolSummary: str
    gachaRuleType: GachaRuleType
    guarantee5Avail: int
    guarantee5Count: int
    guaranteeName: str | None
    LMTGSID: str | None
    openTime: int
    limitParam: dict[str, Any] | None
    dynMeta: dict[str, Any] | None = Field(default=None)
    linkageParam: dict[str, Any] | None = Field(default=None)
    linkageRuleId: str | None = Field(default=None)
