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


def number_of_rooms(array):
    start_times = []
    end_times = []

    for times in array:
        start_times.append(times[0])
        end_times.append(times[1])

    start_times.sort()
    end_times.sort()

    rooms = 0
    start_index = 0
    end_index = 0

    while start_index < len(start_times):
        if start_times[start_index] < end_times[end_index]:
            rooms += 1
        else:
            end_index += 1    
        start_index += 1

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

