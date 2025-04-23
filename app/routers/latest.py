from fastapi import APIRouter

from app.functions.parser import table_parser
from app.utils.config import MAIN_URL
from app.utils.scraper import get_scrape


def earthquake_latest():
    """
    Get and parse the latest earthquake data.
    """
    res = get_scrape(MAIN_URL)
    if not res[0]:
        return res[1]

    tables = res[1].find_all("table")
    data_table = tables[2]

    parsed_data = table_parser(data_table)
    return parsed_data


# setup router
router = APIRouter(
    prefix="/latest", tags=["latest"], responses={404: {"message": "Not Found"}}
)


@router.get("/")
async def get_latest():
    return earthquake_latest()
