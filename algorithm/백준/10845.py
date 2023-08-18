# '''
# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# '''
from collections import deque
import sys

N = int(sys.stdin.readline())
lst = deque()

for i in range(N):
    com = sys.stdin.readline().split()
    if com[0] == 'push':
        lst.append(int(com[1]))
    elif com[0] == 'pop':
        if not lst:
            print(-1)
        else:
            m = lst.popleft()
            print(m)

    elif com[0] == 'front':
        if not lst:
            print(-1)
        else:
            print(lst[0])

    elif com[0] == 'back':
        if not lst:
            print(-1)
        else:
            print(lst[-1])

    elif com[0] == 'size':
        print(len(lst))

    elif com[0] == 'empty':
        if lst:
            print(0)
        else:
            print(1)
