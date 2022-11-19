class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        units  = dict()
        
        for item in boxTypes:
            if item[1] not in units:
                units[item[1]] = item[0]
            else:
                units[item[1]] = units[item[1]] + item[0]
        loaded = 0
        print(sorted(units, reverse= True))
        for key in sorted(units, reverse= True):
            if truckSize == 0:
                return loaded
            loaded += min(units[key], truckSize) * key
            truckSize = truckSize - min(units[key], truckSize)
        return loaded
            
        