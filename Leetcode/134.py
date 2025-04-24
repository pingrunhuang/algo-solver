class Solution(object):
    """
    Time Limit Exceeded
    """
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        stations = len(gas)
        for i in range(stations):
            result = self.cal_position(i, gas, cost)
            if result!=-1:
                return result
        return -1
    def cal_position(self, start, gas, cost):
        stations = len(gas)
        i = start
        cur_tank = 0
        off_set = 0
        while i!=start or off_set!=stations:
            cur_tank += (gas[i]-cost[i])
            # 注意每次对cur_tank做更新之后就要判断是否满足大于零的要求了，相当于回调
            # 因为cur_tank实际上记录的是到达下一个站点剩下的油量
            if cur_tank<0:
                return -1
            if i==stations-1:
                i=0
            else:
                i+=1
            off_set+=1
        return start

class Solution2(object):
    """
    pointer
    """
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        num_stations = len(gas)
        gain_at_each_station = []

        for i in range(num_stations):
            gain_at_each_station.append(gas[i]-cost[i])
        
        i = 0
        while i < num_stations:
            end = self.canCompleteCircuitWithStart(gain_at_each_station, i)

            if end==i+num_stations:
                return i
            else:
                if i < num_stations:
                    i = end+1
                else:
                    i -= num_stations
        return -1

    def canCompleteCircuitWithStart(self, gain_at_each_station, start):
        """
        :rtype: the end index
        """
        cur = 0
        cur_pointer = start
        num_stations = len(gain_at_each_station)
        gain_at_each_station = 2*gain_at_each_station
        
        while cur_pointer<start+num_stations:
            cur+=gain_at_each_station[cur_pointer]
            if cur<0:
                return cur_pointer
            else:
                cur_pointer+=1
        return cur_pointer



if __name__ == "__main__":
    s = Solution()
    gas  = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    print(s.canCompleteCircuit(gas, cost))
    gas = [3,3,4]
    cost = [3,4,4]
    print(s.canCompleteCircuit(gas, cost))
    gas = [4,5,2,6,5,3]
    cost = [3,2,7,3,2,9]
    print(s.canCompleteCircuit(gas, cost))
    gas = [3,1,1]
    cost = [1,2,2]
    print(s.canCompleteCircuit(gas, cost))
    gas = [5,1,2,3,4]
    cost =[4,4,1,5,1]
    print(s.canCompleteCircuit(gas, cost)) # 4