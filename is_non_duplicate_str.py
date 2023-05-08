def is_non_duplicated_str(str: str) -> bool:
    """
    Check if a string has all unique characters.
    """
    if len(str) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in str:
        val = ord(char)
        if char_set[val]:
            return False
        char_set[val] = True

    return True


if __name__ == "__main__":
    print(is_non_duplicated_str("abc"))
    print(is_non_duplicated_str("abca"))
