import pickle
def write():
    f=open("students.dat","wb")
    record=[]
    while True:
        rno=int(input("enter roll number"))
        name=input("enter name")
        marks=int(input("enter marks"))
        data=[rno,name,marks]
        record.append(data)
        ch=input("do you want to continue?")
        if ch=='n':
            break
    pickle.dump(record,f)



def read():
    f=open("students.dat",'rb')
    while True:
        try:
            s=pickle.load(f)
            for i in s:
                print(i)
        except EOFError:
            break

    f.close()

def append():
    f=open("students.dat","ab")
    record=[]
    while True:
        rno=int(input("enter roll number"))
        name=input("enter name")
        marks=int(input("enter marks"))
        data=[rno,name,marks]
        record.append(data)
        ch=input("do you want to continue?")
        if ch=='n':
            break
    pickle.dump(record,f)
    f.close()
def search():
    f=open("students.dat","rb")
    s=pickle.load(f)
    found=0
    rno=int(input("enter roll number whose record you want to search"))
    for i in s:
        if i[0]==rno:
            print(i)
            found=1
    if found==0:
        print("record not found")

def update():
    f=open("students.dat","rb+")
    s=pickle.load(f)
    found=0
    rno=int(input("roll number for record to be updated"))
    for i in s:
        if rno==i[0]:
            print("current name",i[1])
            i[1]=input("enter new name")
            found=1
            break
    if found==0:
        print("record not found")
    else:
        f.seek(0)
        pickle.dump(s,f)
    f.close()
    
    
    
    
write()
#append()
read()
#search()
update()
read()
print("hello beutiful people outhere")
