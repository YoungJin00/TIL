import requests
from pprint import pprint


def best_review_books():
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

    # pprint(response['item'][0]['customerReviewRank'])
    lst = response['item']
    ls = [] 

    for i in range(len(lst)):
        if lst[i]['customerReviewRank'] >= 9:
            ls.append(lst[i])
    
    return ls
            

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    pprint(best_review_books())
