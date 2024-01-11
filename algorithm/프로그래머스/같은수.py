def solution(array, commands):
    answer = []
    for a in range(len(commands)):
        arr = array[commands[a][0]-1:commands[a][1]]
        arr.sort()
        answer.append(arr[commands[a][2]-1])
    return answer