from csv2json import convert, load_csv, save_json

with open('test2.csv') as r, open('test2.json', 'w') as w:
    convert(r, w)