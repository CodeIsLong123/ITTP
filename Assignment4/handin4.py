def wordfile_to_list(filename): 
    with open(filename, "r") as file:
        word_list = [line.strip() for line in file]
        return word_list

def wordfile_differences_linear_search(filename1, filename2):
    word_list1 = wordfile_to_list(filename1)
    word_list2 = wordfile_to_list(filename2)
    return [word for word in word_list1 if word not in word_list2]
    
def binary_search(sorted_list, element):
    """Search for element in list using binary search.
       Assumes sorted list"""
    # Current active list runs from index_start up to
    # but not including index_end
    index_start = 0
    index_end = len(sorted_list)
    while (index_end - index_start) > 0:
        index_current = (index_end-index_start)//2 + index_start
        if element == sorted_list[index_current]:
            return True
        elif element < sorted_list[index_current]:
            index_end = index_current
        elif element > sorted_list[index_current]:
            index_start = index_current+1
    return False

def wordfile_differences_binary_search(filename1, filename2):
    word_list1 = wordfile_to_list(filename1)
    word_list2 = sorted(wordfile_to_list(filename2))
    return [word for word in word_list1 if not binary_search(word_list2, word)]


def wordfile_to_dict(filename):
    with open(filename, "r") as file:
        word_dict = {line.strip(): 1 for line in file}
        return word_dict

def wordfile_differences_dict_search(filename1, filename2): 
    word_list1 = wordfile_to_list(filename1)
    word_list2 = wordfile_to_dict(filename2)
    return [word for word in word_list1 if word not in word_list2]
