from handin3_project import read_data3
filename = 'Land_and_Ocean_summary.txt'
year_range = (2015, 2018)
temp_anomaly_data = read_data3(filename, year_range)

print(temp_anomaly_data)
