import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

import resizer

#variables
image_path = ""


#tk colors
RED = "red"
GREEN = "green"
BLUE = "blue"
AQUA = "aqua"
BLACK = "black"
WHITE = "white"
LIGHT_GREY = "#D3D3D3"
DARK_GREY = "#A9A9A9"


#functions

#tk functions

def choose_image():
    global image_path
    choosen_image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    if choosen_image_path:
        choose_file_label.config(text=f"Seçilen dosya: {choosen_image_path}")
        image_path = choosen_image_path

def resize_image():
    # try:
        
    # except:
    #     messagebox.showerror("Bir hata oluştu!","Lütfen gerekli yerleri düzgün bir şekilde doldurduğunuza emin olup tekrar deneyin.")
    
    current_image_path = image_path
    current_image_width = int(choose_width_textbox.get())
    current_image_height =  int(choose_height_textbox.get())
    if(current_image_path != "" and current_image_width != "" and current_image_height != ""):
        resizer.resizeImageAndSave(current_image_path,current_image_width,current_image_height)
    
        messagebox.showinfo("Başarılı!","Resim başarıyla yeniden boyutlandırıldı!")
    else:
        messagebox.showerror("Resim seçilmedi!","Lütfen bir resim seçiniz.")


#tk root
root = tk.Tk()
root.title("Image Resizer")
root.geometry("700x250")
root.resizable(False,False)

root.grid_rowconfigure(0, weight=2)
root.grid_rowconfigure(1, weight=5)

#tk frames
top_frame = tk.Frame(root,bg=DARK_GREY,height=100,width=600)
top_frame.grid(row=0,column=0,sticky=tk.NSEW)

middle_frame = tk.Frame(root,bg=LIGHT_GREY,height=300,width=600)
middle_frame.grid(row=1,column=0,sticky=tk.NSEW)

#tk objects
#top_frame
choose_file_label = tk.Label(top_frame,text="Hiçbir resim seçilmedi.",wraplength=500,width=75)
choose_file_label.pack(side=tk.LEFT,padx=5)

choose_file_button = tk.Button(top_frame,text="Resim seç",command=choose_image)
choose_file_button.pack(side=tk.LEFT,padx=1)

#middle frame
choose_width_label = tk.Label(middle_frame,text="Genişlik : ",width=15)
choose_width_label.pack(side=tk.TOP,padx=5,pady=1)

choose_width_textbox = tk.Entry(middle_frame,width=15)
choose_width_textbox.pack(side=tk.TOP,padx=0)

x_label = tk.Label(middle_frame,text="x",width=2)
x_label.pack(side=tk.TOP,padx=5,pady=0)

choose_height_label = tk.Label(middle_frame,text="Yükseklik : ",width=15)
choose_height_label.pack(side=tk.TOP,padx=15,pady=1)

choose_height_textbox = tk.Entry(middle_frame,width=15)
choose_height_textbox.pack(side=tk.TOP,padx=0)

choose_file_button = tk.Button(middle_frame,text="Uygula",command=resize_image)
choose_file_button.pack(side=tk.TOP,pady=10)


def main():
    root.mainloop()


if __name__ == "__main__":
    main()