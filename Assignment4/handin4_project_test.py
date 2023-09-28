from handin4_project import AnomalyData

# Test the AnomalyData class
## Task 1 
anomaly_data = AnomalyData('Land_and_Ocean_summary.txt')
value = anomaly_data.data[1990][0]

## Task 2
decade_dict = anomaly_data.one_value_per_decade()
