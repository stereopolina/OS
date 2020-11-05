#this work was done by Polina Romanenkova
# for de_assignment Computational Practicum
import tkinter
from tkinter import *
from tkinter import messagebox

import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from solid import Euler, ImprovedEuler, RungeKutta, MySolution, my_func, ceilmy
import numpy as np

matplotlib.use("TkAgg")

# here is the end of import-statements


list_of_data = ['', '', '', '']
list_of_data_for_grids = ['', '']# global array to insert variables

list_of_checkers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # global array to evaluate, what to draw


# here i intoduce a very strande thing:
# everycheckbutton will have its number and by it i will understand,
# which checbuttons were pressed


def error_handling(x0, x, num, x1grid, x2grid):
    if x < x0:
        messagebox.showerror("Error", "x can not be less, than x0\nit was set to x0 + 1")

    if num == 0:
        messagebox.showerror("Error", "0 is too small to be a number of steps\nit was set to 10")

    if x1grid > x2grid:
        messagebox.showerror("Error", "x2 can not be less, than x1\nit was set to x1 + 1")

def drawer(root, frame_high, frame_low, x0, y0, x, num, x1grid, x2grid):
    error_handling(x0, x, num, x1grid, x2grid)

    if x < x0:
        x = x0 + 1
    if num <= 0:
        num = 10
    if x1grid > x2grid:
        x2grid = x1grid + 1

    root.title('Computational Practicum')
    root.geometry('1100x1000+300+200')
    root.protocol('WM_DELETE_WINDOW')
    root.resizable(True, False)
    frame_plot = Frame(frame_high)
    frame_plot.pack(side=LEFT)

    frame_check1 = Frame(frame_high)
    frame_check1.pack(side=RIGHT)

    frame_plot2 = Frame(frame_low)
    frame_plot2.pack(side=LEFT)

    frame_check2 = Frame(frame_low)
    frame_check2.pack(side=RIGHT)

    #

    # here intvars are created for checkbuttons
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()
    var8 = IntVar()
    var9 = IntVar()
    var10 = IntVar()

    # This function puts all labels into the window
    def labels():
        defau = Label(frame_check1, text="default values:\nx0=1.0\ny0=2.0\nx=10.0\nnum=10")
        defau.pack()

        gx0 = StringVar()  # we will take the string of user's command for x0 from here
        def getx0():  # function called if the new value was entered for x0
            lblx0.configure(text="Got it!")
            list_of_data[0] = gx0.get()

        lblx0 = Label(frame_check1, text="Enter x0:")
        lblx0.pack()
        txtx0 = Entry(frame_check1, width=1, textvariable=gx0)
        txtx0.pack()
        btnx0 = Button(frame_check1, text="Calculate x0", command=getx0)
        btnx0.pack()

        gy0 = StringVar()  # we will take the string of user's command for y0 from here

        def gety0():  # function called if the new value was entered for y0
            lbly0.configure(text="Got it!")
            list_of_data[1] = gy0.get()

        lbly0 = Label(frame_check1, text="Enter y0:")
        lbly0.pack()
        txty0 = Entry(frame_check1, width=1, textvariable=gy0)
        txty0.pack()
        btny0 = Button(frame_check1, text="Calculate y0", command=gety0)
        btny0.pack()

        gx = StringVar()  # we will take the string of

        # user's command for x from here
        def getx():  # function called
            # if the new value was entered for x
            lblx.configure(text="Got it!")
            list_of_data[2] = gx.get()

        lblx = Label(frame_check1, text="Enter x:")
        lblx.pack()
        txtx = Entry(frame_check1, width=1, textvariable=gx)
        txtx.pack()
        btnx = Button(frame_check1, text="Calculate x", command=getx)
        btnx.pack()

        gnum = StringVar()  # we will take the string

        # of user's command for the number of steps from here
        def getnum():  # function called
            # if the new value was entered for num
            lblnum.configure(text="Got it!")
            list_of_data[3] = gnum.get()

        lblnum = Label(frame_check1, text="Enter number of steps:")
        lblnum.pack()
        txtnum = Entry(frame_check1, width=1, textvariable=gnum)
        txtnum.pack()
        btnnum = Button(frame_check1, text="Calculate number of steps", command=getnum)
        btnnum.pack()

        grid = StringVar()
        def getxgrid():  # function called
            # if the new value was entered for num
            lblgrid1.configure(text="Got it!")
            list_of_data_for_grids[0] = grid.get()

        lblgrid1 = Label(frame_check2, text="Enter x1 for grid sizes:")
        lblgrid1.pack()
        txtgrid1 = Entry(frame_check2, width=1, textvariable=grid)
        txtgrid1.pack()
        btngrid1 = Button(frame_check2, text="Calculate grid #1", command=getxgrid)
        btngrid1.pack()

        grid2 = StringVar()
        def getxgrid2():  # function called
            # if the new value was entered for num
            lblgrid2.configure(text="Got it!")
            list_of_data_for_grids[1] = grid2.get()

        lblgrid2 = Label(frame_check2, text="Enter x2 for grid sizes:")
        lblgrid2.pack()
        txtgrid2 = Entry(frame_check2, width=1, textvariable=grid2)
        txtgrid2.pack()
        btngrid2 = Button(frame_check2, text="Calculate grid #1", command=getxgrid2)
        btngrid2.pack()

    # This checkbutton() function puts all possiblle places
    # to put a tick into the window(here we will define
    # which lines the user wants to be drawn

    def checkbuttons():  # I could not find a solution
        # how to make these fedora1-10 functions universal
        # because they must not have any value as a parameter
        # and an outside counter did not solve the problem
        def fedora1():
            list_of_checkers.append(1)

        check1 = Checkbutton(frame_check1, text='Exact Solution', variable=var1, onvalue=1, offvalue=0, command=fedora1)

        def fedora2():
            list_of_checkers.append(2)

        check2 = Checkbutton(frame_check1, text='Euler Method', variable=var2, onvalue=2, offvalue=0, command=fedora2)

        def fedora3():
            list_of_checkers.append(3)

        check3 = Checkbutton(frame_check1, text='Improved Euler Method', variable=var3, onvalue=3, offvalue=0,
                             command=fedora3)

        def fedora4():
            list_of_checkers.append(4)

        check4 = Checkbutton(frame_check1, text='Runge-Kutta Method', variable=var4, onvalue=4, offvalue=0,
                             command=fedora4)
        check1.pack()
        check2.pack()
        check3.pack()
        check4.pack()

        # here starts the second layer of checkbuttons
        def fedora5():
            list_of_checkers.append(5)

        check5 = Checkbutton(frame_check2, text='Euler Method Error', variable=var5, onvalue=5, offvalue=0,
                             command=fedora5)

        def fedora6():
            list_of_checkers.append(6)

        check6 = Checkbutton(frame_check2, text='Improved Euler Method Error', variable=var6, onvalue=6, offvalue=0,
                             command=fedora6)

        def fedora7():
            list_of_checkers.append(7)

        check7 = Checkbutton(frame_check2, text='Runge-Kutta Method Error', variable=var7, onvalue=7, offvalue=0,
                             command=fedora7)
        check5.pack()
        check6.pack()
        check7.pack()

        def fedora8():
            list_of_checkers.append(8)

        check8 = Checkbutton(frame_check2, text='Euler Method MAX Error', variable=var8, onvalue=8, offvalue=0,
                             command=fedora8)

        def fedora9():
            list_of_checkers.append(9)

        check9 = Checkbutton(frame_check2, text='Improved Euler MAX Method Error', variable=var9, onvalue=9, offvalue=0,
                             command=fedora9)

        def fedora10():
            list_of_checkers.append(10)

        check10 = Checkbutton(frame_check2, text='Runge-Kutta MAX Method Error', variable=var10, onvalue=10, offvalue=0,
                              command=fedora10)
        check8.pack()
        check9.pack()
        check10.pack()

    # this function creates plots in the window
    def plot_drawer(x0, y0, x, num, x1grid, x2grid):
        step = (x - x0) / num
        x1 = x0
        i = 0
        xarr = []
        while i <= num:
            xarr.append(ceilmy(x1))  # here we create a list of numbers to be represented as x-s of the plot
            x1 += step
            i += 1
        xx = np.array(xarr)


        mysol = MySolution(x0, y0, x, num, my_func)  # an object of class MySolution is created
        line1 = MySolution.exact_solution(
            mysol)  # we use computational method and fill a list with obtained exact results

        euler = Euler(x0, y0, x, num, my_func)
        line2 = Euler.euler(
            euler)  # we use computational method and fill a list with obtained results of euler function

        imp_euler = ImprovedEuler(x0, y0, x, num, my_func)
        line3 = ImprovedEuler.improved_euler(imp_euler)

        rung_kutt = RungeKutta(x0, y0, x, num, my_func)
        line4 = RungeKutta.runge_kutta(rung_kutt) \
            # this list of functions
        # was supposed to be a solution
        # for useless list creations,
        # but the code would be too redundant because of
        # too much imcludings in checkbuttons' trackers

        # def firstline(line):
        #     mysol = MySolution(x0, y0, x, num, my_func)
        #     line = MySolution.exact_solution(mysol)
        #     return line
        #
        # def secondline(line):
        #     euler = Euler(x0, y0, x, num, my_func)
        #     line = Euler.euler(euler)
        #     return line
        #
        #
        # def thirdline(line):
        #     imp_euler = Improved_Euler(x0, y0, x, num, my_func)
        #     line = Improved_Euler.improved_euler(imp_euler)
        #     return line
        #
        # def fourthline(line):
        #     rung_kutt = Runge_Kutta(x0, y0, x, num, my_func)
        #     line = Runge_Kutta.runge_kutta(rung_kutt)
        #     return line

        f = Figure(figsize=(6, 4), dpi=100)
        a = f.add_subplot(111)
        a.set(title="Numerical Methods")

        if 1 in list_of_checkers:
            # line1 = firstline(line1)                                  #here those functions could be possibly used
            a.plot(xx, line1, label='Exact Solution', color='indigo')

        if 2 in list_of_checkers:
            # line2 = secondline(line2)
            a.plot(xx, line2, label='Eulers Method', color='seagreen')

        if 3 in list_of_checkers:
            # line3 = thirdline(line3)
            a.plot(xx, line3, label='Improved Eulers Method', color='royalblue')

        if 4 in list_of_checkers:
            # line4 = fourthline(line4)
            a.plot(xx, line4, label='Runge-Kutta Method', color='darkorange')

        if 1 in list_of_checkers or 2 in list_of_checkers or 3 in list_of_checkers or 4 in list_of_checkers:
            # we check the nesessity to have labels
            # (if at least one tick was put here)
            a.legend()
        canvas = FigureCanvasTkAgg(f, master=frame_plot)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tkinter.BOTH, expand=3)

        i = 0
        error1 = []
        error2 = []
        error3 = []










        # here is a creation or not for arrays

        # if 5 in list_of_checkers and (line1 == [] or line2 == []):
        #     if (line1 == []):
        #         line1 = firstline(line1)
        #     else:
        #         line2 = secondline(line2)
        # if 6 in list_of_checkers and (line1 == [] or line3 == []):
        #     if (line1 == []):
        #         line1 = firstline(line1)
        #     else:
        #         line3 = thirdline(line3)
        # if 7 in list_of_checkers and (line1 == [] or line4 == []):
        #     if(line1 == []):
        #         line1 = firstline(line1)
        #     else:
        #         line4 = fourthline(line4)

        # while i <= num:
        #     if line1 != [] and line2 != []:
        #         error1.append(abs(line1[i] - line2[i]))
        #     if line1 != [] and line3 != []:
        #         error2.append(abs(line1[i] - line3[i]))
        #     if line1 != [] and line4 != []:
        #         error3.append(abs(line1[i] - line4[i]))
        #     i += 1
        error4 = []
        error5 = []
        error6 = []




        ilast = xarr[0]
        necessarypoint = xarr[len(xarr) - 1]
        for i in xarr:
            if i < x1grid:
                ilast = i
            elif i > x1grid and i < x2grid:
                necessarypoint = i

        for i in range(xarr.index(ilast), xarr.index(necessarypoint)):
            if line1 != [] and line2 != []:
                error1.append(abs(line1[i] - line2[i]))
            if line1 != [] and line3 != []:
                error2.append(abs(line1[i] - line3[i]))
            if line1 != [] and line4 != []:
                error3.append(abs(line1[i] - line4[i]))
        xarr1 = xarr[xarr.index(ilast): xarr.index(necessarypoint)]
        xx = np.array(xarr1)


        f1 = Figure(figsize=(4, 4), dpi=100)
        a = f1.add_subplot(111)
        a.set(title="Errors on Numerical Methods")
        if 5 in list_of_checkers:
            a.plot(xx, error1, label='Euler Error', color='seagreen')
        if 6 in list_of_checkers:
            a.plot(xx, error2, label='Improved Euler Error', color='royalblue')
        if 7 in list_of_checkers:
            a.plot(xx, error3, label='Runge-Kutta Error', color='darkorange')
        if 5 in list_of_checkers or 6 in list_of_checkers or 7 in list_of_checkers:
            # we check the nesessity to have labels
            # (if at least one tick was put here)
            a.legend()

        canvas = FigureCanvasTkAgg(f1, master=frame_plot2)  # here we plot a second graph into tkinter
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tkinter.BOTH, expand=3, side=LEFT)



        # max = 0.0
        # for i in error1:
        #     if(i > max):
        #         max = i
        #     error4.append(max)

        for i in range(1, len(error1) + 1):
            error4.append(max(error1[:i:]))

        for i in range(1, len(error2) + 1):
            error5.append(max(error2[:i:]))

        for i in range(1, len(error3) + 1):
            error6.append(max(error3[:i:]))

        f2 = Figure(figsize=(4, 4), dpi=100)
        a = f2.add_subplot(111)
        a.set(title="MAX Errors on Numerical Methods")
        if 8 in list_of_checkers:
            a.plot(xx, error4, label='Eulers MAX Error', color='seagreen')
        if 9 in list_of_checkers:
            a.plot(xx, error5, label='Improved Eulers MAX Error', color='royalblue')
        if 10 in list_of_checkers:
            a.plot(xx, error6, label='Runge-Kutta MAX Error', color='darkorange')

        if 8 in list_of_checkers or 9 in list_of_checkers or 10 in list_of_checkers:
            # we check the nesessity to have labels
            # (if at least one tick was put here)
            # or either an error will occur
            a.legend()

        canvas = FigureCanvasTkAgg(f2, master=frame_plot2)  # here we plot a third graph into tkinter
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tkinter.BOTH, expand=3, side=RIGHT)

    labels()
    checkbuttons()
    plot_drawer(x0, y0, x, num, x1grid, x2grid)
    list_of_checkers.clear()
    # list_of_data = ['', '', '', '']
