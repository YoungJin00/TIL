import requests
from pprint import pprint


def author_other_works(title):
    # 여기에 코드를 작성합니다.  
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'
    params = {
        'ttbkey': 'ttbdudwlscjswo951411001',
        'Query' : title,
        'QueryType': 'Title',
        'MaxResults' : 20,
        'start' : 1,
        'SearchTarget' : 'Book',
        'output' : 'js',
        'Version' : '20131101'
    }

    response = requests.get(URL, params=params).json()

    lst = response['item']
    first_author = lst[0]['author']
    ls = []

    for i in range(len(lst)):
        if lst[i]['author'] == first_author:
            ls.append(lst[i]['author'])
        
    
    return first_author



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    pprint(author_other_works('베니스의 상인'))

    pprint(author_other_works('개미'))

    # pprint(author_other_works('*'))
