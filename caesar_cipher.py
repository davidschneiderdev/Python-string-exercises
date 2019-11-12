
import string

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_index_len = len(alphabet) - 1 
# print(alphabet)
ciphered_list = list((input("Input ciphered text here: ")).lower())
# print(ciphered_text)
offset = 13
past_range_offset = offset - 1

deciphered_list = []

for letter in ciphered_list:
    # print(letter)
    if letter == ' ':
        deciphered_list.append(letter)
    else:
        index = alphabet.index(letter)
        # print(index)
        shift_position = index + offset
        if shift_position > alphabet_index_len:
            shift_position = past_range_offset - (alphabet_index_len - index)
        # print(shift_position)
        shifted_letter = alphabet[shift_position]
        # print(shifted_letter)
        deciphered_list.append(shifted_letter)
    
deciphered_string = ''.join(deciphered_list)
print(deciphered_string)










