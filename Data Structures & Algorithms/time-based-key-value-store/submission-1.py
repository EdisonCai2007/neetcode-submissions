class TimeMap:
    mapping: dict[str, list[tuple[int, str]]]

    def __init__(self):
        self.mapping = {} # dict[key, list[(timestamp, value)]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapping[key] = self.mapping.get(key, []) + [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        values = self.mapping.get(key) # list[(timestamp, value)]
        if values:
            lp, rp = 0, len(values) - 1

            while lp <= rp:
                mid = (lp + rp) // 2

                if values[mid][0] > timestamp:
                    rp = mid - 1
                elif values[mid][0] < timestamp:
                    lp = mid + 1
                else:
                    return values[mid][1]

            return "" if rp == -1 else values[rp][1]
        else:
            return ""
                


