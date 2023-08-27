# DICT = {
#     'S': 13,
#     'D': 13,
#     'H': 13,
#     'C': 13
# }

T = int(input())
for tc in range(1, T+1):
    cards = input()
    card_set = set()

    S,D,H,C = 13,13,13,13
    for i in range(len(cards) // 3):
        card_set.add(cards[i*3:i*3+3])
        if cards[i*3] == 'S':
            S -= 1
        elif cards[i*3] == 'D':
            D -= 1
        elif cards[i*3] == 'H':
            H -= 1
        elif cards[i*3] == 'C':
            C -= 1
    if len(card_set) != 4:
        print(f'#{tc} ERROR')
    else:
        print(f'#{tc} {S} {D} {H} {C}')

# T = int(input())
# for tc in range(1, T+1):
#     cards = input()
#     card_set = set()
#
#     card_count = {
#         'S': 13,
#         'D': 13,
#         'H': 13,
#         'C': 13
#     }
#
#     for i in range(len(cards) // 3):
#         card = cards[i*3]
#         card_set.add(cards[i*3:i*3+3])
#         card_count[card] -= 1
#
#     if len(card_set) != 4:
#         print(f'#{tc} ERROR')
#     else:
#         print(f'#{tc} {card_count["S"]} {card_count["D"]} {card_count["H"]} {card_count["C"]}')



