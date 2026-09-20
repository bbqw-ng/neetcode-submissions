class TimeMap:

    def __init__(self):
        self.hm = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.hm.get(key) == None:
            self.hm[key] = []
        self.hm[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        #no values
        if not self.hm.get(key):
            return ""
        #if there is only 1 value correlated to key
        elif len(self.hm[key]) == 1 and self.hm[key][0][1] == timestamp:
            return self.hm[key][0][0]
        else:
            largest_ts = None
            n = len(self.hm[key])
            left, right = 0, n-1
            while left <= right:
                mid = left + (right - left) // 2
                pair = self.hm[key][mid]
                pair_val = pair[0]
                pair_ts = pair[1]
                if pair_ts == timestamp:
                    return pair_val
                elif pair_ts > timestamp:
                    right = mid - 1
                else:
                    largest_ts = pair
                    left = mid + 1
            if largest_ts:
                return largest_ts[0]
        return ""
        
        
        
        
            
        
