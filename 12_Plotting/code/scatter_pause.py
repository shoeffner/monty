import matplotlib.pyplot as plt
from iris_reader import get_data

data = get_data()  # iris data again
x = [i['sepal_length'] for i in data if i['class'] == 'Iris-setosa']
y = [i['sepal_width'] for i in data if i['class'] == 'Iris-setosa']

fig, ax = plt.subplots(1, 1, num='Iris setosa')
scatter = ax.plot([], [], 'ko')[0]
ax.set_xlim([4, 6])
ax.set_ylim([2, 4.5])

plt.ion()
plt.show()

for xi, yi in zip(x, y):
    scatter.set_data(xi, yi)  # Set data
    fig.canvas.draw()  # Update complete canvas
    plt.pause(0.25)  # Pause until next frame
