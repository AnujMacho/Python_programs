def vowel_count(str1):
    str2 = str1.lower()
    print({a:str2.count(a) for a in str2 if a in "aeiou"})

vowel_count('Elie')