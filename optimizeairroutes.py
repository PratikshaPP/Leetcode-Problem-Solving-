

class Solution(object):

    def optimizeAirRoutes(self, maxTravelDist, forwardRouteList, returnRouteList):

        result = []

        max = float('-inf')
        returnRouteList.sort(key = lambda x: x[1])
        for i in range(len(forwardRouteList)):
            route = []
            target = maxTravelDist - forwardRouteList[i][1]
            index = self.binarySearch(returnRouteList, target)
            if index != -1:
                sum = forwardRouteList[i][1] + returnRouteList[index][1]
                if sum >= max:
                    if sum > max:
                        route = []
                    max = sum
                    route.append(i)
                    route.append(index)
                    result.append(route)
            

        return result
                    

    def binarySearch(self, returnRouteList, target):

        low = 0
        high = len(returnRouteList) - 1

        while low<=high:

            mid = low+(high-low)//2

            if returnRouteList[mid][1] == target:
                return mid
            elif returnRouteList[mid][1] > target:
                high = mid-1
            else:
                low = mid+1

        return high

maxTravelDist = 7000
forwardRouteList = [[1,4000],[2,2000],[3,6000]]
returnRouteList = [[1,4000],[2,2500],[3,2800]]
print(Solution().optimizeAirRoutes(maxTravelDist, forwardRouteList , returnRouteList))