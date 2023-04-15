from collections import defaultdict
from collections import deque

class Solution:
    def __init__(self):
        self.length = 0
        self.all_combo_dict = defaultdict(list)

    def visitWordNode(self, queue, visited, other_visited):
        current_word, level = queue.popleft()
        for i in range(self.length):
            intermediate_word = current_word[:i] + '*' + current_word[i + 1:]
            for word in self.all_combo_dict[intermediate_word]:
                if word in other_visited:
                    return level + other_visited[word]
                if word not in visited:
                    visited[word] = level + 1
                    queue.append((word, level + 1))
        return 0
        
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        self.length = len(beginWord)

        for word in wordList:
            for i in range(self.length):
                self.all_combo_dict[word[:i] + '*' + word[i + 1:]].append(word)
                
        queue_begin = deque([(beginWord, 1)])
        queue_end = deque([(endWord, 1)])
        visited_begin = {
            beginWord: 1
        }
        visited_end = {
            endWord: 1
        }
        while queue_begin and queue_end:
            ans = self.visitWordNode(queue_begin, visited_begin, visited_end)
            if ans:
                return ans
            ans = self.visitWordNode(queue_end, visited_end, visited_begin)
            if ans:
                return ans
        return 0
