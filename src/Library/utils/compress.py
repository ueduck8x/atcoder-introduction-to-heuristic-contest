from typing import Dict, List


# 座標圧縮
def compress(nums: List[int]) -> Dict[int, int]:
    new_nums = list(set(nums))
    new_nums.sort()
    ans = {origin: new_id for new_id, origin in enumerate(new_nums, 1)}
    return ans
