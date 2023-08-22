with open("one_test.txt", "r") as input_file:

    current_value=0
    total_list =[]

    for line in input_file:
        stripped = line.strip()
        if stripped != "": 
            current_value=current_value+int(stripped)
        else:
            total_list.append(current_value)
            current_value=0
 

sort_total_list = sorted(total_list,reverse=True) 
top_three= sort_total_list[:3]
print(top_three)
top_three_total=0
for number in top_three:
    top_three_total+=number
print(top_three_total)
          

