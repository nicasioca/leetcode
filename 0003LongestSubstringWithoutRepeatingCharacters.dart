import 'dart:math';

class Solution {
   var _str;
   Solution(this._str);

   int lengthOfLongestSubstring() {
    var left = 0;
    var longest = 0;
    var used = {};
    var size = this._str.length;
    for (var i = 0; i < size; i++){
      var right = i;
      var c = this._str[i];
      if (used.containsKey(c) && left <= used[c]){
        left = used[c] + 1;
      } else {
        longest = max(longest, right - left + 1);
      }
      used[c] = right;
    }
    return longest;
   }
}

void main() {
  var s = Solution('abcdefghijj').lengthOfLongestSubstring();
  print(s);
}