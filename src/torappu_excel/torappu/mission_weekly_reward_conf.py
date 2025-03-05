from .mission_periodic_reward_conf import MissionPeriodicRewardConf


class MissionWeeklyRewardConf(MissionPeriodicRewardConf):
    beginTime: int
    endTime: int
