import matplotlib.pyplot as plt

fig, ax = plt.subplots(num='My canvas')
ax.set_ylim([0, 1])
ax.set_xlim([0, 1])
line = ax.plot([], [], 'r-')[0]

def add_point(event):
    if event.button == 1:
        x, y = map(list, line.get_data())
        x.append(event.xdata)
        y.append(event.ydata)
        line.set_data(x, y)
        fig.canvas.draw()

fig.canvas.mpl_connect('button_press_event', add_point)

plt.show()
