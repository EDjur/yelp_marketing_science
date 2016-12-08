import pandas as pd
from util.data_io import load_csv, export_csv, read_colnames_txtfile

pd.set_option('display.width', 1000)


def subset_columns(df):
    colnames = read_colnames_txtfile("../project_data/yelp_business_revelant_colnames.txt")
    new_df = df.select(lambda col: col in colnames, axis=1)
    return new_df


def only_restaurants(df):
    df = df[df.categories.str.contains('Restaurants')]
    return df.reset_index()

def only_las_vegas(df):
    df = df[df.city == "Las Vegas"]
    return df.reset_index()


if __name__ == '__main__':
    df = load_csv("yelp_business.csv")
    df = only_las_vegas(df)
    df = subset_columns(df)
    df = only_restaurants(df)
    del df['level_0']
    print(df)
    export_csv(df, "relevant_cols_only_restaurants.csv")
