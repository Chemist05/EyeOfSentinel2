import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from tkinter import filedialog
import matplotlib.pyplot as plt
import rasterio as rio
from rasterio.plot import reshape_as_image
import cv2
import time
import os
import random







# add file path ch2
list1 = []
def upload1():

    """uploading a TIFF file for Channel 2"""
    file = filedialog.askopenfile(initialdir="/", title="Select a file", filetypes=[("tiff file", "*.tiff")])
    split_list = file.name.split("/")

    ctk.CTkLabel(main_frame, text=split_list[-1]).grid(row=2, column=0)

    list1.append(file.name)


# add file path ch3
list2 = []
def upload2():

    """uploading a TIFF file for Channel 3"""
    file = filedialog.askopenfile(initialdir="/", title="Select a file", filetypes=[("tiff file", "*.tiff")])
    split_list = file.name.split("/")

    ctk.CTkLabel(main_frame, text=split_list[-1]).grid(row=2, column=1)

    list2.append(file.name)


# add file path ch4
list3 = []
def upload3():

    """uploading a TIFF file for Channel 4"""
    file = filedialog.askopenfile(initialdir="/", title="Select a file", filetypes=[("tiff file", "*.tiff")])
    split_list = file.name.split("/")

    ctk.CTkLabel(main_frame, text=split_list[-1]).grid(row=5, column=0)

    list3.append(file.name)


# add file path ch8
list4 = []
def upload4():

    """uploading a TIFF file for Channel 8"""
    file = filedialog.askopenfile(initialdir="/", title="Select a file", filetypes=[("tiff file", "*.tiff")])
    split_list = file.name.split("/")

    ctk.CTkLabel(main_frame, text=split_list[-1]).grid(row=5, column=1)

    list4.append(file.name)


# add file path ch11
list5 = []
def upload5():

    """uploading a TIFF file for Channel 11"""
    file = filedialog.askopenfile(initialdir="/", title="Select a file", filetypes=[("tiff file", "*.tiff")])
    split_list = file.name.split("/")

    ctk.CTkLabel(main_frame, text=split_list[-1]).grid(row=8, column=0)

    list5.append(file.name)










def start():
    start = time.perf_counter()
    
    """first message"""
    messagebox.showwarning(title="Loading", message="Don't close the application!! \nBut close this warningbox \n\nIt will take few minutes \nPlease have patience :/")

    
    """open and reshape the Channels"""
    with rio.open(list1[-1]) as src:
        img_chan_11 = reshape_as_image(src.read())

    with rio.open(list2[-1]) as src:
        img_chan_8 = reshape_as_image(src.read())

    with rio.open(list3[-1]) as src:
        img_chan_4 = reshape_as_image(src.read())

    with rio.open(list4[-1]) as src:
        img_chan_3 = reshape_as_image(src.read())

    with rio.open(list5[-1]) as src:
        img_chan_2 = reshape_as_image(src.read())
        
    end = time.perf_counter()

    """shows how much time it takes to open and reshape the Channels (not important)"""
    print(f"Zeit: {round(end-start, 2)}")


    """resize the Channels"""
    img_chan_11_resized = cv2.resize(img_chan_11, (2745, 2745))
    img_chan_8_resized = cv2.resize(img_chan_8, (2745, 2745))
    img_chan_4_resized = cv2.resize(img_chan_4, (2745, 2745))
    img_chan_3_resized = cv2.resize(img_chan_3, (2745, 2745))
    img_chan_2_resized = cv2.resize(img_chan_2, (2745, 2745))


    start = time.perf_counter()
    
    """calculate NDVI, NDWI, NDSI, NDBI, NDBSI"""
    ndvi = (img_chan_8_resized.astype(float) - img_chan_4_resized.astype(float)) / (img_chan_8_resized + img_chan_4_resized)
    
    ndwi = (img_chan_3_resized.astype(float) - img_chan_8_resized.astype(float)) / (img_chan_3_resized + img_chan_8_resized)
    
    ndsi = (img_chan_3_resized.astype(float) - img_chan_11_resized.astype(float)) / (img_chan_3_resized + img_chan_11_resized)
    
    ndbi = (img_chan_11_resized.astype(float) - img_chan_8_resized.astype(float)) / (img_chan_11_resized + img_chan_8_resized)
    
    ndbsi = ((img_chan_4_resized.astype(float) + img_chan_11_resized.astype(float)) - (img_chan_8_resized.astype(float) + img_chan_2_resized.astype(float))) / ((img_chan_4_resized.astype(float) + img_chan_11_resized.astype(float)) + (img_chan_8_resized.astype(float) + img_chan_2_resized.astype(float)))
    
    end = time.perf_counter()
    
    """shows how much time it takes to calculate NDVI, NDWI, etc (not important)"""
    print(f"Zeit: {round(end-start, 2)}")
    
    
    """create new folder for plots"""
    diff = random.randint(10000000000, 99999999999)
    os.makedirs(f"{diff}_ND_plots")

    
    """NDVI plot"""
    plt.imshow(ndvi, cmap="RdYlGn")
    plt.colorbar()
    plt.title("NDVI")
    plt.axis("off")
    plt.savefig(f"{diff}_ND_plots/NDVI.png")
    plt.clf()
    
    """NDWI plot"""
    plt.imshow(ndwi, cmap="Blues")
    plt.colorbar()
    plt.title("NDWI")
    plt.axis("off")
    plt.savefig(f"{diff}_ND_plots/NDWI.png")
    plt.clf()
    
    """NDSI plot"""
    plt.imshow(ndsi, cmap="winter")
    plt.colorbar()
    plt.title("NDSI")
    plt.axis("off")
    plt.savefig(f"{diff}_ND_plots/NDSI.png")
    plt.clf()
    
    """NDBI plot"""
    plt.imshow(ndbi, cmap="OrRd")
    plt.colorbar()
    plt.title("NDBI")
    plt.axis("off")
    plt.savefig(f"{diff}_ND_plots/NDBI.png")
    plt.clf()
    
    """NDBSI plot"""
    plt.imshow(ndbsi, cmap="YlOrBr")
    plt.colorbar()
    plt.title("NDBSI")
    plt.axis("off")
    plt.savefig(f"{diff}_ND_plots/NDBSI.png")
    plt.clf()


    """second message"""
    messagebox.showinfo(title="result", message="it is finish :)")


#style
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

window = ctk.CTk()


#center application in screen
width = 520
height = 520

screenw = window.winfo_screenwidth()
screenh = window.winfo_screenheight()

x = (screenw // 2) - (width // 2)
y = (screenh // 2) - (height // 2)

lol = f"{width}x{height}+{int(x)}+{int(y)}"

window.geometry(lol)


# static and title
window.resizable(False, False)
window.title("EyeOfSentinel2")

# frame
main_frame = ctk.CTkFrame(window)
main_frame.grid(row=1, column=0, padx=82, pady=22)


# widget outside frame
ctk.CTkLabel(window, text="Generator for NDVI, NDWI, NDSI, NDBI, NDBSI", font=("Ubuntu", 16)).grid(row=0, columnspan=2, pady=10)


# widgets in frame

# Channel 2
ctk.CTkLabel(main_frame, text="File of Channel 2: ", font=("Ubuntu", 11)).grid(row=1, column=0)
ctk.CTkButton(main_frame, text="Upload Ch2", command=upload1).grid(row=3, column=0)

# Channel 3
ctk.CTkLabel(main_frame, text="File of Channel 3: ", font=("Ubuntu", 11)).grid(row=1, column=1)
ctk.CTkButton(main_frame, text="Upload Ch3", command=upload2).grid(row=3, column=1)

# Channel 4
ctk.CTkLabel(main_frame, text="File of Channel 4: ", font=("Ubuntu", 11)).grid(row=4, column=0)
ctk.CTkButton(main_frame, text="Upload Ch4", command=upload3).grid(row=6, column=0)

# Channel 8
ctk.CTkLabel(main_frame, text="File of Channel 8: ", font=("Ubuntu", 11)).grid(row=4, column=1)
ctk.CTkButton(main_frame, text="Upload Ch8", command=upload4).grid(row=6, column=1)

# Channel 11
ctk.CTkLabel(main_frame, text="File of Channel 11: ", font=("Ubuntu", 11)).grid(row=7, column=0)
ctk.CTkButton(main_frame, text="Upload Ch11", command=upload5).grid(row=9, column=0)

# start
ctk.CTkButton(main_frame, text="Start", command=start, width=47, fg_color="green").grid(row=9, column=1, sticky=tk.N+tk.W+tk.S+tk.E)


# widget outside frame
ctk.CTkLabel(window, text="Website:", font=("Ubuntu", 13)).grid(row=10, columnspan=2)

# every widget (in frame) padding
for wig in main_frame.winfo_children():
    wig.grid_configure(padx=20, pady=10)

window.mainloop()