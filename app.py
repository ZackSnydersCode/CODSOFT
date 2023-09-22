import tkinter as graphics
from tkinter import ttk
def creating_of_task():
    task = entry.get()
    if task:
        listbox.insert(graphics.END, task)
        entry.delete(0, graphics.END)
def update_my_list():
    selected_task = listbox.curselection()
    if selected_task:
        updated_task = entry.get()
        if updated_task:
            listbox.delete(selected_task)
            listbox.insert(selected_task[0],updated_task)
            entry.delete(0,graphics.END)
def remove_task():
    grabbed_task = listbox.curselection()
    if grabbed_task:
        listbox.delete(grabbed_task)
env = graphics.Tk()
env.title('CODSOFT (To Do List)')
env.configure(bg='green')
const_height = 390
const_width = 495
env.geometry(f'{const_width}x{const_height}')
screen_height = env.winfo_screenheight()
screen_width = env.winfo_screenwidth()
env.resizable(False,False)
listbox_height = int(screen_height/50)
listbox_width = int(screen_width/20)

listbox = graphics.Listbox(env, height=listbox_height, width=listbox_width-21,font=("Helvetica", 15))
listbox.place(x=10,y=10)

entry = graphics.Entry(env,width=20,font=("Helvetica", 14))
entry.place(x=10,y=355)

add_button = ttk.Button(env, text='New Task', command=creating_of_task,style='Rounded.TButton')
add_button.place(x=248,y=355)

remove_button = ttk.Button(env, text='Remove', command=remove_task,style='Rounded.TButton')
remove_button.place(x=330,y=355)

update_my_task = ttk.Button(env, text='Update', command=update_my_list,style='Rounded.TButton')
update_my_task.place(x=413,y=355)
env.mainloop()
