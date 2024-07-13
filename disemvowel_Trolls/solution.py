vowel_list = ['a','e','i','o','u','A','E','I','O','U']
def disemvowel(string_):
    new_string = string_
    for letter in vowel_list:
        new_string = new_string.replace(letter,"")
    return new_string