sortedList = []
marksList = []
# lists

name = input('Name of student: ')

count1 = 0
while count1 != 10:
    marksList.append(int(input('Mark: ')))
    count1 = count1 + 1
# marks are put into a list

totalMark = 0
count2 = 0
average = 0
for mark in marksList:
    totalMark = totalMark + mark
    count2 = count2 + 1
    average = totalMark/count2
# get the average

count3 = 1
while count3 <= 3:
    high_value = marksList[0]
    low_value = marksList[0]
    for marks in marksList:
        if high_value < marks:
            high_value = marks
        if low_value > marks:
            low_value = marks
    marksList.pop(marksList.index(high_value))
    marksList.pop(marksList.index(low_value))
    sortedList.append(high_value)
    sortedList.append(low_value)
    count3 = count3+1
# gets the three highest marks and the three lowest marks and appends them to sortedList

print(name + ':')
print('Average mark is', average)
print('Highest marks were', sortedList[0], sortedList[2], sortedList[4],
      'and then lowest marks were', sortedList[5], sortedList[3], sortedList[1])
# prints the information
