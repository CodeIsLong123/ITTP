data_list = []
# Read the file and populate data_list
def read_data(filename):
    data_list.clear()
    with open(filename, "r") as file:
        for line in file:
            cleaned_line = line.strip( )
            if not cleaned_line or cleaned_line.startswith("%"):
                continue
            data_list.append(line)
        return data_list


data_list_returned = read_data("Land_and_Ocean_summary.txt")

