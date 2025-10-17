from msgspec import field

from .blackboard import Blackboard
from .buildable_type import BuildableType, BuildableTypeStr
from .height_type_mask import HeightTypeMask
from .profession_category import ProfessionCategory
from .side_type import SideType
from ..common import BaseStruct


class RuneData(BaseStruct):
    key: str
    selector: "RuneData.Selector"
    blackboard: list[Blackboard]

    class Selector(BaseStruct):
        professionMask: ProfessionCategory | int
        buildableMask: BuildableTypeStr | BuildableType
        heightTypeMask: HeightTypeMask | int | None = field(default=None)
        sideType: SideType | None = field(default=None)
        playerSideMask: BuildableTypeStr | BuildableType | None = field(default=None)
        charIdFilter: list[str] | None = field(default=None)
        enemyIdFilter: list[str] | None = field(default=None)
        enemyIdExcludeFilter: list[str] | None = field(default=None)
        enemyLevelTypeFilter: list[str] | None = field(default=None)
        enemyActionHiddenGroupFilter: list[str] | None = field(default=None)
        skillIdFilter: list[str] | None = field(default=None)
        tileKeyFilter: list[str] | None = field(default=None)
        groupTagFilter: list[str] | None = field(default=None)
        filterTagFilter: list[str] | None = field(default=None)
        filterTagExcludeFilter: list[str] | None = field(default=None)
        subProfessionExcludeFilter: list[str] | None = field(default=None)
        mapTagFilter: list[str] | None = field(default=None)
