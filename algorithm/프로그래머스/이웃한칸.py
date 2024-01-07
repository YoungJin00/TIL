def solution(board, h, w):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    answer = 0
    s = board[h][w]
    for k in range(4):
        ni, nj = h + di[k], w + dj[k]
        if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
            s = board[ni][nj]
            if s == board[h][w]:
                answer += 1
    return answer