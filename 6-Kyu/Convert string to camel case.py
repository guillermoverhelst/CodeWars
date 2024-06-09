import re
#First solution
def to_camel_case(text):
    temp_text = text
    final_text = ""
    for i in range(len(text)):
        if text[i] == '_' or text[i] == '-':
            text = text.replace(text[i+1],text[i+1].upper())
        else:    
            final_text += text[i]
            text = temp_text
    return final_text

print(to_camel_case("the_cat-is_kawaii"))

#Solution using re
def to_camel_case2(text):
    final_text = re.sub(r"[-_](\w)", lambda x: x.group(1).upper(), text)
    return final_text

print(to_camel_case2("the_cat-is_kawaii"))
