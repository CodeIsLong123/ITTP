import re 

def read_word_file(filename):
    word_list = []
    for i, line in enumerate(open(filename)):
        word_list.append((i, line.rstrip()))
    return word_list
        
def read_word_file2(filename, filter_re_str=""):
    word_list = []
    for i, line in enumerate(open(filename)):
        if re.search(filter_re_str, line):
            word_list.append((i, line.rstrip()))
    return word_list
