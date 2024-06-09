#My solution
def duplicate_count(text):
    char_count = {}
    
    text = text.lower()
    
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    counter = sum(1 for count in char_count.values() if count > 1)
    
    return counter
     
print(duplicate_count("abcdeaa"))