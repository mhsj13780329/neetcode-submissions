class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 1
        cars_data = []
        for i in range(len(position)):
            car_data = [position[i], speed[i]]
            cars_data.append(car_data)

        cars_data.sort(key=lambda x: x[0], reverse=True)
        times = []
        for i in range(len(cars_data)):
            times.append((target - cars_data[i][0]) / cars_data[i][1])

        cur_time_ref = times[0]
        for i in range(1, len(times)):
            if times[i] > cur_time_ref:
                fleets += 1
                cur_time_ref = times[i]

        return fleets