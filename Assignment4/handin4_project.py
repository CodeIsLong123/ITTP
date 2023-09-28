class AnomalyData: 
    def __init__(self, filename, year_range=None):
        data_dict = {}
        with open(filename, "r") as file:   
            for line in file:
                cleaned_line = line.rstrip()
                if not cleaned_line or cleaned_line.startswith("%"):
                    continue
                columns = [float(value) for value in cleaned_line.split()]
                year = int(columns[0])
                if year_range is None or (year in range(year_range[0], year_range[1])): 
                    data_dict[year] = columns[1:]      
        self.data = data_dict
            
    def one_value_per_decade(self):
        new_dict = {}
        for year in self.data.keys():
            if year % 10 == 0:
                new_dict[year] = self.data[year]
        return new_dict
