from tkinter import *
from tkinter import ttk
from views import *
from tkinter import messagebox

#colors 
co0 = "#ffffff"
co1 = "#000000"
co2 = "#223CE6"

window = Tk()
window.title("Phonebook")
window.geometry('485x450')
window.configure(background=co0)
window.resizable(width=FALSE, height=FALSE)


#Frames
frame_up = Frame(window, width=500, height=50, bg=co2)
frame_up.grid(row=0, column=0, padx=0, pady=1)

frame_down = Frame(window, width=500, height=150, bg=co0)
frame_down.grid(row=1, column=0, padx=0, pady=1)

frame_table = Frame(window, width=500, height=100, bg=co0, relief='flat')
frame_table.grid(row=2, column=0, columnspan=2, padx=10,pady=1, sticky=NW)

#Functions
# Functions
def show():
    global tree
    list_header = ['Name', 'Gender', 'Telephone', 'Email']
    demo_list = viewdata()

    tree = ttk.Treeview(frame_table, selectmode='extended', columns=list_header, show="headings")
    vsb = ttk.Scrollbar(frame_table, orient='vertical', command=tree.yview)
    hsb = ttk.Scrollbar(frame_table, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(row=0, column=0, sticky='nsew')
    vsb.grid(row=0, column=1, sticky='ns')
    hsb.grid(row=1, column=0, columnspan=2, sticky='ew')

    for col, header in enumerate(list_header):
        tree.heading(header, text=header, anchor=NW)
        tree.column(header, width=112)  # You can adjust the width as needed

    for item in demo_list:
        tree.insert('', 'end', values=item)
    

# Call the show function outside
show()

def insertData():
    Name = e_name.get()
    Gender = c_gender.get()
    Telephone = e_telephone.get()
    Email = e_email.get()

    data = [Name, Gender, Telephone, Email]

    if Name == '' or Gender == '' or Telephone == '' or Email == '':
        messagebox.showwarning("data", 'Please fill in all fields')

    else:
        add(data)
        messagebox.showinfo('data', 'Data Added Successfully!')

        e_name.delete(0, 'end')
        c_gender.delete(0, 'end')
        e_telephone.delete(0, 'end')
        e_email.delete(0, 'end')

        show()

def toUpdate():
    try:
        tree_data = tree.focus()
        tree_dic = tree.item(tree_data)
        tree_list = tree_dic['values']

        Name = str(tree_list[0])
        Gender = str(tree_list[1])
        Telephone = str(tree_list[2])
        Email = str(tree_list[3])

        e_name.insert(0, Name)
        c_gender.insert(0, Gender)
        e_telephone.insert(0, Telephone)
        e_email.insert(0, Email)

        def confirm():
            new_name = e_name.get()
            new_gender = c_gender.get()
            new_telephone = e_telephone.get()
            new_email = e_email.get()

            data = [new_telephone, new_name, new_gender, new_telephone, new_email]
            update(data)

            messagebox.showinfo('Success', 'Data Updated Successfully!')

            e_name.delete(0, 'end')
            c_gender.delete(0, 'end')
            e_telephone.delete(0, 'end')
            e_email.delete(0, 'end')

            for widget in frame_table.winfo_children():
                widget.destroy()

            b_confirm.destroy()

            show()
        
        b_confirm = Button(frame_down, text ="Confirm", width=10,height=1, bg=co2, fg=co0, font=("Ivy 8 bold"), command=confirm)
        b_confirm.place(x=290, y=110)

    except IndexError:
        messagebox.showerror('Error', 'Select one of the Entry from the Table!')

def toRemove():
    try:
        tree_data = tree.focus()
        tree_dic = tree.item(tree_data)
        tree_list = tree_dic['values']
        tree_telephone = str(tree_list[2])

        removedata(tree_telephone)
        messagebox.showinfo('Success', 'Data has been Deleted Successfully!')

        for widget in frame_table.winfo_children():
            widget.destroy()

        show()

    except IndexError:
        messagebox.showerror('Error', 'Select one of the Entry from the Table!')

def toSearch():
    telephone = e_search.get()

    data = search(telephone)

    def delete_commend():
        tree.delete(*tree.get_children())

    delete_commend()

    for item in data:
        tree.insert('', 'end', values = item)

    e_search.delete(0, 'end')

#Frame_up widgets
app_name = Label(frame_up, text="Phonebook App", height=1, font=('Verdana 17 bold'), bg=co2,fg=co0)
app_name.place(x=5, y=5)

#Frame_down widgets
l_name = Label(frame_down, text="Name *", width=20, height=1, font=("Ivy 10"), bg=co0, anchor=NW)
l_name.place(x=10, y=20)
e_name = Entry(frame_down, width=25, justify="left", highlightthickness=1, relief="solid")
e_name.place(x=80, y=20)

l_gender = Label(frame_down, text="Gender *", width=20, height=1, font=("Ivy 10"), bg=co0, anchor=NW)
l_gender.place(x=10, y=50)
c_gender = ttk.Combobox(frame_down, width=27)
c_gender['values'] = ['', 'F', 'M']
c_gender.place(x=80, y=50)

l_telephone = Label(frame_down, text="Telephone*", height=1, font=("Ivy 10"), bg=co0, anchor=NW)
l_telephone.place(x=10, y=80)
e_telephone = Entry(frame_down, width=25, justify="left", highlightthickness=1, relief="solid")
e_telephone.place(x=80, y=80)

l_email = Label(frame_down, text="Email *", height=1, font=("Ivy 10"), bg=co0, anchor=NW)
l_email.place(x=10, y=110)
e_email = Entry(frame_down, width=25, justify="left", highlightthickness=1, relief="solid")
e_email.place(x=80, y=110)

b_search = Button(frame_down, text ="Search", height=1, bg=co2, fg=co0, font=("Ivy 8 bold"), command=toSearch)
b_search.place(x=290, y=20)
e_search = Entry(frame_down, width=16, justify="left", font=('Ivy', 11), highlightthickness=1, relief="solid")
e_search.place(x=347, y=20)

b_view = Button(frame_down, text ="View", width=10,height=1, bg=co2, fg=co0, font=("Ivy 8 bold"), command=show)
b_view.place(x=290, y=50)

b_add = Button(frame_down, text ="Add", width=10,height=1, bg=co2, fg=co0, font=("Ivy 8 bold"), command=insertData)
b_add.place(x=400, y=50)

b_update = Button(frame_down, text ="Update", width=10,height=1, bg=co2, fg=co0, font=("Ivy 8 bold"), command=toUpdate)
b_update.place(x=400, y=80)

b_delete = Button(frame_down, text ="Delete", width=10,height=1, bg=co2, fg=co0, font=("Ivy 8 bold"), command=toRemove)
b_delete.place(x=400, y=110)


window.mainloop()