class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        class Trie:
            def __init__(self):
                self.root = {}
            
            def insert(self, word):
                cur = self.root
                for c in word:
                    cur = cur.setdefault(c, {}) 
                cur['#'] = True
        
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        res = []
        is_visited = [[False] * len(board[0]) for _ in range(len(board))]
        
        def dfs(r, c, cur_str, cur_trie):
            cur_str += board[r][c]
            pre_trie = cur_trie
            cur_trie = cur_trie[board[r][c]]
            if '#' in cur_trie:
                res.append(cur_str)
                # If the word is found out, we don't need this word in trie anymore
                del cur_trie['#']
                # If there is no possible letters later, we can delete the key to save our time to do useless dfs.
                if not cur_trie.keys():
                    del pre_trie[board[r][c]]
                    return
            
            is_visited[r][c] = True
            for new_r, new_c in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= new_r < len(board) and 0 <= new_c < len(board[0]) and board[new_r][new_c] in cur_trie and not is_visited[new_r][new_c]:
                    dfs(new_r, new_c, cur_str, cur_trie)
            is_visited[r][c] = False
        
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] in trie.root:
                    dfs(r, c, "", trie.root)
        
        return res


# Example 1:
# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]

# Example 2:
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []