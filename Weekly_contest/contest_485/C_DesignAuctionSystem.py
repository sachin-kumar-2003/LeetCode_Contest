from heapq import heappush, heappop, heapify
class AuctionSystem:

    def __init__(self):
        self.bids = {}
        self.itembid = defaultdict(list)

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        self.bids[(itemId, userId)] = bidAmount
        heappush(self.itembid[itemId], (-bidAmount, -userId))
        

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        self.bids[(itemId, userId)] = newAmount
        heappush(self.itembid[itemId], (-newAmount, -userId))

    def removeBid(self, userId: int, itemId: int) -> None:
        del self.bids[(itemId, userId)]

    def getHighestBidder(self, itemId: int) -> int:
        heap = self.itembid[itemId]

        while heap:
            bidamount , userid = heap[0]
            bidamount = -bidamount
            userid = -userid
            if(itemId, userid) in self.bids and self.bids[(itemId, userid)] == bidamount:
                return userid
            heappop(heap)
        return -1


# Your AuctionSystem object will be instantiated and called as such:
# obj = AuctionSystem()
# obj.addBid(userId,itemId,bidAmount)
# obj.updateBid(userId,itemId,newAmount)
# obj.removeBid(userId,itemId)
# param_4 = obj.getHighestBidder(itemId)