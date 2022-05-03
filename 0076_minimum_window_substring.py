from collections import Counter

class Solution:
    
    def minWindow(self, s: str, t: str) -> str:
        min = size = len(s)
        result = ''
        t_count = Counter(t)
        for i in range(size):
            l = r = i

            while l > 0:
                count = Counter(s[l:i+1])
                match = True
                for val in t:
                    if count[val] < t_count[val]:
                      match = False
                      break
                if match:
                    if len(s[l:i+1]) <= min:
                        min = len(s[l:i+1])
                        result = s[l:i+1]
                l -= 1

            while r < size:
                count = Counter(s[i:r+1])
                match = True
                for val in t:
                    if count[val] < t_count[val]:
                      match = False
                      break
                if match:
                    if len(s[i:r+1]) <= min:
                        min = len(s[i:r+1])
                        result = s[i:r+1]
                r += 1

        return result


s = "qdsvbyuipqxnhkbgqdgozelvapgcainsofnrfjzvawihgmpwpwnqcylcnufqcsiqzwhhhjchfmqmagkrexigytklnrdslmkniuurdwzikrwlxhcbgkjegwsvnvpzhamrwgjzekjobizbreexqqewmwubtjadlowhwhiarurvcsyvwcunsylgwhisrivezrmvzwwsqppuhnreqmtkkgrjozbhjwlkpzgqwejotylamcgeqzobihmwinduloecqmtoqcejcpmqusukulncsbabodxbtbeloxzgbesdveupyocuzryutyxjdulzvpklokspqkslqodqfhlgajatkxfntqorhzcxlwmdigoyxtrcccidnlyxidnevdveczbpwpugyjhveyxhcfkpqipboehjhcombrdzhyghjncnnzwpggezrvcfzjqjngvoyyqhwwohlsvarrpzavatrcasnqbazyrzxhivfydsqasjtjiteloxposdhtfgswhrfpomnteftyonjyiojxnznfeubjctijmnyaanwgsphieqhpgsoutbbxycjaxrklekogakpsbwdimkxvelpyosvmxgnuxzgejwmjgbehxhpmtohzbyxqsvepbrmzsufcqrnwttfscxgxlpxnpufirjxtdjuvfzzvqprlizelwmkjchwtcdbvpbosminsjpncehnmgtzegknkrmdvrhrgihywsoobdedhltvtmxzuhmeaakysrpybyzxqnouqszzfswahtzbanidoubilsgoqfnjubdmvclaxkaedbfeppj"
t = "fjknwevk"

Solution().minWindow(s, t)


# 225 / 266 test cases passed.
# Time LImit Exceeded
# Output eventually would be: 'fzzvqprlizelwmkjchwtcdbvpbosminsjpncehnmgtzegk'


# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
    
# Example 2:
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
    
# Example 3:
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.