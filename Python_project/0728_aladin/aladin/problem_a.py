import requests
from pprint import pprint
import json



def author_works():
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'
    params = {
        'ttbkey': '',
        'Query' : '파울로 코엘료',
        'QueryType': 'Author',
        'MaxResults' : 20,
        'start' : 1,
        'SearchTarget' : 'Book',
        'output' : 'js',
        'Version' : '20131101'
    }

    response = requests.get(URL, params=params).json()
    # pprint(response['item'])
    lst = response['item']
    ls = []
    for i in lst:
        ls.append((i['title']))
        
    return ls

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    print(author_works())

    