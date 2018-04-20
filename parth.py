from tkinter import *
win=Tk()
count=0
def addrec():
    f=open('stock.txt','a')
    deptname=s1.get()
    deptid=s2.get()
    hod=s3.get()
    nfaculties=s4.get()
    nstudents=s5.get()
    f.writelines(deptname.ljust(5)+deptid.ljust(20)+hod.ljust(20)+nfaculties.ljust(20)+nstudents.ljust(10)+"\n")
    f.close()
def delrec():
    prt_rcd=[s1.get(),s2.get(),s3.get(),s4.get(),s5.get()]
    f=open('stock.txt','r')
    lines=f.readlines()
    print(lines)
    print(prt_rcd)
    f.close()
    f=open('stock.txt','w')
    for i in lines:
        m=i.split()
        print(m)
        if(m!=prt_rcd):
             f.writelines(m[0].ljust(5)+m[1].ljust(20)+m[2].ljust(20)+m[3].ljust(20)+m[4].ljust(10)+"\n")
    f.close()
def updaterec():
    a1=s1.get()
    a2=s2.get()
    a3=s3.get()
    a4=s4.get()
    a5=s5.get()
    f=open('stock.txt','r')
    h=f.readlines()
    f.close()
    f=open('stock.txt','w')
    flag=0
    for i in h:
        j=i.split()
        if(j[0]!=a1):
            f.writelines(j[0].ljust(5)+j[1].ljust(20)+j[2].ljust(20)+j[3].ljust(20)+j[4].ljust(10)+"\n")
    
        else:
            f.writelines(a1.ljust(5)+a2.ljust(20)+a3.ljust(20)+a4.ljust(10)+a5.ljust(10)+"\n")
            flag=1
    f.close()
def searchrec():
    var=s1.get()
    f=open('stock.txt','r')
    h=f.readlines()
    for i in h:
        j=i.split()
        if(j[0]==var): 
            print(j)
            s1.set(j[0])
            s2.set(j[1])
            s3.set(j[2])
            s4.set(j[3])
            s5.set(j[4])
    f.close()  
def nextrec():
    f=open('stock.txt','r')
    i=0
    global count
    while(i<=count):
        l=f.readline()
        i=i+1
    info=l.split()
    s1.set(info[0])	
    s2.set(info[1])
    s3.set(info[2])
    s4.set(info[3])
    s5.set(info[4])
    count=count+1
    f.close()
def prevrec():
    global count
    i=0
    count=count-1
    print(count)
    f=open("stock.txt","r")
    while(i<=count-1):
        l=f.readline()
        i=i+1
        print(l)
    rec=l.split()
    s1.set(rec[0])
    s2.set(rec[1])
    s3.set(rec[2])
    s4.set(rec[3])
    s5.set(rec[4])
def first():
    f=open("stock.txt",'r')
    k=f.readlines()[0]
    j=k.split()
    print(j)
    s1.set(j[0])
    s2.set(j[1])
    s3.set(j[2])
    s4.set(j[3])
    s5.set(j[4])
    f.close()
def last():
    f=open("stock.txt",'r')
    de=sum(1 for i in open("stock.txt"))-1
    print(de)
    k=f.readlines()[de]
    j=k.split()
    s1.set(j[0])
    s2.set(j[1])
    s3.set(j[2])
    s4.set(j[3])
    s5.set(j[4])
    f.close()
s1=StringVar()
s2=StringVar()
s3=StringVar()
s4=StringVar()
s5=StringVar()
l1=Label(win,text="Stock Name")
l2=Label(win,text="Market Cap")
l3=Label(win,text="EPS")
l4=Label(win,text="EBIDTA")
l5=Label(win,text="Profit After Tax")
t1=Entry(win,textvariable=s1)
t2=Entry(win,textvariable=s2)
t3=Entry(win,textvariable=s3)
t4=Entry(win,textvariable=s4)
t5=Entry(win,textvariable=s5)
b1=Button(win,text="ADD",command=addrec)
b2=Button(win,text="DELETE",command=delrec)
b3=Button(win,text="UPDATE",command=updaterec)
b4=Button(win,text="SEARCH",command=searchrec)
b5=Button(win,text="NEXT",command=nextrec)
b6=Button(win,text="PREVIOUS",command=prevrec)
b7=Button(win,text="FIRST",command=first)
b8=Button(win,text="LAST",command=last)
l1.grid(row=1,column=1,sticky=E)
l2.grid(row=2,column=1,sticky=E)
l3.grid(row=3,column=1,sticky=E)
l4.grid(row=4,column=1,sticky=E)
l5.grid(row=5,column=1,sticky=E)
t1.grid(row=1,column=2)
t2.grid(row=2,column=2)
t3.grid(row=3,column=2)
t4.grid(row=4,column=2)
t5.grid(row=5,column=2)
b1.grid(row=6,columnspan=2)
b2.grid(row=7,column=1)
b3.grid(row=8,column=1)
b4.grid(row=6,column=2)
b5.grid(row=7,column=2)
b6.grid(row=8,column=2)
b7.grid(row=10,column=1)
b8.grid(row=10,column=2)
win.mainloop()
