class Solution:
    def length_of_longest_substring(self, s: str) -> int:

        char_map = {}

        # Set char_map for all unicode characters that represent the ASCII table
        for i in range(256):
            char_map[i] = -1
        ls = len(s)
        i = max_len = 0

        # Iterate over the input characters
        # ord is converting the character back to the number representing the index
        for j in range(ls):

            # Note that when char_map[ord(s[j])] >= i, it means that there is a duplicate
            # character in current i, j iteration. Need to set i in order to compute j - i later
            if char_map[ord(s[j])] >= i:
                i = char_map[ord(s[j])] + 1

            # Set the char_map with the input character as you iterate over it
            char_map[ord(s[j])] = j

            # Find the longest substring without repeating characters
            # compared to longest max to longest substring less duplicate characters
            max_len = max(max_len, j - i + 1)

        return max_len

if __name__ == '__main__':
    s = Solution()
    print(s.length_of_longest_substring('abcdefghijj'))
    # Output: 10