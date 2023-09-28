import handin3


word_list = handin3.read_word_file("british-english")

filter_re_str = r"^py[a-zA-Z]{4}$"

filtered_word_list = handin3.read_word_file2("british-english", filter_re_str)
