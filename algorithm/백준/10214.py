# 10214 baseball

t = int(input())
yon = []
ko = []

for tc in range(t):
  for i in range(9):
    a = list(map(int, input().split()))
    yon.append(a[0])
    ko.append(a[1])

  if sum(yon) > sum(ko):
    print("Yonsei")
  elif sum(yon) < sum(ko):
    print("Korea")
  else:
    print("Draw")


