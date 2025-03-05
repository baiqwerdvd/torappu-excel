from .roguelike_item_data import RoguelikeItemData
from .roguelike_recruit_ticket_feature import RoguelikeRecruitTicketFeature
from .roguelike_relic_feature import RoguelikeRelicFeature
from .roguelike_upgrade_ticket_feature import RoguelikeUpgradeTicketFeature
from ..common import BaseStruct


class RoguelikeItemTable(BaseStruct):
    items: dict[str, RoguelikeItemData]
    recruitTickets: dict[str, RoguelikeRecruitTicketFeature]
    upgradeTickets: dict[str, RoguelikeUpgradeTicketFeature]
    relics: dict[str, RoguelikeRelicFeature]
