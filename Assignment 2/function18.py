def count_frequency(input_string):
    frequency = {}   
    for char in input_string:
        if char in frequency:
            frequency[char] += 1  
        else:
            frequency[char] = 1              
    return frequency

input_string = input("Enter any string:")
result = count_frequency(input_string)
print(result)