
long_vowels =  ["ee",  "oo"]

status = True
while status:
    user_prompt = input("Type in a word! ")
    for vowels in long_vowels:
        if vowels in user_prompt:
            if vowels == "ee":
                new_word = user_prompt.replace("ee", "eeeee")
                print(new_word)
                status = False
            else: 
                new_word = user_prompt.replace("oo", "ooooo")
                print(new_word)
                status = False





# if long_vowels[0] in user_prompt:
#     user_prompt.replace(long_vowels[0], "eeeee")
#     print(user_prompt)
# if long_vowels[1] in user_prompt:
#     user_prompt.replace(long_vowels[1], "ooooo")
#     print(user_prompt)





