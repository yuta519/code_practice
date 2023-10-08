def has_duplicate_char(char: str) -> bool:
    char_list = sorted(list(char))

    for i in range(len(char_list) - 1):
        if char_list[i] == char_list[i + 1]:
            return True
    return False


print(has_duplicate_char("stringify"))
print(has_duplicate_char("abcdef"))
