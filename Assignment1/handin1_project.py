'''
part 2
'''

list_of_lines = []
with open("Land_and_Ocean_summary.txt", "r") as file:
    for line in file:
        list_of_lines.append(line)


for line in list_of_lines:
    cleaned_line = line.strip()
    if not cleaned_line or cleaned_line.startswith("%"):
        continue
    

    split_lines = cleaned_line.split()

    year = int(split_lines[0])
    
    if year >= 2000:
        print(year)



        
        
    