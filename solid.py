#this work was done by Polina Romanenkova
# for de_assignment Computational Practicum
from math import floor

def ceilmy(x):
    return floor(x*100)/100


import matplotlib

matplotlib.use("TkAgg")


# here is the end of import-statements


def my_func(x, y):
    return 1 + 2 * y / x


class ExactSolution:
    def __init__(self, x0, y0, x, num, my_func):
        self.x0 = x0
        self.y0 = y0
        self.x = x
        self.num = num
        self.step = (x - x0) / num
        self.xarray = []
        self.yarray = []
        self.my_func = my_func
        for i in range(0, num + 1):
            self.xarray.append(self.x0 + i * self.step)


class MySolution(ExactSolution):
    def exact_solution(self):
        c1 = self.y0 / self.x0 + 1
        y = []
        x1 = self.x0
        y1 = self.y0
        for i in range(0, self.num + 1):
            y1 = x1 * (c1 * x1 - 1)
            y.append(y1)
            # y.append(y1)
            x1 += self.step
        return y


class NumMethod:
    def __init__(self, x0, y0, x, num, my_func):
        self.x0 = x0
        self.y0 = y0
        self.x = x
        self.num = num
        self.step = (x - x0) / num
        self.xarray = []
        self.yarray = []
        self.my_func = my_func
        for i in range(0, num + 1):
            self.xarray.append(self.x0 + i * self.step)


class Euler(NumMethod):
    def euler(self):
        y = []
        y1 = self.y0  # this is done so that no instance is changed
        # and we can use them later
        y2 = self.y0
        for i in range(0, self.num + 1):
            y.append(y1)
            y1 = y[i] + self.step * self.my_func(self.xarray[i], y[i])
            # y.append(y1) #this step was moved to the beginning of cycle
        return y


class ImprovedEuler(NumMethod):
    def improved_euler(self):
        y = []
        y1 = self.y0
        for i in range(0, self.num + 1):
            y.append(y1)
            deltay = self.step * self.my_func(self.xarray[i] + self.step / 2, y[i] +
                                              self.step / 2 * self.my_func(self.xarray[i], y[i]))
            y1 = y[i] + deltay
        return y


class RungeKutta(NumMethod):
    def runge_kutta(self):
        y = []
        yback = self.y0
        xback = self.x0
        y1 = self.y0
        y2 = self.y0
        for i in range(0, self.num + 1):
            y.append(y1)
            k1i = self.my_func(self.xarray[i], y2)
            k2i = self.my_func(self.xarray[i] + self.step / 2, y2 + self.step / 2 * k1i)
            k3i = self.my_func(self.xarray[i] + self.step / 2, y2 + self.step / 2 * k2i)
            k4i = self.my_func(self.xarray[i] + self.step, y2 + self.step * k3i)
            y1 = y2 + self.step / 6 * (k1i + 2 * k2i + 2 * k3i + k4i)
            # y.append(y1)
            y2 = y1
        return y




#here i checked, whether everything was set correctly

# x0 = 1.0
# y0 = 2.0
# x = 10.0
# num = 10
#
# e = Euler(x0, y0, x, num, my_func)
# e1 = Euler.euler(e)
#
# i = Improved_Euler(x0, y0, x, num, my_func)
# i1 = Improved_Euler.improved_euler(i)
#
# r = Runge_Kutta(x0, y0, x, num, my_func)
# r1 = Runge_Kutta.runge_kutta(r)
#
# ex = MySolution(x0, y0, x, num, my_func)
# ex1 = MySolution.exact_solution(ex)

# for i in ex1:
#     print(i)
# print('\n')
#
# for i in e1:
#     print(i)
# print('\n')
#
# for i in i1:
#     print(i)
# print('\n')
#
# for i in r1:
#     print(i)
# print('\n')


# grid = StringVar()
#         def getxgrid():  # function called
#             # if the new value was entered for num
#             lblnum.configure(text="Got it!")
#             list_of_data_for_grids[1] = grid.get()
#
#         lblnum = Label(frame_check2, text="Enter x1 for grid sizes:")
#         lblnum.pack()
#         txtnum = Entry(frame_check2, width=1, textvariable=grid)
#         txtnum.pack()
#         btnnum = Button(frame_check2, text="Calculate grid #1", command=getxgrid)
#         btnnum.pack()
#
#         grid2 = StringVar()
#         def getxgrid2():  # function called
#             # if the new value was entered for num
#             lblnum.configure(text="Got it!")
#             list_of_data_for_grids[2] = grid2.get()
#
#         lblnum = Label(frame_check2, text="Enter x2 for grid sizes:")
#         lblnum.pack()
#         txtnum = Entry(frame_check2, width=1, textvariable=grid2)
#         txtnum.pack()
#         btnnum = Button(frame_check2, text="Calculate grid #1", command=getxgrid2)
#         btnnum.pack()

# ilast = xarr[0]
        # necessarypoint = 1.0
        # if list_of_data_for_grids[0] != '':
        #     necessarypoint = float(list_of_data_for_grids[0])
        #
        # necessarypoint2 = 10.0
        # if list_of_data_for_grids[1] != '':
        #     necessarypoint2 = float(list_of_data_for_grids[0])
        # for i in xarr:
        #     if i < necessarypoint:
        #         ilast = i
        #     elif i > necessarypoint and i < necessarypoint2:
        #         necessarypoint2 = i

        # for i in range(xarr.index(necessarypoint), xarr.index(necessarypoint2)):
        #     if line1 != [] and line2 != []:
        #         error1.append(abs(line1[i] - line2[i]))
        #     if line1 != [] and line3 != []:
        #         error2.append(abs(line1[i] - line3[i]))
        #     if line1 != [] and line4 != []:
        #         error3.append(abs(line1[i] - line4[i]))
        # xarr = xarr[xarr.index(necessarypoint): xarr.index(necessarypoint2)]
        # xx = np.array(xarr)