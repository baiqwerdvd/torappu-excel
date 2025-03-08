from typing import Any

from .gacha_rule_type import GachaRuleType
from ..common import BaseStruct

from msgspec import field


class GachaPoolClientData(BaseStruct):
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
    dynMeta: dict[str, Any] | None = field(default=None)
    linkageParam: dict[str, Any] | None = field(default=None)
    linkageRuleId: str | None = field(default=None)
