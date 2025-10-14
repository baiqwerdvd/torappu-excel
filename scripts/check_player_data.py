from pathlib import Path

from torappu_excel import PlayerDataModel

player_data_path = Path("PlayerData.json")
if not player_data_path.exists():
    raise FileNotFoundError("请先保存 PlayerData.json")


_ = PlayerDataModel.model_validate_json(player_data_path.read_text(encoding="utf-8"))
