# Open the files in read mode
with open("Raw_Skills_Dataset.csv", 'r',encoding="utf8") as file1:
    with open("Example_Technical_Skills.csv", 'r', encoding="utf8") as file2:
# The set intersection() method returns a set that contains the similarity between file1 and file2       
        same = set(file1).intersection(file2)
with open('Hard_Skills_Dataset.csv', 'w') as file_out:
    for line in same:
        file_out.write(line)
