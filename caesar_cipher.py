
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_index_len = len(alphabet) - 1 

ciphered_list = list((input("Input ciphered text here: ")).lower())
deciphered_list = []

offset = 13
past_range_index = offset - 1

for letter in ciphered_list:
    if letter == ' ':
        deciphered_list.append(letter)
    else:
        index = alphabet.index(letter)
        shift_position = index + offset
        if shift_position > alphabet_index_len:
            shift_position = past_range_index - (alphabet_index_len - index)
        # print(shift_position)
        shifted_letter = alphabet[shift_position]
        # print(shifted_letter)
        deciphered_list.append(shifted_letter)
    
deciphered_string = ''.join(deciphered_list)
print(deciphered_string)










