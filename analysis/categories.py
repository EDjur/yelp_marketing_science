from util.data_io import load_csv


def calculate_unique(df):
    test = set()

    test_list = []
    category_index = df.columns.get_loc('categories')
    for index, row in df.iterrows():
        for category in row[category_index]:
            test_list.append(category)
        print(row[category_index])









if __name__ == '__main__':
    df = load_csv("distance_col_yelp_business.csv")
    df = calculate_unique(df)
