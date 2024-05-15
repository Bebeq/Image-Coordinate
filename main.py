import cv2 
import tkinter
from tkinter import filedialog
import os

# Inisiasi Awal Tkinter
root = tkinter.Tk()
root.withdraw()

def click_event(event, x, y, flags, params): 
    # Fungsi Left Click
    if event == cv2.EVENT_LBUTTONDOWN: 
        # Menampilkan Koordinat Di Terminal
        print(x, ',', y) 
        # Menampilkan Koordinat Di Gambar
        font = cv2.FONT_HERSHEY_SIMPLEX 
        cv2.putText(img, str(x) + ',' +
                    str(y), (x,y), font, 
                    1, (255, 255, 0), 2)
        # Menampilkan Titik Tepat Koordinat
        cv2.circle(img, (x,y), radius=0, color=(0, 0, 255), thickness=5)
        cv2.imshow("Image", img) 

def search_file():
    file = filedialog.askopenfilename(title="Open Image File", filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ico *.tif")])
    return file

if __name__=="__main__": 
    print("Image Coordinate\nAuthor : Bebeq (https://github.com/Bebeq)\n")
    
    # Membuka File
    file_path = search_file()
    file_name = file_path.split("/")[-1]
    print ("Open Image Name : " , file_name)

    if file_path:
        # Menampilkan Image
        img = cv2.imread(file_path, 1) 
        cv2.imshow("Image", img) 
        cv2.setMouseCallback("Image", click_event) 
        cv2.waitKey(0) 
        cv2.destroyAllWindows() 
