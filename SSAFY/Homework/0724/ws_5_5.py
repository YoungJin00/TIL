def even_elements(input):
    # 빈 리스트를 생성하여 짝수를 담을 준비
    res = []

    index = 0
    for _ in range(len(input)):
      if input[index] % 2 == 0:
        res.append(input.pop(index))
      else:
        index += 1

    return res

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = even_elements(my_list)

print(result)
