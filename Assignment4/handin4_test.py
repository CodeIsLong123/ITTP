import handin4 
import timeit 

## Task 1
start_time = timeit.default_timer()
wordlist_british = handin4.wordfile_to_list("british-english")
wordlist_american = handin4.wordfile_to_list("american-english")
time_spent = timeit.default_timer() - start_time
print("Time spent on wordfile_to_list: {:.2f} seconds".format(time_spent))

## Task 2 - Linear Search 

start_time = timeit.default_timer()
differences_linear_search = handin4.wordfile_differences_linear_search("british-english", "american-english")
time_spent = timeit.default_timer() - start_time
print("Time spent on linear_search: {:.2f} seconds".format(time_spent))

## Task 3 - Binary Search

start_time = timeit.default_timer()
differences_binary_search = handin4.wordfile_differences_binary_search("british-english", "american-english")
time_spent = timeit.default_timer() - start_time
print("Time spent on binary_search: {:.2f} seconds".format(time_spent))

## Task 4 - Dictionary Search
worddict_american = handin4.wordfile_to_dict("american-english")

start_time = timeit.default_timer()
differences_dict_search = handin4.wordfile_differences_dict_search("british-english", "american-english")
time_spent = timeit.default_timer() - start_time
print("Time spent on dict_search: {:.2f} seconds".format(time_spent))
