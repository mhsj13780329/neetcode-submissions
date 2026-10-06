class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 1
        cars_data = []

        cars_data = list(zip(position, speed))
        cars_data.sort(reverse=True)

        cur_time_ref = (target - cars_data[0][0]) / cars_data[0][1]

        for pos, spd in cars_data[1:]:
            current_car_time = (target - pos) / spd
            if current_car_time > cur_time_ref:
                fleets += 1
                cur_time_ref = current_car_time
        return fleets
