class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        shift = 0
        l = len(arr)
        for i in range(l):
            if arr[i] == 0:
                shift += 1
        for i in range(l-1, -1, -1):
            # put the shifted number in the right spot
            if i + shift < l:
                arr[i+shift] = arr[i]
            # if we meet a 0, we need to duplicate 0
            if arr[i] == 0:
                shift -= 1
                if i + shift < l:
                    arr[i+shift] = 0
