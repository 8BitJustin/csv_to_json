import csv
import json


def make_json(csv_path, json_path):
    data = {}

    with open(csv_path, encoding='utf-8') as csvp:
        csv_reader = csv.DictReader(csvp)

        for rows in csv_reader:
            key = rows['Year']
            data[key] = rows

    with open(json_path, 'w', encoding='utf-8') as jsonp:
        jsonp.write(json.dumps(data, indent=4))


csv_path = r'elearningtest.csv'
json_path = r'elearningtest_with_keys.json'

make_json(csv_path, json_path)