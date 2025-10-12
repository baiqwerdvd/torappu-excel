from pydantic import BaseModel, ConfigDict, Field

from .blackboard import Blackboard
from .buildable_type import BuildableType, BuildableTypeStr
from .height_type_mask import HeightTypeMask
from .profession_category import ProfessionCategory
from .side_type import SideType


class RuneData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    key: str
    selector: "RuneData.Selector"
    blackboard: list[Blackboard]

    class Selector(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        professionMask: ProfessionCategory | int
        buildableMask: BuildableTypeStr | BuildableType
        heightTypeMask: HeightTypeMask | int | None = Field(default=None)
        sideType: SideType | None = Field(default=None)
        playerSideMask: BuildableTypeStr | BuildableType | None = Field(default=None)
        charIdFilter: list[str] | None = Field(default=None)
        enemyIdFilter: list[str] | None = Field(default=None)
        enemyIdExcludeFilter: list[str] | None = Field(default=None)
        enemyLevelTypeFilter: list[str] | None = Field(default=None)
        enemyActionHiddenGroupFilter: list[str] | None = Field(default=None)
        skillIdFilter: list[str] | None = Field(default=None)
        tileKeyFilter: list[str] | None = Field(default=None)
        groupTagFilter: list[str] | None = Field(default=None)
        filterTagFilter: list[str] | None = Field(default=None)
        filterTagExcludeFilter: list[str] | None = Field(default=None)
        subProfessionExcludeFilter: list[str] | None = Field(default=None)
        mapTagFilter: list[str] | None = Field(default=None)
