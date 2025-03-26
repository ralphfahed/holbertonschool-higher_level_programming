#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []  # Create an empty list to store the results

    for i in range(list_length):  # Iterate through the range of list_length
        try:
            # Attempt to divide the elements of both lists
            result.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)  # If division by zero, append 0
        except (TypeError, ValueError):
            print("wrong type")
            result.append(0)  # If wrong type, append 0
        except IndexError:
            print("out of range")
            result.append(0)  # If the index is out of range, append 0

    return result  # Return the list of division results
