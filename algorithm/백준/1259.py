# 팰린드 롬수

"""
어떤 단어를 뒤에서 부터 읽어도 똑같다면 팰린드롬이라함
"""

while True:
    num = input()

    reverse_num = num[::-1]
    if num == '0':
        break

    if int(num) == int(reverse_num):
        print("yes")
    else:
        print("no")

