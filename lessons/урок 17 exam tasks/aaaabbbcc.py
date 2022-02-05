s = 'a'
l = len(s)-1
c = 1
t = ''
if len(s) == 1:
    t = t + s + str(c)
else:
    for i in range(0,l):
        if s[i] == s[i+1]:
            c +=1
        elif s[i] != s[i+1]:
            t = t + s[i] + str(c)
            c = 1
    for j in range(l,l+1):
        if s[-1] == s[-2]:
            t = t + s[j] + str(c)
        elif s[-1] != s[-2]:
            t = t + s[j] + str(c)
            c = 1
print(t)














a = 'aaawwwwqqweqwww'
l = len(a) - 1
c = 1
t = ''
if len(a) == 1:
    t = t + a + str(c)
else:
    for i in range(0,l):
        if a[i] == a[i+1]:
            c += 1
        elif a[i] != a[i+1]:
            t = t + a[i] + str(c)
            c = 1
    for j in range(l,l+1):
        if a[-1] == a[-2]:


