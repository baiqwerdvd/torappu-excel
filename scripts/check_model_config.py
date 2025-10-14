import logging
import os
import re

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

BASE_DIR = r"src\torappu_excel"

CLASS_PATTERN = re.compile(r"^\s*class\s+\w+\(BaseModel\)\s*:")
CONFIG_LINE = (
    'model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]'
)


def check_file(path: str):
    errors: list[str | tuple[int, str]] = []
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if CLASS_PATTERN.match(line):
            j = i + 1
            while j < len(lines) and lines[j].strip() == "":
                j += 1
            if j >= len(lines):
                errors.append((i + 1, "class后没有内容"))
                continue
            if CONFIG_LINE not in lines[j]:
                errors.append((i + 1, f"缺少正确的 model_config 行 (found: {lines[j].strip()})"))
    return errors


def main():
    total_errors: dict[str, list[str | tuple[int, str]]] = {}
    for root, _, files in os.walk(BASE_DIR):
        for file in files:
            if file == "models.py":
                continue

            if file.endswith(".py"):
                path = os.path.join(root, file)
                errs = check_file(path)
                if errs:
                    total_errors[path] = errs

    if not total_errors:
        logger.info("所有 BaseModel 类均包含正确的 model_config 定义。")
    else:
        logger.warning("检测到以下文件未符合要求: \n")
        for path, errs in total_errors.items():
            logger.warning(f"{path}:")
            for line_no, msg in errs:
                logger.warning(f"  行 {line_no}: {msg}")
            logger.warning("")


if __name__ == "__main__":
    main()
