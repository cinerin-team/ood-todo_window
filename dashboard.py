import re

import requests
from lxml import etree

from config import TCS


def download_page(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def process_downloaded_page_from_dashboard(string):
    string = string.replace("\n", "")
    m = re.search('(<table .*?>.+?</table>)', string)
    try:
        found = ' '.join(m.group(1).split())
        found = found.replace("<thead>", "").replace("</thead>", "").replace("<tbody>", "").replace("</tbody>", "")
    except AttributeError:
        found = '<html><head><title>Master OUT OF DATE</title><script src="/assets/sort-table.js"></script><meta http-equiv=\'refresh\' content=\'600\'></head><center><h2>Master OUT OF DATE</h2><h3></h3></center><style>table, td, th {  border: 1px solid #aaaaaa;  border-collapse: collapse;  text-align: left;  padding: 6px;  font-size: 18px}tr:nth-child(even) {  background-color: #dddddd;}tr:nth-child(odd) {  background-color: #fff;}</style></head><body>    </body></html>'
    return found


def parse_table_for_dash(string):
    dict_list = []
    dict_list.clear()
    table = etree.HTML(process_downloaded_page_from_dashboard(string)).find("body/table")
    try:
        rows = iter(table)
        headers = [col.text for col in next(rows)]
        for row in rows:
            values = [col.text for col in row]
            one_line = dict(zip(headers, values))
            clean_line = {k: v.strip() for k, v in one_line.items()}
            dict_list.append(clean_line)
    except TypeError:
        pass
    return dict_list


def collect_team_tc_state(string):
    result = []
    for item in string:
        if item['Test case ID'] in TCS.keys():
            result.append([item['Test case ID'], item['Verdict'], TCS[item['Test case ID']]["owner"]])
    return result


def merge_tables(ood, todo, global_text):
    result = []
    for tc in TCS.keys():
        ood_value = False
        if ood:
            for item in ood:
                if item[0] == tc:
                    ood_value = True
                    break
        todo_value = False
        if todo:
            for item in todo:
                if item[0] == tc:
                    todo_value = True
                    break
        result.append([TCS[tc]["owner"], tc, todo_value, ood_value])
    if global_text != "":
        result = list(filter(lambda x: x[0] == global_text, result))
    return sorted(result, key=lambda x: x[0])
