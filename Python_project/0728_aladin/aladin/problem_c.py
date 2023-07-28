import requests
from pprint import pprint


def bestseller_book():
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

    lst = response['item']

    sorted_lst = sorted(lst, key=lambda x: int(x.get('salesPoint', 0)))
    
    top_5_books = sorted_lst[-1:-6:-1]
    top_5_books_title = []
    for i in range(5):
        top_5_books_title.append(top_5_books[i]['title'])


    return top_5_books_title



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    pprint(bestseller_book())

