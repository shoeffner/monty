"""
Prints some statistics about the iris data set.
"""
import csv


IRIS_FILE = '05_ErrorsDebugging/code/iris.csv'
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
    if len(values) & 2:
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
    mean_sepal_length = mean(sepal_lengths)
    print('Mean sepal length:', mean_sepal_length)

    sepal_l_setosa = [d[SEPAL_LENGTH] for d in data if 'setosa' in d[CLASS]]
    mean_sepal_l_setosa = mean(sepal_l_setosa)
    print('Mean sepal length (setosa):', mean_sepal_l_setosa)

    sepal_widths = [d[SEPAL_LENGTH] for d in data]
    median_sepal_width = median(sepal_widths)
    print('Median sepal width:', median_sepal_width)

    sepal_w_virginica = [d[SEPAL_LENGTH] for d in data if 'vir' in d[CLASS]]
    median_sepal_w_virginica = median(sepal_w_virginica)
    print('Median sepal width (virginica):', median_sepal_w_virginica)

    petal_lengths = [d[PETAL_LENGTH] for d in data]
    mode_petal_length = mode(petal_lengths)
    print('Mode petal length:', mode_petal_length)  # @shoeffner: 1.4 or 1.5


if __name__ == '__main__':
    main(False)
