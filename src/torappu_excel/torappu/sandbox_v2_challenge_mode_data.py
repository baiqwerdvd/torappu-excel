from pydantic import BaseModel, ConfigDict

from .sandbox_v2_challenge_const import SandboxV2ChallengeConst
from .sandbox_v2_challenge_mode_difficulty_data import SandboxV2ChallengeModeDifficultyData
from .sandbox_v2_challenge_mode_reward_data import SandboxV2ChallengeModeRewardData
from .sandbox_v2_challenge_mode_unlock_data import SandboxV2ChallengeModeUnlockData


class SandboxV2ChallengeModeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    challengeConst: SandboxV2ChallengeConst
    challengeModeUnlockData: dict[str, SandboxV2ChallengeModeUnlockData]
    challengeModeRewardData: dict[str, SandboxV2ChallengeModeRewardData]
    challengeModeDifficultyData: list[SandboxV2ChallengeModeDifficultyData]
