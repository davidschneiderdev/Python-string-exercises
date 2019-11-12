
paragraph = "Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal."
upper_paragraph = paragraph.upper()
capped_list = list(upper_paragraph)
print(capped_list)

index = 0
while index < len(capped_list):
    if capped_list[index] == "A":
        capped_list[index] = "4"
        index += 1
    elif capped_list[index] == "E":
        capped_list[index] = "3"
        index += 1
    elif capped_list[index] == "G":
        capped_list[index] = "6"
        index += 1
    elif capped_list[index] == "I":
        capped_list[index] = "1" 
        index += 1
    elif capped_list[index] == "O":
        capped_list[index] = "0"
        index += 1
    elif capped_list[index] == "S":
        capped_list[index] = "5"
        index += 1
    elif capped_list[index] == "T":
        capped_list[index] = "7"
        index += 1
    else:
        index += 1

joined_list = ''.join(capped_list)
print(joined_list)





    
