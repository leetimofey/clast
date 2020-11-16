def printpic(n):
    pic=[]
    for j in range(32):
        pic.append(start[n][j*32:(j+1)*32])
    for j in range(len(pic)):
        #print(*pic[j])
        for z in range(len(pic[j])):
            if pic[j][z]==1:
                print("# ", end='')
           # if pic[j][z]==2:
            #    print("#", end=' ')
            #if pic[j][z]==3:
            #    print("+", end=' ')
            if pic[j][z]==0:
                print("  ", end='')
            #if pic[j][z]==4:
             #   print("-", end=' ')                
            if z==31:
                print()
def printfile(n):
    with open('file.txt', 'w') as p:
        pic=[]
        for j in range(32):
            pic.append(start[n][j*32:(j+1)*32])
        for j in range(len(pic)):
            #print(*pic[j])
            for z in range(len(pic[j])):
                if pic[j][z]==1:
                    p.write("# ")
               # if pic[j][z]==2:
                #    print("#", end=' ')
                #if pic[j][z]==3:
                #    print("+", end=' ')
                if pic[j][z]==0:
                    p.write("  ")
                #if pic[j][z]==4:
                 #   print("-", end=' ')                
                if z==31:
                    p.write("\n")        
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
    
result=[]
for i in range(len(a)):
    result.append([i+1])
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
    
    
print("Vvedite kolvo klasterov:")
kolvo=int(input())

print("Spisok izobrazheniy:")
print()
for i in range(len(start)):
    print(i+1)
    printpic(i)
    
min=1000
str=0
slb=0
sredn=[]

while (len(final))!=kolvo:
    for i in range(len(final)):
        for j in range(len(final)):
            if i!=j and final[i][j]<min:
                min=final[i][j]
                str=i
                slb=j
    for i in range(len(a[str])):
        sredn.append((a[str][i]*len(result[str])+a[slb][i])*len(result[slb])/(len(result[str])+len(result[slb])))
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
    a.append(sredn)
    sredn=[]
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
    print("Tekushaya matritsa rasstoyaniy:")
    for i in range(len(final)):
        print(*final[i])
    print("Tekushee kolvo klasterov:", len(final))
    print("Tekushie klastery:")
    for i in range(len(result)):
        print(i+1, result[i])    

print("Spisok klasterov i soderzhashihsya v nih izobrazheniy:")
for i in range(len(result)):
    print(i+1, result[i])
    for j in range(len(result[i])):
        print(result[i][j])
        printpic(result[i][j]-1)
printfile(1)