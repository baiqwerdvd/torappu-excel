from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class ActSandboxData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    milestoneDataList: list["ActSandboxData.MilestoneData"]
    milestoneTokenId: str

    class MilestoneData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        milestoneId: str
        orderId: int
        tokenId: str
        tokenNum: int
        item: ItemBundle
        isPrecious: bool
