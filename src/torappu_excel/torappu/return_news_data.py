from .return_news_type import ReturnNewsType
from ..common import BaseStruct


class ReturnNewsData(BaseStruct):
    groupId: str
    sortId: int
    tabTitle: str
    tabIcon: str
    title: str
    desc: str
    imgId: str
    iconId: str
    jumpType: ReturnNewsType
    jumpPlace: str
