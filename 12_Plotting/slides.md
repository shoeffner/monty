% Plotting


# Plotting

```{ .python .exec .plt .hideimports }
import matplotlib.pyplot as plt

plt.plot([1, 2, 3])
```


# Plotting libraries

- `ggplot`:  http://ggplot.yhathq.com
- `matplotlib`: https://matplotlib.org
- `vtk`: http://www.vtk.org

\note{
- ggplot is close to R's ggplot2 library
- matplotlib started out as a project to mimic MATLAB's plotting capabilities
- vtk is a library for 3D plots

We focus on matplotlib.
}


# Plotting data

```{ .python .exec .plt }
import matplotlib.pyplot as plt

y = [x ** 2 for x in range(5)]
plt.plot(y)
```

*Important*: `plt.show()`!

\note{
If you only supply one argument to `plot()`, it uses x from `0` to `N - 1` and
assumes the data as `y` values.

For my automatic slide generation I had to leave out the call to `plt.show()`,
which actually brings up the figure where we plot to. You have to add it
whenever you want to see what you plotted.
}


# Plotting data

```{ .python .exec .plt }
import matplotlib.pyplot as plt

x = range(-4, 5)
y = [i ** 2 for i in x]
plt.plot(x, y)
```


# Adding labels

```{ .python .exec .plt .hideimports }
import matplotlib.pyplot as plt

x = range(-4, 5)
y = [i ** 2 for i in x]
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('$x^2$')
```

\note{
Please note that for space reasons I remove the imports from now on. It's `import matplotlib.pyplot as plt`.

`pyplot` (which is our `plt`) always refers to the last active plot when making changes. We will see later, why this is important.

Matplotlib supports LaTeX math formulae for many labels, e.g. titles.
}


# Adding labels

```{ .python .exec .plt .hideimports }
import matplotlib.pyplot as plt

x = range(-4, 5)
y = [i ** 2 for i in x]
plt.plot(x, y)
plt.title(r'$x \rightarrow x^2$')
```


# Getting a data set

Iris Data set [@fisher1936]:

```{ .python wd=12_Plotting/code }
import requests
with open('iris.data', 'w') as iris:
    iris.write(requests.get(
        'https://archive.ics.uci.edu/ml/' +
        'machine-learning-databases/iris/iris.data'
        ).text)
```


# Reading iris data

\scriptsize

```{ .python wd=12_Plotting/code file=iris_reader.py .exec .hideimports }
```

\normalsize


# Plotting iris data

```{ .python wd=12_Plotting/code .exec .hideimports .plt }
import matplotlib.pyplot as plt
from iris_reader import get_data

y = [i['sepal_length'] for i in get_data()]
plt.plot(y)
plt.ylabel('sepal length')
```

\note{
It makes not much sense to just plot the sepal lengths. Let's plot it in relation to something.
}


# Plotting iris data

\small

```{ .python wd=12_Plotting/code .exec .hideimports .plt }
import matplotlib.pyplot as plt
from iris_reader import get_data

data = get_data()
x = [i['sepal_length'] for i in data]
y = [i['sepal_width'] for i in data]
plt.plot(x, y)
plt.xlabel('sepal length')
plt.ylabel('sepal width')
```

\normalsize

\note{
This still doesn't seem right, what should we change?
}


# Scatter plots

\small

```{ .python wd=12_Plotting/code .exec .hideimports .plt }
import matplotlib.pyplot as plt
from iris_reader import get_data

data = get_data()
x = [i['sepal_length'] for i in data]
y = [i['sepal_width'] for i in data]
plt.scatter(x, y)
plt.xlabel('sepal length')
plt.ylabel('sepal width')
```

\normalsize



# References
