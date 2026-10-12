import csv

'''
o	Add teacher
o	View teacher details
o	Search teacher
'''

def teacher_management(csv_path:str):
    with open(csv_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        no_of_entries = list(reader)[-1][0]

    def add_teacher(name:str, Class:int, section:str, number:int):
        with open(csv_path, 'a', newline='') as csv_file1:
            writer = csv.writer(csv_file1)

            writer.writerow([no_of_entries, name, Class, section, number])

    def view_teacher(id_no:int):
        with open(csv_path, 'r') as csv_file2:
            reader2 = csv.reader(csv_file2)
            retrieved = None
            reader_list = list(reader2)
            columns = reader_list[0]
            columns[0] = 'Roll No'

            for row in reader_list:
                if row and row[0] == str(id_no):
                    retrieved = list(row)
                    break

            dictionary = {}

            if retrieved:
                for i in range(len(columns)):
                    dictionary[columns[i]] = retrieved[i]

            print("Found Record:", dictionary)

    def search_teacher(name:str):
        with open(csv_path, 'r') as csv_file2:
            reader2 = csv.reader(csv_file2)
            retrieved = []
            reader_list = list(reader2)
            columns = reader_list[0]
            columns[0] = 'Id Number' # Random Characters Error

            for row in reader_list:
                if row and row[1] == str(name):
                    retrieved.append(int(list(row)[0]))

            print(f"Found Records({len(retrieved)}):\n\t", end='')
            dictionary = {}
            for x in retrieved:
                for i in range(len(columns)):
                    dictionary[columns[i]] = reader_list[x][i]

                print(dictionary, end="\n\t")