import matplotlib.pyplot as plt
import matplotlib.animation as animation
from iris_reader import get_data

data = get_data()  # iris data again
x = [i['sepal_length'] for i in data if i['class'] == 'Iris-setosa']
y = [i['sepal_width'] for i in data if i['class'] == 'Iris-setosa']

fig, ax = plt.subplots(num='Iris setosa')
scatter = ax.plot([], [], 'ko')[0]
ax.set_xlim([4, 6])
ax.set_ylim([2, 4.5])

def update(frame_number):
    scatter.set_data(x[frame_number], y[frame_number])
    return scatter,  # Note the comma!

ani = animation.FuncAnimation(fig, update, range(len(x)),
                              interval=250, blit=True)
plt.show()
