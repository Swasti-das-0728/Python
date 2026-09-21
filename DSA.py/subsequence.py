def is_subsequence(s1,s2):
    i = 0
    j = 0

    while i< len(s1) and j< len(s2):
        if s1[i] == s2[j]:
            i+=1
        j+=1
    return i== len(s1)
s1 = "sw"
s2 = "sweeRTY"
if is_subsequence(s1,s2):
    print("subsequence")
else:
    print("not subsequence")
