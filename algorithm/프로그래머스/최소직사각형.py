def solution(sizes):
    w = []
    h = []
    for i in range(len(sizes)):        
        if sizes[i][0] >= sizes[i][1]:
            w.append(sizes[i][1])
            h.append(sizes[i][0]) 
            
        else:
            w.append(sizes[i][0])
            h.append(sizes[i][1])       

    return max(h) * max(w)