'''a=[]
with open('hash.csv', 'r') as f:
    for line in f:
        line=line[:-1]
        b=list(map(int, line.split(',')))
        a.append(b)
start=a
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
        

for i in range(len(final)):
    print(*final[i])
print(len(final), "pis")
for i in range(len(final)):
    print(len(final[i]))'''
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
    
#��󦠨� Ҡ��� ������� �Р�����
result=[]
for i in range(len(a)):
    result.append([i+1])
#��󦠨� Ҡ�ᷤ� ������Է�
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
    
    
print("�먦�� ��з������ �Р�����:")
kolvo=int(input())

min=1000
str=0
slb=0
sredn=[]

while (len(final))!=kolvo:#��Ơ �Р����� ������ ��� Ԡ��
    for i in range(len(final)):
        for j in range(len(final)):
            if i!=j and final[i][j]<min:#Ԡ�֦�� ҷԷҠ���֨ ������Է�
                min=final[i][j]
                str=i
                slb=j
    for i in range(len(a[str])):
        sredn.append((a[str][i]*len(result[str])+a[slb][i])*len(result[slb])/(len(result[str])+len(result[slb])))#ب������련� ަ��
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
    a.append(sredn)#禠зз ������, �ҨԷз �� Ԡ ަ��
    sredn=[]
    #����� ��󦠨� Ҡ�ᷤ� ������Է�
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
    print("������ Ҡ�ᷤ� ������Է�:")
    for i in range(len(final)):
        print(*final[i])
    print("������ ��з������ �Р�����:", len(final))
    print("������ �Р����:")
    for i in range(len(result)):
        print(i+1, result[i])    
print("�ط��� ��֢��Է�:")
for i in range(len(start)):
    print(i+1)
    #print(i+1, start[i])
    pic=[]
    for j in range(6):
        pic.append(start[i][j*6:(j+1)*6])
    for j in range(len(pic)):
        #print(*pic[j])
        for z in range(len(pic[j])):
            if pic[j][z]==1:
                print("�", end=' ')
            if pic[j][z]==0:
                print(" ", end=' ')
            if z==5:
                print()
print("�ط��� �Р����� � ��Ҩ� �֦�������� � Է� ��֢��Է�:")
for i in range(len(result)):
    print(i+1, result[i])
print("��, �з� ���� �Ԩ 20 ������, � ������ �� ط��")