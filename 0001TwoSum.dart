class Solution {
  var _nums_index;
  var _target;
  Solution(this._nums_index, this._target);

  (int, int) twoSum() {
    var size = this._nums_index.length;
    List<(int, int)> nums = [(0, 0)];
    for (var i=0; i<size; i++){
      nums.add((i, this._nums_index[i]));
    }
    nums.removeAt(0);

    nums.sort((a, b) => (a.$2).compareTo(b.$2));
    var begin = 0;
    var end = size - 1;

    while (begin < end) {
      var curr = nums[begin].$2 + nums[end].$2; 

      if (curr == this._target) {
        return (nums[begin].$1, nums[end].$1);
      } else if (curr > this._target) {
        end = end - 1;
      } else {
        begin = begin + 1;
      }
    }

    return (0, 0);
  }
}

void main() {
  var s = Solution([3, 2, 4], 6).twoSum();
  print(s);
}
