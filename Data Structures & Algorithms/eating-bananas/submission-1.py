class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calculate_total_time(piles, eat_rate):
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / eat_rate)
            return total_time

        sum = 0
        max = 0
        for pile in piles:
            sum += pile
            if pile > max:
                max = pile
        min_rate = math.ceil(sum / h)

        while True:
            avg = (min_rate + max) // 2
            if avg == 1:
                return 1
            avg_time = calculate_total_time(piles, avg)

            if avg_time > h:
                min_rate = avg + 1
                continue
            else:
                if calculate_total_time(piles, avg - 1) > h:
                    return avg
                else:
                    max = avg - 1
                    continue
