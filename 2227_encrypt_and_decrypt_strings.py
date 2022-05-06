import typing as List

class Solution:
    def encode(self, strs: List) -> str:
        return ':;'.join(strs)

    def decode(self, str: str) -> List:
        return str.split(':;')


# Example1
# Input: ['lint','code','love','you']
# Output: ['lint','code','love','you']
# Explanation:
# One possible encode method is: 'lint:;code:;love:;you'

# Example2
# Input: ['we', 'say', ':', 'yes']
# Output: ['we', 'say', ':', 'yes']
# Explanation:
# One possible encode method is: 'we:;say:;:::;yes'