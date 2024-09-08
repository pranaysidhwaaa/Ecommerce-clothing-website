#!/usr/bin/env python
# coding: utf-8

# In[22]:


from tkinter import *
r=Tk()
r.geometry('1300x1300')
def display():
    s1=e1.get()
    print(s1)
    l1=Label(r,text='Name:  '+s1,font=('Times New Roman New Roman',21))
    l1.place(x=10,y=650)
    s2=e2.get()
    l2=Label(r,text='Password: '+s2,font=('Times New Roman',21))
    l2.place(x=10,y=690)
    print(s2)
    s8=e1.get()
    print(s8)
    l8=Label(r,text='Roll no.:  '+s8,font=('Times New Roman New Roman',21))
    l8.place(x=10,y=730)
    s5=v1.get()
    print(s5)
    l9=Label(r,text='Subject  '+s5,font=('Times New Roman New Roman',21))
    l9.place(x=10,y=770)
    s6=e3.get()
    print(s6)
    l10=Label(r,text='Marks:  '+s6,font=('Times New Roman New Roman',21))
    l10.place(x=10,y=810)
    s7=v2.get()
    print(s7)
    l11=Label(r,text='Class:  '+s7,font=('Times New Roman New Roman',21))
    l11.place(x=10,y=850)
l3=Label(r,text='Enter Your Name',font=('Times New Roman',21))
l3.place(x=10,y=70)
e1=Entry(r,font=('Times New Roman',21))
e1.place(x=280,y=70)
l4=Label(r,text='Enter Your Password',font=('Times New Roman',21))
l4.place(x=10,y=120)
e2=Entry(r,show='*',font=('Times New Roman',21))
e2.place(x=280,y=120)

l5=Label(r,text='Student roll no. ',font=('Times New Roman',21))
l5.place(x=10,y=180)
s3=Spinbox(r,from_=1,to=10000,font=('Times New Roman',21))
s3.place(x=280,y=180)


v1=IntVar()
l6=Label(r,text='Subject ',font=('Times New Roman',21))
l6.place(x=10,y=280)
R1=Radiobutton(r,text='Operating System',variable=v1,value=1,font=('Times New Roman',21))
R1.place(x=180,y=280)
R2=Radiobutton(r,text='Analysis of Algorithms',variable=v1,value=2,font=('Times New Roman',21))
R2.place(x=480,y=280)
R3=Radiobutton(r,text='Microprocessors',variable=v1,value=3,font=('Times New Roman',21))
R3.place(x=820,y=280)
R4=Radiobutton(r,text='Engineering Mathematics',variable=v1,value=4,font=('Times New Roman',21))
R4.place(x=250,y=320)
R5=Radiobutton(r,text='Database Management System',variable=v1,value=5,font=('Times New Roman',21))
R5.place(x=600,y=320)


l7=Label(r,text='Marks ',font=('Times New Roman',21))
l7.place(x=10,y=400)
e3=Entry(r,font=('Times New Roman',21))
e3.place(x=280,y=400)

v2=IntVar()
l6=Label(r,text='Class ',font=('Times New Roman',21))
l6.place(x=10,y=500)
R1=Radiobutton(r,text='Distinction',variable=v2,value=1,font=('Times New Roman',21))
R1.place(x=280,y=500)
R2=Radiobutton(r,text='First class',variable=v2,value=2,font=('Times New Roman',21))
R2.place(x=480,y=500)
R3=Radiobutton(r,text='Second Class',variable=v2,value=3,font=('Times New Roman',21))
R3.place(x=680,y=500)
R4=Radiobutton(r,text='Third Class',variable=v2,value=4,font=('Times New Roman',21))
R4.place(x=880,y=500)
R5=Radiobutton(r,text='Fail',variable=v2,value=5,font=('Times New Roman',21))
R5.place(x=1080,y=500)



b1=Button(r,text='Submit',font=('Times New Roman',21),command=display)
b1.place(x=120,y=580)
b2=Button(r,text='Clear',font=('Times New Roman',21))
b2.place(x=290,y=580)

r.mainloop()


# In[ ]:




