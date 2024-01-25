import bisect
from typing import List
from collections import namedtuple


RangeSpec = namedtuple('RangeSpec', ['min', 'max'])


def conflict_range(item_ranges: List[RangeSpec]):
    sorted_items = []

    for item in item_ranges:
        if not sorted_items:
            sorted_items.append(item.min)
            sorted_items.append(item.max)
            continue

        mix_index = bisect.bisect(sorted_items, item.min)
        max_index = bisect.bisect(sorted_items, item.max)

        if mix_index % 2 == 0 and item.max in sorted_items:
            max_index -= 1

        if mix_index == max_index and mix_index % 2 == 0:
            sorted_items.insert(max_index, item.max)
            sorted_items.insert(mix_index, item.min)
        else:
            raise RuntimeError(f"conflict {item}")


if __name__ == "__main__":
    conflict_range([RangeSpec(3, 8), RangeSpec(1, 3), RangeSpec(8, 9)])
