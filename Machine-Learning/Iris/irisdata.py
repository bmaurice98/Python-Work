from pandas import read_csv


def data():
    # Load in dataset
    url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
    names = ["sepal-length", "sepal-width", "petal-length", "petal-width", "class"]
    dataset = read_csv(url, names=names)

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


if __name__ == "data":
    data()
