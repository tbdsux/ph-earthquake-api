from utils.config import MAIN_URL
from utils.scraper import get_scrape


async def earthquake_latest():
    s = get_scrape()

    tables = s.find_all("table")
    data_table = tables[2]

    drows = data_table.find_all("tr")
    drow_headers = drows[0]
    drow_datas = drows[1:]

    edatas = []

    eheaders = []
    for i in drow_headers.find_all("th"):
        eheaders.append(" ".join([i.strip() for i in i.get_text().strip().split("\n")]))

    eheaders.append("Link")

    for j in drow_datas:
        edata_arr = {}

        for index, k in enumerate(j.find_all("td")):
            edata_arr[eheaders[index]] = k.get_text().strip()

        if j.find("a"):
            edata_arr["Link"] = MAIN_URL + j.find("a")["href"]

        edatas.append(edata_arr)

    return {"headers": eheaders, "data": edatas}
