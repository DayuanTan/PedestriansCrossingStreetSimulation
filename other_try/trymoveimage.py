from tkinter import *
import time

root = Tk()



def next_image(event):
    leng =  len(items)
    for i in range(leng):
        print("i: ", i)
        move_one_img(items[i], 10*(i+1), 10*(i+1))
        # time.sleep(2)
        
    
def move_one_img(item, xoff, yoff):
    canvas1.move(item, xoff, yoff)
    root.after(3000, func=None)

        
    # canvas1.move(item1, 10, 0) # <--- Use Canvas.move method.
    # canvas1.move(item2, 0, 1)
    
    

image1 = r"other_try/ped_lr.png"
photo1 = PhotoImage(file=image1)
# photo1 = PhotoImage(file="other_try/ped_lr.png")
width1 = photo1.width()
height1 = photo1.height()
canvas1 = Canvas(width=600, height=300)
canvas1.pack(expand=1, fill=BOTH) # <--- Make your canvas expandable.
x = (width1)/2.0
y = (height1)/2.0
item1 = canvas1.create_image(x, y, image=photo1) # <--- Save the return value of the create_* method.

photo2 = PhotoImage(file=image1)
width2 = photo1.width()
height2 = photo1.height()
x = (width2)/2.0
y = (height2)/2.0
item2 = canvas1.create_image(x, y+100, image=photo2) # <--- Save the return value of the create_* method.

items = list()
items.append(item1)
items.append(item2)

canvas1.bind('<Button-1>', next_image)
root.mainloop() 