"""
You are given a dictionary of words and a large input string. You have to find out whether the input string can be completely segmented into the words of a given dictionary. The following two examples elaborate on the problem further.
"""

def can_segment_string(s, dictionary):
    for i in range(1, len(s)+1):
        if s[0:i] in dictionary:
            first_str_point = i
            if s[first_str_point:] in dictionary:
                return True
    return False


if __name__ == "__main__":
    dictionary_words: list[str] = ["apple", "apple", "pear", "pie"]
    input_string1: str =  "applepie"
    input_string2: str =  "applepeer"
    print(can_segment_string(input_string1, dictionary_words))
    print(can_segment_string(input_string2, dictionary_words))
