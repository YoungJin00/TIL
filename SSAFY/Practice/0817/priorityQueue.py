from queue import PriorityQueue

# q = PriorityQueue()
q = PriorityQueue(maxsize=8)

# 추가
q.put(1)
q.put(2)
q.put(3)
q.put(4)

print(q.get())
print(q.get())
print(q.get())
print(q.get())


q.put((1, '윤태우'))
q.put((2, '황호철'))
q.put((3, '원종현'))
q.put((0, '허범성'))

print(q.get()[1])
print(q.get())
print(q.get())
print(q.get())