import asyncio
import json
import logging
import os
from pathlib import Path

import aiofiles
import aiohttp
from msgspec import Struct, convert

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ApiFileData(Struct):
    name: str
    path: str
    size: int
    create_at: str
    modified_at: str
    is_dir: bool


class ApiFileStruct(Struct):
    dir: ApiFileData
    children: list[ApiFileData]


class ApiResponse(Struct):
    code: int
    msg: str | None
    data: ApiFileStruct


async def download_file(session: aiohttp.ClientSession, url: str, local_path: Path) -> None:
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            content = await response.read()

            os.makedirs(os.path.dirname(local_path), exist_ok=True)

            async with aiofiles.open(local_path, "wb") as f:
                _ = await f.write(content)

            logger.info(f"已下载: {os.path.basename(local_path)}")
    except Exception as e:
        logger.error(f"下载 {url} 时出错: {e}")


async def get_file_list(api_url: str) -> list[ApiFileData]:
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url) as response:
            response.raise_for_status()
            data = convert(await response.json(), ApiResponse)
            return data.data.children


async def download_torappu_excel() -> None:
    api_url = "https://torappu.prts.wiki/api/v1/files/gamedata/latest/excel"
    base_download_url = "https://torappu.prts.wiki/gamedata/latest/excel/"
    local_dir = Path().parent / "src" / "torappu_excel" / "json"

    try:
        files = await get_file_list(api_url)

        async with aiohttp.ClientSession() as session:
            tasks: list[asyncio.Task[None]] = []
            for file_info in files:
                filename = file_info.name
                download_url = base_download_url + filename

                task = asyncio.create_task(download_file(session, download_url, local_dir / filename))
                tasks.append(task)

            _ = await asyncio.gather(*tasks)

        logger.info("所有文件下载完成")

    except aiohttp.ClientError as e:
        logger.error(f"网络请求错误: {e}")
    except json.JSONDecodeError:
        logger.error("JSON解析错误")
    except Exception as e:
        logger.error(f"发生未知错误: {e}")


def main():
    asyncio.run(download_torappu_excel())


if __name__ == "__main__":
    main()
