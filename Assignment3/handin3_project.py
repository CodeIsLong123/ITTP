def read_data2(filename, year_range=None):
    data_list = []
    with open(filename, "r") as file:
        for line in file:
            cleaned_line = line.strip()
            if not cleaned_line or cleaned_line.startswith("%"):
                continue
            data_list.append(line)
        if year_range is not None:
            year_range = [int(i) for i in year_range]
            data_list = [line for line in data_list if int(line.split()[0]) 
                         in range(year_range[0], year_range[1])]
            return data_list
        return data_list

def read_data3(filename, year_range=None):
    data_dict = {}
    with open(filename, "r") as file:   
        for line in file:
            cleaned_line = line.rstrip()
            if not cleaned_line or cleaned_line.startswith("%"):
                continue
            # Assuming the columns are separated by spaces or tabs
            columns = [float(value) for value in cleaned_line.split()]
            year = int(columns[0])
            # Check if the year is within the specified range
            if year_range is None or (year in range(year_range[0], year_range[1])): 
                data_dict[year] = columns[1:]        
        return data_dict
