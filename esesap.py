import tkinter as tk
from tkinter import ttk
import os 
import shutil
from tkinter import messagebox as m_box

win=tk.Tk()
win.title("esesap")
win.geometry('540x160')
win.resizable(width=False,height=False)
win.wm_iconbitmap("e32.ico")

#filetuple----------

dict_extension = {
    'images':('jpg','jpeg','bmp','png','gif','tiff','psd','webp','svg','ai','ico'),
    'documents':('txt','docx','doc','pdf','tex','wks','wpd','odt','rtf','wps'),
    'videos':('mkv','avi','mp4','m4a','m4v','3gp','3gp2','3g2','ogg','wmv','flv'),
    'songs':('3ga','aa','aa3','mp3')
}

        


##Labels---------
folder=tk.Label(win,text="ENTER THE PATH OF FOLDER : ")
folder.grid(row = 0 , column = 0,sticky=tk.W)

#Folders name---------

folder_one=tk.Label(win,text="ENTER NAME OF IMAGES FOLDER : ")
folder_one.grid(row=1,column=0,sticky=tk.W)

folder_two=tk.Label(win,text="ENTER NAME OF DOCUMENTS FOLDER : ")
folder_two.grid(row=2,column=0,sticky=tk.W)

folder_three=tk.Label(win,text="ENTER NAME OF VIDEOS FOLDER : ")
folder_three.grid(row=3,column=0,sticky=tk.W)

folder_four=tk.Label(win,text="ENTER NAME OF SONGS FOLDER")
folder_four.grid (row=4,column=0,sticky=tk.W)


#entry -----------------
folder_path=tk.StringVar()
folder_entry=tk.Entry(win,width=50,textvariable=folder_path)
folder_entry.grid(row=0,column=1)

#FOLDER ENTRY---------
folder_one_var=tk.StringVar()
folder_one_entry=tk.Entry(win,width=50,textvariable=folder_one_var)
folder_one_entry.grid(row=1,column=1)

folder_two_var=tk.StringVar()
folder_two_entry=tk.Entry(win,width=50,textvariable=folder_two_var)
folder_two_entry.grid(row=2,column=1)

folder_three_var=tk.StringVar()
folder_three_entry=tk.Entry(win,width=50,textvariable=folder_three_var)
folder_three_entry.grid(row=3,column=1)

folder_four_var=tk.StringVar()
folder_four_entry=tk.Entry(win,width=50,textvariable=folder_four_var)
folder_four_entry.grid(row=4,column=1)

#filemove ...............
def filemove(folder_path,file_extensions):
    l=[]
    for file in os.listdir(folder_path):
        for extension in file_extensions:
            if(file.endswith(extension)):
                l.append(file)
    return l
#check.....

#action--------
def action():
    path=folder_path.get()
    if os.path.exists(path):
        i=0
    else:
        m_box.showerror('Path Error','Enter A Valid Path')
        return 3    
    folder_name_list=[folder_one_var.get(),folder_two_var.get(),folder_three_var.get(),folder_four_var.get()]
    for j in folder_name_list:
        if(j==''):
            m_box.showerror('No Name Error','Fill All Feilds')
            return 1
    i=0
    for type,extension in dict_extension.items():
        fileslist=filemove(path,extension)
        if (len(fileslist)>0):
            new_path=os.path.join(path,folder_name_list[i])
            try:
                os.mkdir(new_path)
            except:
                m_box.showerror('Error Name','Folder Already Exist Or Invalid Folder Name')
                return 2

            for files in fileslist :
                old_path=os.path.join(path,files)
                shutil.move(old_path,new_path)
        i+=1   
    m_box.showinfo('Complete','Complete')

#Submit button--------
submit_btn=tk.Button(win,text="Submit",command=action)
submit_btn.grid(row=5,column=0,sticky=tk.W)




win.mainloop()
