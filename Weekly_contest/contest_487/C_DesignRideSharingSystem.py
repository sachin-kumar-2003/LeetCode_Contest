from typing import List
from collections import deque
class RideSharingSystem:

    def __init__(self):
        self.riders = deque()
        self.drivers = deque()
        self.a_riders = set()

    def addRider(self, riderId: int) -> None:
        self.riders.append(riderId) 
        self.a_riders.add(riderId)

    def addDriver(self, driverId: int) -> None:
        self.drivers.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        while self.riders and self.riders[0] not in self.a_riders:
            self.riders.popleft()
        if len(self.riders) >= 1 and len(self.drivers) >= 1:
            first_rider = self.riders.popleft()
            first_driver = self.drivers.popleft()
            self.a_riders.remove(first_rider)
            return [first_driver, first_rider]
        return [-1, -1]

    def cancelRider(self, riderId: int) -> None:
        self.a_riders.discard(riderId)
        


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)