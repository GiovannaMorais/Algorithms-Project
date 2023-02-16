def is_palindrome_iterative(word):
    length = len(word)
    mid = length // 2
    for i in range(mid):
        if word[i] != word[length - i - 1]:
            return False
    return True if length > 0 else False
