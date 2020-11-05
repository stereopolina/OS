#this work was done by Polina Romanenkova
# for de_assignment Computational Practicum
from tkinter import *
import matplotlib
from module import drawer, list_of_data, list_of_data_for_grids

matplotlib.use("TkAgg")
LARGE_FONT = ("VErdana", 12)

root = Tk()


def main_window():
    root_loop = Tk()
    frame_high = Frame(root_loop)
    frame_high.pack(side=TOP)
    frame_low = Frame(root_loop)
    frame_low.pack(side=TOP)

    x0 = 1.0
    y0 = 2.0
    x = 10.0
    num = 10
    xarr = []
    x1grid = 1.0
    x2grid = 10.0
    for i in range(0, num + 1):
        xarr.append((x - x0) / num * x0)
    if list_of_data:
        if list_of_data[-4] == '':
            x0 = 1.0
        else:
            x0 = float(list_of_data[-4])

        if list_of_data[-3] == '':
            y0 = 2.0
        else:
            y0 = float(list_of_data[-3])
        if list_of_data[-2] == '':
            x = 10.0
        else:
            x = float(list_of_data[-2])
        if list_of_data[-1] == '':
            num = 10
        else:
            num = int(list_of_data[-1])


        if list_of_data_for_grids[0] == '':
            x1grid = 1.0
        else:
            # print(list_of_data_for_grids[0])
            x1grid = float(list_of_data_for_grids[0])

        if list_of_data_for_grids[1] == '':
            x2grid = 10.0
        else:
            x2grid = float(list_of_data_for_grids[1])

        drawer(root_loop, frame_high, frame_low, x0, y0, x, num, x1grid, x2grid)
    else:
        drawer(root_loop, frame_high, frame_low, x0, y0, x, num, x1grid, x2grid)
    Button(frame_high, text="Create plots",
           command=lambda: [root_loop.destroy(), main_window()]).pack(side=LEFT)
    root_loop.mainloop()


frameHigh = Frame(root)
frameHigh.pack(side=TOP)

frameLow = Frame(root)
frameLow.pack(side=TOP)

# x0 = 1.0
# y0 = 2.0
# x = 10.0
# num = 10
root.title('Computational Practicum')
root.geometry('1100x1000+300+200')
root.protocol('WM_DELETE_WINDOW')
root.resizable(True, False)
drawer(root, frameHigh, frameLow, 1.0, 2.0, 10.0, 10, 1.0, 10.0)
test = Button(frameHigh, text="Create plots",
              command=lambda: [root.destroy(), main_window()]).pack(side=LEFT)
root.mainloop()
