from api.functions.parser import table_parser
from api.utils.config import MAIN_URL
from api.utils.scraper import get_scrape
from fastapi import APIRouter


def earthquake_latest():
    """
    Get and parse the latest earthquake data.
    """
    s = get_scrape(MAIN_URL)

    tables = s.find_all("table")
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
