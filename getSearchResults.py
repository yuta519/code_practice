# Complete the 'getSearchResults' function below.
#
# The function is expected to return a 2D_STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY words
#  2. STRING_ARRAY queries
#
# Given 2 arrays words and queries for each query, retun array of the strings that are anagrams of the strings tahat are anagrams, sorted  alphabetically ascending order.
# Example
#  words = ["duel", "speed", "dule", "cars"]
#  queries = ["spede", "deul"]
# output = [["speed"], ["dule", "duel"]]
# please write python code


def getSearchResults(words, queries):
    # Write your code here
    result = []
    for query in queries:
        temp = []
        for word in words:
            if sorted(word) == sorted(query):
                temp.append(word)
        result.append(temp)
    return result


def get_anagrams(words, queries):
    # Create a dictionary to store the sorted letters of each word in 'words'
    word_dict = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word in word_dict:
            word_dict[sorted_word].append(word)
        else:
            word_dict[sorted_word] = [word]

    # Create a list of anagrams for each query
    results = []
    for query in queries:
        sorted_query = "".join(sorted(query))
        if sorted_query in word_dict:
            results.append(sorted(word_dict[sorted_query]))
        else:
            results.append([])

    return results


if __name__ == "__main__":
    # words = ["duel", "speed", "dule", "cars"]
    words = ["allot", "cat", "act", "peach", "peahc", "dusty"]
    queries = ["tac", "study", "cheap"]
    print(get_anagrams(words, queries))
