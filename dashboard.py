import re

import requests
from lxml import etree

import importlib
import config

tc_const = importlib.import_module(config.CONSTANTS_MODULE)

def download_page(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def process_downloaded_page_from_dashboard(string):
    string = string.replace("\n", "")
    m = re.search('(<table .*?>.+?</table>)', string)
    found = ' '.join(m.group(1).split())
    found = found.replace("<thead>", "").replace("</thead>", "").replace("<tbody>", "").replace("</tbody>", "")
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
        if item['Test case ID'] in tc_const.TCS.keys():
            result.append([item['Test case ID'], item['Verdict'], tc_const.TCS[item['Test case ID']]["owner"]])
    return result


def merge_tables(ood, todo, global_text):
    result = []
    for tc in tc_const.TCS.keys():
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
        result.append([tc_const.TCS[tc]["owner"], tc, todo_value, ood_value])
    if global_text != "":
        result = list(filter(lambda x: x[0] == global_text, result))
    return sorted(result, key=lambda x: x[0])
