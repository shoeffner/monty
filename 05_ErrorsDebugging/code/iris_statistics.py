"""
Prints some statistics about the iris data set.
"""
import csv
import os
import statistics


IRIS_FILE = 'iris.csv'
SEPAL_LENGTH = 'sepal length in cm'
SEPAL_WIDTH = 'sepal width in cm'
PETAL_LENGTH = 'petal length in cm'
PETAL_WIDTH = 'petal width in cm'
CLASS = 'class'


def read_with_csv(filename):
    """Reads the iris file using the csv module.

    Args:
        filename: The filename.

    Returns:
        A list of dictionaries mapping the features to their values.
    """
    with open(filename, 'r') as iris_file:
        reader = csv.DictReader(iris_file, [SEPAL_LENGTH, SEPAL_WIDTH,
                                            PETAL_LENGTH, PETAL_WIDTH, CLASS])
        return list(reader)


def read_without_csv(filename):
    """Reads the iris file without using the csv module.

    Args:
        filename: The filename.

    Returns:
        A list of dictionaries mapping the features to their values.
    """
    data = []
    with open(filename, 'r') as iris_file:
        for line in iris_file.read().splitlines()[:-1]:
            features = line.split(',')
            data.append({SEPAL_LENGTH: features[0], SEPAL_WIDTH: features[1],
                         PETAL_LENGTH: features[2], PETAL_WIDTH: features[3],
                         CLASS: features[4]})
    return data


def make_data_numeric(data, *features):
    """For each entry in data, all features in features are cast to float.

    Args:
        data: The dataset to modify.
        features: The features to cast to float.
    """
    for date in data:
        for feature in features:
            date[feature] = float(date[feature])
    return data


def count_occurences(data, feature):
    """Counts how often each unique value of a feature occurs in the whole
    dataset.

    Args:
        data: The dataset to count.
        feature: The feature to count.

    Returns:
        A dictionary where the keys are the data values and the values are the
        occurences.
    """
    values = [d[feature] for d in data]
    return {k: values.count(k) for k in set(values)}


def mean(values):
    """Returns the mean of the values.

    Args:
        Values: A list of values.

    Returns:
        The mean.
    """
    return sum(values) / len(values)


def median(values):
    """Returns the median of the values.

    Args:
        Values: A list of values.

    Returns:
        The median.
    """
    idx = len(values) // 2
    if len(values) & 1:
        return sorted(values)[idx]
    else:
        return mean(sorted(values)[idx - 1:idx + 1])


def mode(values):
    """Returns the mode of the values.

    If multiples values tie, one value is returned.

    Args:
        values: A list of values.

    Returns:
        The mode.
    """
    counts = {k: values.count(k) for k in set(values)}
    return sorted(counts, key=counts.__getitem__)[-1]


def test():
    """Tests the statistical functions.

    Raises:
        AssertionError if a test fails.
    """
    testlist0 = [1, 2, 3, 4, 5]
    testlist1 = [1, 2, 3, 4, 5, 6]
    testlist2 = [2, 2, 3, 4, 4, 6]
    testlist3 = [2, 2, 3, 4, 5, 6, 7]

    assert mean(testlist0) - 5 <= 1e-6, mean(testlist0)
    assert mean(testlist1) - 3.5 <= 1e-6, mean(testlist1)
    assert mean(testlist2) - 21 / 6 <= 1e-6, mean(testlist2)
    assert mean(testlist3) - 29 / 7 <= 1e-6, mean(testlist3)

    assert median(testlist0) == 3, median(testlist0)
    assert median(testlist1) - 3.5 <= 1e-6, median(testlist1)
    assert median(testlist2) - 3.5 <= 1e-6, median(testlist2)
    assert median(testlist3) == 4, median(testlist3)

    assert mode(testlist3) == 2, mode(testlist3)


def main(with_csv=False):
    """Performs some simple data analysis.

    If with_csv is True, the csv module is used for loading the data.
    Otherwise, a simple custom solution is used.

    Args:
        with_csv: If True, uses the csv module.
    """
    if with_csv:
        data = read_with_csv(IRIS_FILE)
    else:
        data = read_without_csv(IRIS_FILE)

    data = make_data_numeric(data, SEPAL_LENGTH, SEPAL_WIDTH,
                             PETAL_LENGTH, PETAL_WIDTH)

    print('Total number of rows:', len(data))

    class_counts = count_occurences(data, CLASS)
    print('Instances:', class_counts)

    sepal_lengths = [d[SEPAL_LENGTH] for d in data]
    print('Mean sepal length (statistics):', statistics.mean(sepal_lengths))
    print('Mean sepal length (custom):', mean(sepal_lengths))

    sepal_l_setosa = [d[SEPAL_LENGTH] for d in data if 'setosa' in d[CLASS]]
    print('Mean sepal length (setosa, statistics):',
          statistics.mean(sepal_l_setosa))
    print('Mean sepal length (setosa, custom):', mean(sepal_l_setosa))

    sepal_widths = [d[SEPAL_WIDTH] for d in data]
    print('Median sepal width (statistics):', statistics.median(sepal_widths))
    print('Median sepal width (custom):', median(sepal_widths))

    sepal_w_virginica = [d[SEPAL_WIDTH] for d in data if 'vir' in d[CLASS]]
    print('Median sepal width (virginica, statistics):',
          statistics.median(sepal_w_virginica))
    print('Median sepal width (virginica, custom):', median(sepal_w_virginica))

    petal_l_versicolor = [d[PETAL_LENGTH] for d in data if 'ver' in d[CLASS]]
    print('Mode petal length (versicolor, statistics):',
          statistics.mode(petal_l_versicolor))
    print('Mode petal length (versicolor, custom):', mode(petal_l_versicolor))


if __name__ == '__main__':
    test()
    main(False)
