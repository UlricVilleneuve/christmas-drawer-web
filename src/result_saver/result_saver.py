import requests
import xmltojson
import json

if __name__ == '__main__':
    print('Saving results')
    with open('input/tokens.txt') as tokens_file:
        tokens_file_lines = tokens_file.read().splitlines()
        for token_line in tokens_file_lines:
            participant_name, token = token_line.split(':')
            http_res = requests.get(f'http://127.0.0.1:5000/token/{token}')
            json_res = xmltojson.parse(http_res.text)
            res = json.loads(json_res)
            with open(f'output/{participant_name}.txt', "x") as result_file:
                result_file.write(res["div"]["p"][0])
                result_file.write('\n')
                result_file.write(res["div"]["p"][1])
