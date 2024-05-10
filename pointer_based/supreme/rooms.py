# Meeting Room II


# Given an array of meeting time intervals consisting of start and end times 
# [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms 
# required. 

# Example 1: 

# Input: [[0, 30],[5, 10],[15, 20]] 
# Output: 2 

# Example 2: 

# Input: [[7,10],[2,4]] 
# Output: 1


"""
Need a SORTED array that contains all start times
Need a SORTED array that contains all end times

[0, 5], [1, 3], [2, 6], [4, 7], [5, 9], [8, 10]
start_times = [0, 1, 2, 4, 5, 8]
end_times = [3, 5, 6, 7, 9, 10]

[1,15], [3,15], [5,20], [11,20]
start_times = [1, 3, 5, 11]
end_times = [15, 15, 20, 20]
rooms = 4

[1,3], [5,7], [9,11], [15,17]
start_times = [1,5,9,15]
end_times = [3,7,11,17]

[1,7], [5,30], [8,11]
start

start pointer is incremented every time
    add one room if end pointer is greater than the start pointer
else
    end pointer is incremented
"""


def number_of_rooms(array):
    start_times = []
    end_times = []

    for meeting in array:
        start_times.append(meeting[0])
        end_times.append(meeting[1])
    
    start_times.sort()
    end_times.sort()
    
    rooms = 0
    start_time_pointer = 0
    end_time_pointer = 0

    while start_time_pointer < len(array):
        if end_times[end_time_pointer] > start_times[start_time_pointer]:
            rooms += 1
        else:
            end_time_pointer += 1

        start_time_pointer += 1

    return rooms

# Test cases
print(number_of_rooms([[0, 30], [5, 10], [15, 20]]) == 2)                   
print(number_of_rooms([[7, 10], [2, 4]]) == 1)                               
print(number_of_rooms([[1, 2], [3, 4], [5, 6]]) == 1)                         
print(number_of_rooms([[1, 4], [2, 5], [3, 6]]) == 3)               
print(number_of_rooms([[1, 3], [3, 6], [6, 8]]) == 1)                          
print(number_of_rooms([[1, 10]]) == 1)                                        
print(number_of_rooms([[1, 3], [2, 4], [4, 6]]) == 2)                          
print(number_of_rooms([[1, 5], [2, 3], [4, 6], [5, 7]]) == 2)                
print(number_of_rooms([[0, 5], [1, 3], [2, 6], [4, 7], [5, 9], [8, 10]]) == 3) 
print(number_of_rooms([[1, 2], [2, 3], [3, 4], [4, 5]]) == 1)            
print(number_of_rooms([[1, 20], [5, 10], [11, 15], [16, 18]]) == 2)         
print(number_of_rooms([[1, 4], [1, 3], [1, 2], [1, 5]]) == 4) 

