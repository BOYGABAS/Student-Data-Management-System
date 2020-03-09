from tkinter import *
import tkinter.ttk
import csv

class profile():
    def __init__(self,name,id_number,course):
        self.name=name
        self.id_number=id_number
        self.course=course

    #def timplit(self)

def mergesortpart2(arglist):
        if len(arglist)<=1: #This is the point where we reached the single item where it can't be split
            return arglist
        else:
            left=[]
            right=[]
            final=[]
            for i in range(len(arglist)): #This is where the elements in the list will either be assigned left or right
                if i<=(len(arglist)/2)-1:
                    left.append(arglist[i])
                else:
                    right.append(arglist[i])
            left=mergesortpart2(left) #This is where we split the already spltted lists
            right=mergesortpart2(right)
            while len(left)>0 and len(right)>0: #This is the sorting part
                if left[0].name<right[0].name:
                    final.append(left[0])
                    left.pop(0)
                else:
                    final.append(right[0])
                    right.pop(0)
            if len(left)==0: #If one side of the list is finished then slam the other list to the end of the sorted list as it is logically already sorted
                final.extend(right)
            else:
                final.extend(left)
            return final #return the sorted list

def serts(event):
    global profiles
    field = event.widget.get()
    field = field.strip().lower()
    #print(field)


    if field == "":
        profiles=[*preprofiles]
        pagecombo['values']=[*profilesname]

    else:
        #data = []
        profiles=[]
        newprofilesname=[]
        for item in range(len(profilesname)):
            if (field in profilesname[item].lower()) or (field in field in preprofiles[item].id_number):
                profiles.append(preprofiles[item])
                newprofilesname.append(profilesname[item])
        pagecombo['values']=[*newprofilesname]
        #print(profiles)
    #print("test")
    #pass

def select(event):
    global index
    index=pagecombo.current()
    clear()
    #print(index)
    #print(profiles)
    #print(profiles[index])
    #with profiles[pagecombo.current()] as referrence:
    a=Button(text="Edit",command=edite)
    a.grid(column=0,row=Rreferrence)
    a.configure(background="green")
    x=Label(text=profiles[index].name)
    x.grid(column=0,row=Rreferrence+1)
    x.configure(background="yellow")
    y=Label(text=profiles[index].id_number)
    y.grid(column=0,row=Rreferrence+2)
    y.configure(background="yellow")
    z=Label(text=profiles[index].course)
    z.grid(column=0,row=Rreferrence+3)
    z.configure(background="yellow")
    b=Button(text="Delete",command=delit)
    b.grid(column=0,row=Rreferrence+4)
    b.configure(background="red")

def delit():
    #print(index)
    #print(profiles[index].name)
    #print(profiles[0].name)
    #print(preprofiles.index(profiles[index]))
    preprofiles.remove(profiles[index])
    profiles.pop(index)
    #print(preprofiles)
    #print(profiles)
    refresh()

def konperm(i,j,k):
    profiles[index].name=i
    profiles[index].id_number=j
    profiles[index].course=k
    refresh()

def konperm_part_2(i,j,k):
    global preprofiles
    preprofiles.append(profile(i,j,k))
    print(len(profiles))
    refresh()

def edite(condit=0):
    clear()
    x1=Label(text="Name", bg="yellow")
    x1.grid(column=0,row=Rreferrence+1)
    #x.configure(background="yellow")
    y1=Label(text="Id Number", bg="yellow")
    y1.grid(column=0,row=Rreferrence+2)
    #y.configure(background="yellow")
    z1=Label(text="Course", bg="yellow")
    z1.grid(column=0,row=Rreferrence+3)
    x=Entry(page)
    x.grid(column=1,row=Rreferrence+1)
    #x.configure(background="yellow")
    y=Entry(page)
    y.grid(column=1,row=Rreferrence+2)
    #y.configure(background="yellow")
    z=Entry(page)
    z.grid(column=1,row=Rreferrence+3)
    if condit==0:
        w1=Label(text=("Editting "+profiles[index].name), bg="green")
        w1.grid(column=0,row=Rreferrence)
        x.insert(0,profiles[index].name)
        y.insert(0,profiles[index].id_number)
        z.insert(0,profiles[index].course)
        a=Button(text="Confirm",command=lambda: konperm(x.get(),y.get(),z.get()))
    else:
        w1=Label(text="Creating new student", bg="green")
        w1.grid(column=0,row=Rreferrence)
        a=Button(text="Confirm",command=lambda: konperm_part_2(x.get(),y.get(),z.get()))
    a.grid(column=1,row=Rreferrence)
    a.configure(background="green")
    v=Button(text="Cancel",command=refresh)
    v.grid(column=1,row=Rreferrence+4)
    v.configure(background="red")
    """
    w=Label(text="             ")
    w.grid(column=0,row=Rreferrence+4)
    w.configure(background="red")
    """

    #z.configure(background="yellow")
    #refresh()
def data():
    with open('profile.csv',newline='') as deyta:
        deita=csv.reader(deyta,delimiter=',')
        dieta=deita
        for row in dieta:
            preprofiles.append(profile(row[0],row[1],row[2]))

def update():
    with open('profile.csv','w',newline='') as deyta:
        deita=csv.writer(deyta,delimiter=',')
        for a in preprofiles:
            deita.writerow([a.name]+[a.id_number]+[a.course])

def test():
    x=Label(page,text=profiles[0].name)
    x.grid(column=0,row=0)
    pagecombo['values']=[pagecombo['values'][0],"YOW"]

def clear():
    list = page.grid_slaves()
    rowcount=0
    for l in list:
        rowcount+=1
    #print(rowcount)
    row=rowcount
    for l in list:
        if rowcount==2:
            pass
        elif row>2:
            l.destroy()
        row-=1
    #print(row)

def refresh():
    global profiles
    global preprofiles
    preprofiles=mergesortpart2(preprofiles)
    update()
    profiles=[*preprofiles]
    profilesname.clear()
    for i in profiles:
        profilesname.append(i.name)
    page.destroy()
    menu()

def menu():
    global page
    global pagecombo
    page = Tk()
    page.title("Student Database")
    page.configure(background="black")
    page.geometry('420x420')
    v=Button(text="Create new Account",command=lambda: edite(1))
    v.grid(column=0,row=1)
    v.configure(background="green")
    #btn = Button(page, text="Click Me",command=test)
    #btn.grid(column=0, row=0)
    #btn.configure(background="yellow")
    pagecombo=tkinter.ttk.Combobox(page)
    #pagecombo['values']= (1, 2, 3, 4, 5, "Text")
    pagecombo['values']= [*profilesname]
    pagecombo.bind("<<ComboboxSelected>>", select)
    pagecombo.bind('<KeyRelease>', serts)
    #pagecombo.current(0)

    pagecombo.grid(column=0, row=0)
    page.mainloop()

preprofiles=[]
profiles=[]
profilesname=[]
Rreferrence=2
data()
for i in preprofiles:
    profilesname.append(i.name)
profiles=[*preprofiles]
menu()
