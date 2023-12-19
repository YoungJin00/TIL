def profit_list(l):
    p_lst = []
    for row in range(N):
        diff = prices[row][l+1] - prices[row][l]
        p_lst.append([diff, prices[row][l]])
    p_lst.sort(key=lambda x: (-x[0], x[1]))
    return p_lst


def stock_count(stock_price, now_wallet):
    count = 0
    while now_wallet >= stock_price:
        now_wallet -= stock_price
        count += 1
    return  count


for t in range(1, int(input())+1):
    Ms, Ma = map(int, input().split())
    N, L = map(int, input().split())
    prices = [list(map(int, input().split())) for _ in range(N)]
    capital = Ms + Ma*L

    wallet = Ms
    for i in range(L):
        lst = profit_list(i)
        profits = []
        for profit, price in lst:
            if price < wallet and profit > 0:
                cnt = stock_count(price, wallet)
                wallet -= price*cnt
                profits.append((profit+price)*cnt)
        wallet += sum(profits) + Ma

    print(f'#{t}', wallet - capital)