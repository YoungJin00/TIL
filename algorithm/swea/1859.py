# 백만장자 프로젝트
# 테스트 케이스 먼저 받아오기
T = int(input())

# 테스트 케이스로 받아온 T 값 만큼 반복문 돌리기
for tc in range(1, T+1):
  # 며칠 받을지 값 n 정하기
  n = int(input())
  # 가격 리스트로 값 받기
  li = list(map(int, input().split()))
  # 최대 값 미리 변수 정하기
  # 구글링 후 마지막날을 최대값으로 정하고
  # 역순으로 리스트 값을 찾는 방법이 있음
  max_price = li[n-1]
  # 이익 변수 할당
  money = 0

  # 역순으로 마지막 전전 값부터 값을 찾기
  # n-2 부터 0 까지
  for i in range(n-2, -1, -1):
    # max_price 값 보다 리스트에 속해있는 값이 클경우
    # 최대값 변경해주기
      if li[i] > max_price:
          max_price = li[i]
    # 그게 아니면 이익에 값 넣어주기
      else:
          money += max_price - li[i]

  print(f"#{tc} {money}")


'''
처음 고민하면서 짯던 코드 임
이렇게 첫날 기준으로 되었음
그래서 구글링의 도움을 받고 역순으로 하는 방법이 있었음
거의 다짯으나 매우 아쉬웠음
for tc in range(1, T+1):
  # 며칠 받을지 값 n 정하기
  n = int(input())
  # 가격 리스트로 값 받기
  li = list(map(int, input().split()))
  # 최대 값 미리 변수 정하기
  max_price = li[0]
  # 이익 변수 할당
  money = 0

  for i in range(1, n):
    # max_price 값 보다 리스트에 속해있는 값이 클경우
    # 최대값 변경해주기
      if li[i] > max_price:
          max_price = li[i]
    # 그게 아니면 이익에 값 넣어주기
      else:
          money += max_price - li[i]

  print(f"#{tc} {money}")
'''
