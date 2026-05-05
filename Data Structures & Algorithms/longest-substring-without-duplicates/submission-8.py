# Longest Substring Without Repeating Characters -> find the length of the longest
# contiguous sequence of characters in a string with no duplicates
#
# Strategy (Sliding Window + Hashmap):
#   * Create seen = {} mapping character → last seen index
#   * Use two pointers left and right, both starting at 0
#   * right expands the window every iteration
#   * If duplicate found, left jumps to max(left, seen[duplicate] + 1)
#   * Track result = max window size seen so far
#
# Key idea: Instead of checking every possible substring, slide a window forward.
# The hashmap tells you instantly where a duplicate was last seen so left can
# jump directly past it. result = max(result, i - left + 1) keeps the biggest
# window you've ever seen so when you return it, it's the max length.
#
# Tricky edge case: left must never move backwards!
# Example "abba": when right hits second 'a' at index 3, seen[a]=0
# so seen[a]+1=1 but left is already at 2 — moving left back to 1
# would re-include 'b' which is already in the window.
# Fix: left = max(left, seen[s[i]] + 1) ensures left never goes backwards.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}                                    # maps character → last seen index
        left = 0                                     # left pointer, start of current window
        result = 0                                   # tracks max window size seen so far
        for i in range(len(s)):                      # i is the right pointer, moves every iteration
            if s[i] in seen:                         # duplicate found in current window
                left = max(left, seen[s[i]] + 1)     # jump left past duplicate — max() prevents left from moving backwards
            seen[s[i]] = i                           # always update to latest index of this character
            result = max(result, i - left + 1)       # i - left + 1 is current window size, keep the biggest

        return result                                # max length found


# Patterns to recognize sliding window problems:
#   * "longest/shortest substring/subarray" with some condition
#   * "no repeating characters", "at most k distinct", "sum equals target"
#   * Any problem where you need a contiguous sequence and brute force is O(n²)
#
# Sliding window always has:
#   * left and right pointer both starting at 0
#   * right expands every step
#   * left shrinks only when condition is violated
#   * result tracked with max() or min() every step
#
# When to use hashmap with sliding window:
#   * You need to know WHERE something was last seen → map char to index
#   * You need to COUNT occurrences in window → map char to count
#
# Common mistakes in sliding window:
#   * Putting result update inside the if block — it must update every iteration
#   * Not using max(left, ...) when moving left — left must never go backwards
#   * Updating seen inside the if block only — always update seen every iteration
