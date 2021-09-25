#!/usr/bin/env python3
import sys
import ast
''' matching takes a person's schedule and finds the availabilities with another person's schedule'''

__author__ = 'Jacob Hajjar'
__email__ = 'hajjarj@csu.fullerton.edu'
__maintainer__ = 'jacobhajjar'

def groupschedule (pers1Schedule, pers1DailyAct, pers2Schedule, pers2DailyAct,duration ):

    updatedSchedule1 = updateSchedule(pers1Schedule, pers1DailyAct)
    updatedSchedule2 = updateSchedule(pers2Schedule, pers2DailyAct)
    mergedSchedule=mergedSchedules(updatedSchedule1, updatedSchedule2)
    sortedSchedules= sortedAllSchedules(mergedSchedule)
    print ( matchedAvailabilities(sortedSchedules,duration))

def updateSchedule(Schedule, DailyAct):
    updatedSchedule = Schedule[:]  #make a copy of the schedule
    convertedDailyAct = DailyAct[:]

    updatedSchedule = convert_to_data(updatedSchedule)
    convertedDailyAct = convert_to_data(convertedDailyAct)
    
    updatedSchedule.insert(0, ['0:00', convertedDailyAct[0]])  #update unavailable schedules and add early morning hours
    updatedSchedule.append([convertedDailyAct[1], '23:59'])   #update unavailable schedules and add after work hours
    return updatedSchedule
    #return list(map(lambda s: [convertToMinutes(s[0]), convertToMinutes(s[1])], updatedSchedule))

def convert_to_data(schedule_string):
    schedule = schedule_string[:]
    schedule = schedule.replace('‘','\'')
    schedule = schedule.replace('’','\'')  
    schedule = ast.literal_eval(schedule)
    return schedule

def mergedSchedules(pers1Schedule, pers2Schedule):
    merged =[[0,0]]
    i,j =0,0

    pers1ScheduleMinutes = convertListToMinutes(pers1Schedule)
    pers2ScheduleMinutes = convertListToMinutes(pers2Schedule)

    while i < len(pers1ScheduleMinutes) and j< len(pers2ScheduleMinutes):
        meeting1, meeting2 =pers1ScheduleMinutes[i], pers2ScheduleMinutes[j]
        if meeting1[0]<= meeting2[0]:
            if meeting1[1] > merged[-1][1]:
                merged.append(meeting1)
            i+=1
        else:
            if meeting2[1] > merged[-1][1]:
                merged.append(meeting2)
            j+=1
    while i< len(pers1ScheduleMinutes):
        meeting1 = pers1ScheduleMinutes[i]
        if meeting1[1] > merged[-1][1]:
            merged.append(meeting1)
        i+=1
    while j< len(pers2ScheduleMinutes):
        meeting2 = pers2ScheduleMinutes[j]
        if meeting2[1] > merged[-1][1]:
            merged.append(meeting2)
        j+=1
    return merged

def sortedAllSchedules (Schedule):
    '''finds all of the possible availabilities in the schedules'''
    #for plan in allSchedules:

    #Todo: write a function to  arrange all schedules. New meeting starts AFTER the end of current meeting.
    possibleAvailabilities = []
    index = 0
    while index < (len(Schedule) - 1):
        if Schedule[index][1] < Schedule[index + 1][0]:
            possibleAvailabilities.append([Schedule[index][1], Schedule[index + 1][0]])
            index+=1
        else:
            index+=1
    return possibleAvailabilities



    
def matchedAvailabilities(Schedule, duration):
    availabilities=[]
   #Todo: write a function to match all availabilities
    for possible_availability in Schedule:
        if possible_availability[1] - possible_availability[0] >= int(duration):
            availabilities.append(possible_availability)

    availabilities_reconverted =  []
    for plan in availabilities:
        hoursPlan = []
        for bound in plan:
            hoursPlan.append(convertMinutestoHour(bound))
        availabilities_reconverted.append(hoursPlan)

    return availabilities_reconverted

def convertToMinutes(time):
    hours, minutes = list(map(int, time.split(":")))
    return hours * 60 + minutes

def convertListToMinutes(schedule_list):
    '''converts a 2d list of a time schedule into minutes'''
    scheduleMinutes = [] 
    for plan in schedule_list:
        minutesPlan = []
        for bound in plan:
            minutesPlan.append(convertToMinutes(bound))
        scheduleMinutes.append(minutesPlan)
    return scheduleMinutes

def convertMinutestoHour(minutes):
    hours = minutes // 60
    mins = minutes% 60
    toString = str(hours)
    toStringMins = "0" + str(mins) if mins< 10 else str(mins)
    return toString +":" + toStringMins

def main():
    pers1Schedule = input("Enter schedule for person 1:")
    pers2Schedule = input("Enter schedule for person 2:")
    pers1DailyAct = input("Enter Daily Availability for pers 1: ")
    pers2DailyAct = input("Enter Daily Availability for pers 2: ")
    duration = input("Enter duration of the proposed meeting: ")
    groupSchedule1 = groupschedule(pers1Schedule, pers1DailyAct, pers2Schedule, pers2DailyAct,duration )

if __name__ == '__main__':
    main()

