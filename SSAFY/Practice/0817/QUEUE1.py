def enQ(data):
    global rear

    rear += 1
    Q[rear] = data


def deQ():
    global front
    # if front == rear: # 비어있으면
    #     print('큐가 비어있음')
    front += 1
    return Q[front]

Qsize =3
Q = [0] * Qsize
rear = front = -1

enQ(1)
enQ(2)
rear += 1
Q[rear] = 3

# print(deQ())
# print(deQ())
# print(deQ())

while front != rear:
    front += 1
    print(Q[front])