from collections import deque
import sys

N = int(sys.stdin.readline())
deck = deque([])
for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push_back':
        deck.append(command[1])

    elif command[0] == 'push_front':
        deck.appendleft(command[1])

    elif command[0] == 'front':
        if deck:
            print(deck[0])
        else:
            print(-1)

    elif command[0] == 'back':
        if deck:
            print(deck[-1])
        else:
            print(-1)

    elif command[0] == 'size':
        print(len(deck))

    elif command[0] == 'empty':
        if len(deck) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == 'pop_front':
        if deck:
            m = deck.popleft()
            print(m)
        else:
            print(-1)

    elif command[0] == 'pop_back':
        if deck:
            m = deck.pop()
            print(m)
        else:
            print(-1)

