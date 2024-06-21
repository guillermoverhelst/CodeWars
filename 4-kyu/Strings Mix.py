#First solution
import re
def mix(s1, s2):
    s1 = s1.replace(" ","")
    s2 = s2.replace(" ","")
    dic_s1 = {}
    dic_s2 = {}
    result = []
    s1 = re.sub(r'[^a-z ]', "", s1)
    s2 = re.sub(r'[^a-z ]', "", s2)
    for i in s1:
        if i in dic_s1:
            dic_s1[i] += 1
        else:
            dic_s1[i] = 1

    for i in s2:        
        if i in dic_s2:
            dic_s2[i] += 1
        else:
            dic_s2[i] = 1

    dic_s1 = {i:j for i,j in dic_s1.items() if j > 1}
    dic_s2 = {i:j for i,j in dic_s2.items() if j > 1}
    keys = dic_s1.keys() | dic_s2.keys()
    combined_keys = sorted(keys, key=len)
    for i in combined_keys:
        if i not in dic_s1:
            result.append("2:"+i*dic_s2[i]+"/")
        elif i not in dic_s2:
            result.append("1:"+i*dic_s1[i]+"/")
        else:
            if dic_s1[i] > dic_s2[i]:
                result.append("1:"+i*dic_s1[i]+"/")
            elif dic_s1[i] < dic_s2[i]:
                result.append("2:"+i*dic_s2[i]+"/")
            else:
                result.append("=:"+i*dic_s1[i]+"/")

    

    result.sort(key=lambda x:(-len(x),x))
    
    return "".join(result)[:-1]

s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"
print(mix(s1,s2))

#Better solution
def mix(s1, s2):
    hist = {}
    for ch in "abcdefghijklmnopqrstuvwxyz":
        val1, val2 = s1.count(ch), s2.count(ch)
        if max(val1, val2) > 1:
            which = "1" if val1 > val2 else "2" if val2 > val1 else "="
            hist[ch] = (-max(val1, val2), which + ":" + ch * max(val1, val2))
    return "/".join(hist[ch][1] for ch in sorted(hist, key=lambda x: hist[x]))