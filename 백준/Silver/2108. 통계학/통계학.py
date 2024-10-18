import sys
import statistics
from collections import Counter

input = sys.stdin.readline

n = int(input())
nums = list(map(int, sys.stdin.read().splitlines()))
nums.sort()

sys.stdout.write(str(round(statistics.mean(nums)))+'\n')

sys.stdout.write(str(statistics.median(nums))+'\n')

mode_ = Counter(nums).most_common(2)
if len(mode_) > 1:
    if mode_[0][1] == mode_[1][1]:
        sys.stdout.write(str(mode_[1][0]) + '\n')
    else:
        sys.stdout.write(str(mode_[0][0]) + '\n')
else:
    sys.stdout.write(str(mode_[0][0])+'\n')

range_ = 0
if nums[0] < 0 < nums[-1]:
    range_ = abs(nums[0]) + nums[-1]
elif nums[0] < nums[-1] < 0:
    range_ = abs(nums[0] - nums[-1])
else:
    range_ = nums[-1] - nums[0]
sys.stdout.write(str(range_)+'\n')