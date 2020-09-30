class Solution():
    def int_to_roman(self, num: int) -> str:
        values = [1000, 900, 500, 400,
                  100, 90, 50, 40,
                  10, 9, 5, 4, 1]
        symbols = ['M', 'CM', 'D', 'CD',
                   'C', 'XC', 'L', 'XL',
                   'X', 'IX', 'V', 'IV', 'I']
        roman = ''
        i = 0
        while num > 0:
            k = num // values[i] # if num is divisible then iterate to reduce the num value
            print(f'i: {i}, k: {k}')

            for j in range(k):
                roman += symbols[i] # add roman value of the numerical value
                num -= values[i] # subtract numerical value already used 
            i += 1
            
        return roman

if __name__ == '__main__':
    s = Solution()
    print(s.int_to_roman(1991))

# STEP 0
# i: 0, k: 1
# roman:  M
# num:  991

# STEP 1
# i: 1, k: 1
# roman:  MCM
# num:  91

# STEP 2
# i: 2, k: 0
# i: 3, k: 0
# i: 4, k: 0
# i: 5, k: 1
# roman:  MCMXC
# num:  1

# STEP 3
# i: 6, k: 0
# i: 7, k: 0
# i: 8, k: 0
# i: 9, k: 0
# i: 10, k: 0
# i: 11, k: 0
# i: 12, k: 1
# roman:  MCMXCI
# num:  0

# FINAL OUTPUT
# MCMXCI