# 진법 변환2
def convert_to_base(N, B):
    # 10진수를 B진법으로 변환하는 함수
    base_digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    
    while N > 0:
        remainder = N % B
        result = base_digits[remainder] + result
        N //= B
    
    return result

# 입력 받기
N, B = map(int, input().split())

# B진법으로 변환하여 결과 출력
print(convert_to_base(N, B))