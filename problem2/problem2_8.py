def problem2_8(temp_list):
    sum_of_temp = 0
    min_temp = None
    max_temp = None
    
    for hour_temp in temp_list:
        sum_of_temp += hour_temp
        if max_temp is None or max_temp < hour_temp:
            max_temp = hour_temp
        if min_temp is None or min_temp > hour_temp:
            min_temp = hour_temp
    avg_temp = sum_of_temp / len(temp_list)
    print("Average:", avg_temp)
    print("High:", max_temp)
    print("Low:", min_temp)