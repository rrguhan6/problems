# https://leetcode.com/problems/keyboard-row/


def findWords(words):
    keyboard = [
        set('qwertyuiop'),
        set('asdfghjkl'),
        set('zxcvbnm')
    ]

    ans = []

    for w in words:
        for row in keyboard:
            if set(w.lower()).issubset(row):
                ans.append(w)

    return ans


print(findWords(["Hello", "Alaska", "Dad", "Peace"]))
