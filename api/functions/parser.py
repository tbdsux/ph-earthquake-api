from api.utils.config import MAIN_URL
from urllib.parse import urljoin


def special_2017(tables):
    """
    Special parser for year 2017 because of its weird table structure which was separated from the other table.
    """

    data_headers_table = tables[2]
    data_table = tables[3]

    drow_datas = data_table.find_all("tr")[1:]

    eheaders = table_header_parser(data_headers_table.find("tr"), "td")
    edatas = table_contents_parser(drow_datas, eheaders)

    return {"headers": eheaders, "data": edatas}


def table_parser(table, except_first_td=False, td_is_head=False):
    """
    Main data table parser.
    """
    drows = table.find_all("tr")
    drow_headers = drows[0]
    drow_datas = []
    if except_first_td:
        drow_datas = drows[2:]
    else:
        drow_datas = drows[1:]

    edatas = []

    # table header data keys
    head_key = "th"
    if td_is_head:
        head_key = "td"

    eheaders = table_header_parser(drow_headers, head_key)
    edatas = table_contents_parser(drow_datas, eheaders)

    return {"headers": eheaders, "data": edatas}


def table_header_parser(table_row, header_key="th"):
    eheaders = []
    for i in table_row.find_all(header_key):
        eheaders.append(" ".join([i.strip() for i in i.get_text().strip().split("\n")]))

    eheaders.append("Link")

    return eheaders


def table_contents_parser(table_rows, table_headers):
    edatas = []
    for j in table_rows:
        edata_arr = {}

        for index, k in enumerate(j.find_all("td")):
            edata_arr[table_headers[index]] = k.get_text().strip()

        if j.find("a"):
            edata_arr["Link"] = urljoin(
                MAIN_URL, j.find("a")["href"].replace("..", "").replace("\\", "/")
            )

        edatas.append(edata_arr)

    return edatas
