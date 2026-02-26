from collections import deque

def is_palindrome(text):
    original_text = text
    text = text.lower().replace(" ","")
    char_deque = deque(text)
    while len(char_deque) > 1:
        left = char_deque.popleft()
        right = char_deque.pop()
        if left != right:
            return f"'{original_text}' is not palindrome"
    return f"'{original_text}' is palindrome"

print(is_palindrome("Was it a car or a cat I saw"))
print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("racecar"))
print(is_palindrome("No lemon no banana"))