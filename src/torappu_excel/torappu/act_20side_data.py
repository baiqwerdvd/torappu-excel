from pydantic import BaseModel, ConfigDict


class Act20SideData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    zoneAdditionDataMap: dict[str, str]
    residentCartDatas: dict[str, "Act20SideData.ResidentCartData"]

    class ResidentCartData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        residentPic: str
