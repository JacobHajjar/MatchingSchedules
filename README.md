# MatchingSchedules
Takes in two peoples' schedules from the command line along with the length of their planned meeting and shows which times they have overlapping availability

## Instructions
With the python interpreter installed and in the directory of matching.py, enter "python3 matching.py" and from the command line pass in a schedule of times where each person is unavailable during the day in the format of a 2D Python List. Then, using a List format, enter the earliest and latest time that each person is available. After that, enter the number of minutes for the planned meeting and the program should display in the command line the list of the available time slots that both people have enough time to meet.

## Sample Input

Just the input for copy pasting:

[[ ‘6:00’, ’8:00’],  [’11:30’, ’13:00’], [’14:30’, ’16:00’], [’16:30’, ’17:30’]]  
[[ ‘7:00’, ’9:00’],  [’11:00’, ’12:30’], [’14:40’, ’16:00’], [’17:00’, ’18:00’ ]]  
[‘9:00’, ’20:00’]  
[‘9:00’, ’18: 30’]  
25  
  
Entire program Input/Output:

Enter schedule for person 1:[[ ‘6:00’, ’8:00’],  [’11:30’, ’13:00’],  [’14:30’, ’16:00’], [’16:30’, ’17:30’]]  
Enter schedule for person 2:[[ ‘7:00’, ’9:00’],  [’11:00’, ’12:30’],  [’14:40’, ’16:00’], [’17:00’, ’18:00’ ]]  
Enter Daily Availability for pers 1: [‘9:00’, ’20:00’]  
Enter Daily Availability for pers 2: [‘9:00’, ’18: 30’]  
Enter duration of the proposed meeting: 25

Output:  
[['9:00', '11:00'], ['13:00', '14:30'], ['16:00', '16:30'], ['18:00', '18:30']]
