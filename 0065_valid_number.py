class Solution:
    def is_number(self, s: int) -> bool:
        s = s.strip()
        pos, ls = 0, len(s)
        if ls == 0:
            return False
        if s[pos] == '+' or s[pos] == '-':
            pos += 1
        is_numeric = False
        while pos < ls and s[pos].isdigit():
            pos += 1
            is_numeric = True
        if pos < ls and s[pos] == '.':
            pos += 1
            while pos < ls and s[pos].isdigit():
                pos += 1
                is_numeric = True
        if pos < ls and s[pos] == 'e' and is_numeric:
            is_numeric = False
            pos += 1
            if pos < ls and (s[pos] == '+' or s[pos] == '-'):
                pos += 1
            while pos < ls and s[pos].isdigit():
                pos += 1
                is_numeric = True
        if pos == ls and is_numeric:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.is_number('53.5e93'))
    # Output: True

    # "0" => true
    # " 0.1 " => true
    # "abc" => false
    # "1 a" => false
    # "2e10" => true
    # " -90e3   " => true
    # " 1e" => false
    # "e3" => false
    # " 6e-1" => true
    # " 99e2.5 " => false
    # "53.5e93" => true
    # " --6 " => false
    # "-+3" => false
    # "95a54e53" => false