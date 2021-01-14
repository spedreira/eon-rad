# coding=utf-8


def bad_compression(string):
    s = ''
    i = 0
    if len(string) < 2:
        return string
    else:
        #if string[i] == string [i+1]

        #string.replace(string[i], '', 2)
        while (i < len(string)):  
            if (s and string[i] == s[len(s)-1]):
                s = s[0:-1]
            else:
                s += string[i]
            i += 1

        return s


    #raise NotImplementedError


print(bad_compression("") == "")
print(bad_compression("a") == "a")
print(bad_compression("aba") == "aba")
print(bad_compression("aa") == "")
print(bad_compression("aab") == "b")
print(bad_compression("aaaaa") == "a")
print(bad_compression("aabb") == "")         
print(bad_compression("abba") == "")         
print(bad_compression("abaaba") == "")       
print(bad_compression("aaabccddd") == "abd") 