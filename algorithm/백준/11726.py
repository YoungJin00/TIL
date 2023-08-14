
"""
## 코드 작성 패턴
1. 빈리스트 만들기 ( 입력값에 따른 )
2. 초기값을 설정
3. 점화식 기반으로 계산값 적용하기
4. 특정 입력값에 따른 계산값을 리스트에서 출력하기
"""
n = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 2

for index in range(3, 1001):
    dp[index] = dp[index - 1] + dp[index -2]

print(dp[n] % 10007)