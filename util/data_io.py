import pandas as pd


def load_csv(filename):
    return pd.read_csv("../data/{}".format(filename), encoding='ISO-8859-1')


def export_csv(df, filename="filename"):
    df.to_csv(path_or_buf="../data/{}".format(filename), index=False)


def read_colnames_txtfile(filename):
    with open(filename) as f:
        content = f.readlines()
        content = [line.rstrip('\n') for line in content]
    return content