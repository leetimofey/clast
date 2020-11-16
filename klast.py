def printpic(n):
    pic=[]
    for j in range(32):
        pic.append(start[n][j*32:(j+1)*32])
    for j in range(len(pic)):
        #print(*pic[j])
        for z in range(len(pic[j])):
            if pic[j][z]==1:
                print("þ", end=' ')
           # if pic[j][z]==2:
            #    print("#", end=' ')
            #if pic[j][z]==3:
            #    print("+", end=' ')
            if pic[j][z]==0:
                print(" ", end=' ')
            #if pic[j][z]==4:
             #   print("-", end=' ')                
            if z==31:
                print()
a=[]
with open('hash.csv', 'r') as f:
    for line in f:
        line=line[:-1]
        b=list(map(int, line.split(',')))
        a.append(b)
start=[]
for i in range(len(a)):
    start.append(a[i])
c = []
final=[]
    
#ãÖó¦ ¨Ò Ò ãã·ë ãÖãå ëÖë ÆÐ ãå¨áÖë
result=[]
for i in range(len(a)):
    result.append([i+1])
#ãÖó¦ ¨Ò Ò åá·¤ç á ããåÖÞÔ·½
for i in range(len(a)):
    for j in range(len(a)):
        sum=0
        for k in range(len(a[i])):
            sum+=((a[i][k]-a[j][k])**2)
        sum=(sum**(1/2))
        c.append(sum)
        if len(c)==len(a):
            final.append(c)
            c=[]
        
'''for i in range(len(final)):
    print(*final[i])'''
    
    
print("ìë¨¦·å¨ ÆÖÐ·û¨ãåëÖ ÆÐ ãå¨áÖë:")
kolvo=int(input())

print("äØ·ãÖÆ Ò ãã·ëÖë:")
print()
print()
for i in range(len(start)):
    print(i+1, start[i])
    #printpic(i)
    
min=1000
str=0
slb=0
sredn=[]

while (len(final))!=kolvo:#ØÖÆ  ÆÐ ãå¨áÖë ¢ÖÐíõ¨ û¨Ò Ô ¦Ö
    for i in range(len(final)):
        for j in range(len(final)):
            if i!=j and final[i][j]<min:#Ô µÖ¦·Ò Ò·Ô·Ò ÐíÔÖ¨ á ããåÖÞÔ·¨
                min=final[i][j]
                str=i
                slb=j
    for i in range(len(a[str])):
        sredn.append((a[str][i]*len(result[str])+a[slb][i])*len(result[slb])/(len(result[str])+len(result[slb])))#Ø¨á¨ãû·åñë ¨Ò Þ¦áÖ
    prom=result[str]+result[slb]
    result.append(prom)
    prom=[]
    if str<slb:
        del a[slb]
        del a[str]
        del result[slb]
        del result[str]
    else:
        del a[str]
        del a[slb]
        del result[str]
        del result[slb]
    
    str=slb=0
    min=1000
    a.append(sredn)#ç¦ Ð·Ð· ë¨ÆåÖáñ, ó Ò¨Ô·Ð· ·µ Ô  Þ¦áÖ
    sredn=[]
    #ó ÔÖëÖ ãÖó¦ ¨Ò Ò åá·¤ç á ããåÖÞÔ·½
    c = []
    final=[]
    for i in range(len(a)):
        for j in range(len(a)):
            sum=0
            for k in range(len(a[i])):
                sum+=((a[i][k]-a[j][k])**2)
            sum=(sum**(1/2))
            c.append(sum)
            if len(c)==len(a):
                final.append(c)
                c=[]
    print("æ¨Æçù Þ Ò åá·¤  á ããåÖÞÔ·½:")
    for i in range(len(final)):
        print(*final[i])
    print("æ¨Æçù¨¨ ÆÖÐ·û¨ãåëÖ ÆÐ ãå¨áÖë:", len(final))
    print("æ¨Æçù·¨ ÆÐ ãå¨áñ:")
    for i in range(len(result)):
        print(i+1, result[i])    

print("äØ·ãÖÆ ÆÐ ãå¨áÖë · ÔÖÒ¨á  ãÖ¦¨áé ù·µãÞ ë Ô·µ ·óÖ¢á é¨Ô·½:")
for i in range(len(result)):
    print(i+1, result[i])
    for j in range(len(result[i])):
        print(result[i][j])
        printpic(result[i][j]-1)
#print("ëã¨, ØÐ·ó ¦ ½å¨ ÒÔ¨ 20 ¢ ÐÐÖë, Þ û¨ãåÔÖ ã Ò Ø·ã Ð")