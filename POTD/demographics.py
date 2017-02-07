
GENDER = 0
AGE = 1
YEAR = 2
MAJOR = 3
STATE = 4
ICE_CREAM = 5
DORM = 6
OS = 7
BIRTH_MONTH = 8


def read_data_file(filename):
    data = []
    datafile = open(filename, 'r')
    for line in datafile:
        entry = line.strip().split(',')
        data.append(entry)
    return data

def get_average_age(student_list):
    data = read_data_file('2015-10-16-data.csv')
    x = -1
    list = []
    while x <= 180:
        x += 1
        list.append(int(data[x][1]))
    return sum(list)/len(list)

def count_by_group(student_list, item_to_count=GENDER, group_by=None, group_by_value=None):
        data = read_data_file('2015-10-16-data.csv')
        my_dict = {}
        for x in data:
            data[x] = my_dict.get(x, 0) + 1
        print(my_dict)





print(read_data_file('2015-10-16-data.csv'))
print(get_average_age('2015-10-16-data.csv'))
count_by_group('2015-10-16-data.csv', AGE)
