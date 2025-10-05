class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Problem Description:
        - Merge characters alternatively

        Time Complexity: O(n)
        Space Complexity: O(1)

        Args:
            word1: First word
            word2: Second word

        Returns:
            String containing merged characters.
        """
        merged = list()
        word1_list = list(word1)
        word2_list = list(word2)

        for l1, l2 in zip(word1, word2):
            merged.extend([l1, l2])
            word1_list.pop(0)
            word2_list.pop(0)

        return ''.join(merged) + ''.join(word1_list) + ''.join(word2_list)

def test_solution():
    solution = Solution()
    assert solution.mergeAlternately('abc','def') == 'adbecf'

if __name__ == '__main__':
    test_solution()
