import re

import requests
from lxml import etree

import importlib
import config

tc_const = importlib.import_module(config.CONSTANTS_MODULE)

def download_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        response = [response.text, True]
    except:
        response = ["<html><head><title>Master OUT OF DATE</title><script src=\"/assets/sort-table.js\"></script><meta http-equiv='refresh' content='600'></head><center><h2>Master OUT OF DATE</h2><h3></h3></center><style>table, td, th {border: 1px solid #aaaaaa;border-collapse: collapse;text-align: left;padding: 6px;font-size: 18px}tr:nth-child(even) {background-color: #dddddd;}tr:nth-child(odd) {background-color: #fff;}</style></head><body><table class=\"js-sort-table\" id=\"dashtable\" style=\"width:100%\"><thead><tr><th class='js-sort-number'>#</th><th>Date</th><th>Product</th><th>Test case ID</th><th>Verdict</th><th>Product IC3X TRs</th><th>Product IC5X TRs</th><th>Product Non-block TRs</th><th>Non-IC Trs</th><th>Dallas TRs</th><th>Other tickets</th><th>Analysis</th><th>Analysis Result</th><th>Scope</th><th>Node type</th><th>Test object</th><th>Branch</th><th>Build</th><th>Build time</th><th>Job</th><th>Job time</th><th>Responsible Team</th><th>Assignee</th><th>TC Name</th></tr></thead><tbody></tbody></table></body></html>", False]
    return response


def process_downloaded_page_from_dashboard(string):
    string = string.replace("\n", "")
    m = re.search('(<table .*?>.+?</table>)', string)
    found = ' '.join(m.group(1).split())
    found = found.replace("<thead>", "").replace("</thead>", "").replace("<tbody>", "").replace("</tbody>", "")
    return found


def parse_table_for_dash(string):
    response = []
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
        response.append([True, dict_list])
    except TypeError:
        response.append([False, []])
    return response


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
