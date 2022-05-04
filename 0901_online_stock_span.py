class StockSpanner:

    def __init__(self):
        self.span_list = []

    def next(self, price: int) -> int:
        span = 0
        self.span_list.append(price)
        
        i = len(self.span_list) - 1
        while i >= 0:
            if self.span_list[i] <= price:
                span += 1
            else:
                break
            i -= 1
        
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

# Example 1:

# Input
# ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
# [[], [100], [80], [60], [70], [60], [75], [85]]
# Output
# [null, 1, 1, 1, 2, 1, 4, 6]

# Explanation
# StockSpanner stockSpanner = new StockSpanner();
# stockSpanner.next(100); // return 1
# stockSpanner.next(80);  // return 1
# stockSpanner.next(60);  // return 1
# stockSpanner.next(70);  // return 2
# stockSpanner.next(60);  // return 1
# stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
# stockSpanner.next(85);  // return 6