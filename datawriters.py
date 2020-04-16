import json

def write_json(dict, filename):
    with open(filename, 'a', encoding='utf8') as jsonfile:
        json.dump(dict, jsonfile , ensure_ascii=False)
        jsonfile.write('\n')

def write_txt(data, filename):

    with open(filename, 'a') as filetxt:
        filetxt.write(data)
        filetxt.write('\n')
        filetxt.close()