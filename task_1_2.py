from os import path
from collections import Counter
import requests


log_file_url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'

index_ip = 0
index_method = 5
index_url = 6
i = 0
m = []
def main(log_file_name):
    if not path.exists(log_file_name):
        download_log_file(log_file_name)

    log_analysis_data = log_file_analysis(log_file_name)
    log_data_string = [log_tuple for log_tuple in log_analysis_data]
    print(log_data_string)
    log_analysis_data = log_file_analysis(log_file_name)
    spammers_ip_addresses = Counter(ip_address[index_ip] for ip_address in log_analysis_data)
    print(spammers_ip_addresses)




def log_file_analysis(log_file_name):
    with open(log_file_name, 'r', encoding='utf-8') as file:
        for log_string in file:
            splitting_a_string = log_string.split()
            ip, method, url = (
                splitting_a_string[index_ip],
                splitting_a_string[index_method],
                splitting_a_string[index_url]
            )
            method = method.strip('\'\"')
            yield ip, method, url


def download_log_file(log_file_name):
    response = requests.get(log_file_url, stream=True)
    with open(log_file_name, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            file.write(chunk)


if __name__ == '__main__':
    log_file_name = 'nginx_logs.txt'
    main(log_file_name)