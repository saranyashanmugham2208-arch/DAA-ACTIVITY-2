from collections import Counter

def min_window(s, t):
    if not s or not t:
        return ""

    required = Counter(t)
    window = {}

    have = 0
    need = len(required)

    left = 0
    min_length = float("inf")
    min_start = 0

    for right in range(len(s)):
        ch = s[right]
        window[ch] = window.get(ch, 0) + 1

        if ch in required and window[ch] == required[ch]:
            have += 1

        while have == need:
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_start = left

            left_char = s[left]
            window[left_char] -= 1

            if (left_char in required and
                    window[left_char] < required[left_char]):
                have -= 1

            left += 1

    if min_length == float("inf"):
        return ""

    return s[min_start:min_start + min_length]


s = input("Enter string: ")
t = input("Enter target string: ")

result = min_window(s, t)

if result:
    print("Minimum Window Substring:", result)
else:
    print("No valid window found")
