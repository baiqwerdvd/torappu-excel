from pydantic import BaseModel, ConfigDict


class ObscuredRect(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    m_xMin: float
    m_yMin: float
    m_width: float
    m_height: float
