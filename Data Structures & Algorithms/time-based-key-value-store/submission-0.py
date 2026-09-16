class TimeMap:

    def __init__(self):
        self.mapp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mapp:
            self.mapp[key] = []

        self.mapp[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mapp:
            return ""

        values = self.mapp[key]

        left = 0
        right = len(values) - 1
        result = ""

        while left <= right:
            middle = (left + right) // 2

            mid_timestamp = values[middle][0]

            if mid_timestamp <= timestamp:
                result = values[middle][1]
                left = middle + 1
            else:
                right = middle - 1

        return result