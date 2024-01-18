import heapq as hp

def solution(scoville, K):
    hp.heapify(scoville)
    cnt = 0
    
    while scoville[0] < K:
        cnt += 1
        
        min1 = hp.heappop(scoville)
        min2 = hp.heappop(scoville)
        hp.heappush(scoville, min1 + min2*2)
        
        if((len(scoville) == 2) and (scoville[0] + scoville[1]*2 < K)):
            return -1
    
    return cnt