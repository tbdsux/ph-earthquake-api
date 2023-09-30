from fastapi import APIRouter, Response, status
from api.functions.parser import table_parser, special_2017
from api.utils.config import MONTHLY_DATA_URL
import calendar

from api.utils.scraper import get_scrape


def earthquake_data(year: int, month: int):
    """
    Get and parse the data from a specific year and month.
    """
    month_str = calendar.month_name[month]
    url = f"{MONTHLY_DATA_URL}/{year}/{year}_{month_str}.html"

    [ok, s] = get_scrape(url)
    if not ok:
        return {"message": f"No data from {month_str}, {year} yet."}

    tables = s.find_all("table")

    use_td_head = False
    if year == 2017 or year == 2018:
        use_td_head = True

    if year == 2017 and month < 6:
        return special_2017(tables)

    data_table = tables[2]
    if year == 2017 and month == 12:
        data_table = tables[1]

    parsed_data = table_parser(data_table, except_first_td=True, td_is_head=use_td_head)
    return parsed_data


# setup router
router = APIRouter(
    prefix="/data",
    tags=["data"],
    responses={422: {"message": "Required some parameters, `month` and `year`"}},
)


@router.get("/{year}/{month}")
async def get_data(year: int, month: int, res: Response):
    if month < 0 or month > 12:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": "Invalid month"}

    if year < 2016:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": "Invalid year"}

    return earthquake_data(year, month)
