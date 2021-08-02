from os import name
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from matplotlib.pyplot import yticks

# Load in dataset
def dataload():

    url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
    names = ["sepal-length", "sepal-width", "petal-length", "petal-width", "class"]
    dataset = read_csv(url, names=names)
    return dataset


# returns dataset attributes
def databarf(dataset):
    # shape of dataset (# of instances, # of attributes)
    print(dataset.shape, "\n")

    # head of dataset | dataset.head(# of rows)
    print(dataset.head(20))
    print()

    # descriptions of dataset in centimeters (includes count, mean, min, and max values)
    print(dataset.describe())
    print()

    # class distribution (# of rows belonging to each class)
    print(dataset.groupby("class").size())
    print()


# Univariate plots
# Box and whisker plot
def dataplot(dataset):
    dataset.plot(kind="box", subplots=True, layout=(2, 2), sharex=False, sharey=False)
    pyplot.show()


# Histogram
def datahist(dataset):
    dataset.hist()
    pyplot.show()


# Multivariate plot
# Scatter matrix plot
def datascat(dataset):
    scatter_matrix(dataset)
    pyplot.show()


# Throw all forms of data
def datathrow(dataset):
    databarf(dataset=dataset)
    dataplot(dataset=dataset)
    datahist(dataset=dataset)
    datascat(dataset=dataset)


if __name__ == "dataload":
    dataload()

if __name__ == "databarf":
    data = dataload()
    databarf(data)

if __name__ == "dataplot":
    dataload()
    dataplot(data)

if __name__ == "datahist":
    dataload()
    datahist(data)

if __name__ == "datascat":
    dataload()
    datascat(data)

if __name__ == "datathrow":
    dataload()
    datathrow()
