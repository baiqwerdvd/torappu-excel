from src.torappu_excel.constants import ExcelTableManager


async def test_constants():
    excel = ExcelTableManager()
    await excel.preload_table()
