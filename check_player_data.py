import asyncio
from collections.abc import Awaitable, Callable
import json
import logging
from pathlib import Path
from statistics import mean, stdev
import time

from src.torappu_excel import PlayerDataModel

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


def measure_sync(func: Callable[[], None], repeat: int = 5, label: str = "") -> None:
    durations: list[float] = []
    for _ in range(repeat):
        start = time.perf_counter()
        func()
        durations.append((time.perf_counter() - start) * 1000)

    avg_ms = mean(durations)
    logger.info(f"{label} {repeat} 次平均耗时: {avg_ms:.2f} ms, 波动: ±{stdev(durations):.2f} ms")


async def measure_async(func: Callable[[], Awaitable[None]], repeat: int = 5, label: str = "") -> None:
    durations: list[float] = []
    for _ in range(repeat):
        start = time.perf_counter()
        await func()
        durations.append((time.perf_counter() - start) * 1000)

    avg_ms = mean(durations)
    logger.info(f"{label} {repeat} 次平均耗时: {avg_ms:.2f} ms, 波动: ±{stdev(durations):.2f} ms")


async def main() -> None:
    player_data_path = Path("PlayerData.json")
    json_text = player_data_path.read_text(encoding="utf-8")
    data = json.loads(json_text)

    def load_data():
        _ = PlayerDataModel.convert(data)

    measure_sync(load_data, repeat=1000, label="模型加载")

    data = PlayerDataModel.convert(data)

    def dump_data():
        _ = data.model_dump()

    measure_sync(dump_data, repeat=1000, label="模型序列化")


if __name__ == "__main__":
    asyncio.run(main())
