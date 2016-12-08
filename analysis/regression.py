import matplotlib.pyplot as plt
import datetime
from sklearn.svm import SVR

from util.data_io import load_csv


def svr(df):
    # Use only one feature
    df_X = df.distance_from_central.values
    df_X = df_X.reshape(len(df_X), 1)

    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
    svr_lin = SVR(kernel='linear', C=1e3)
    y_rbf = svr_rbf.fit(df_X, df.stars.values).predict(df_X)
    print("RBF DONE: {}".format(datetime.datetime.now()))
    y_lin = svr_lin.fit(df_X, df.stars.values).predict(df_X)
    print("LINEAR DONE: {}".format(datetime.datetime.now()))

    # Plotting
    lw = 2
    fig = plt.scatter(df_X, df.stars.values, color='darkorange', label='data')
    plt.hold('on')
    plt.plot(df_X, y_rbf, color='navy', lw=lw, label='RBF model')
    plt.plot(df_X, y_lin, color='c', lw=lw, label='Linear model')
    plt.xlabel('Distance from central Las Vegas')
    plt.ylabel('Average stars')
    plt.title('Support Vector Regression')
    plt.legend()
    plt.show()
    fig.figure.savefig('../project_data/stars vs distance.png')


def random_forest(df):
    from sklearn.ensemble import RandomForestRegressor
    features = df.distance_from_central.values
    features = features.reshape(len(features), 1)
    labels = df.stars.values
    model = RandomForestRegressor(n_estimators=10, max_features=1)
    model.fit(features, labels)

    plt.scatter(features, df.stars.values, color='darkorange', label='data')
    plt.plot(features, model.predict(features))
    plt.show()


def group_by_distance(df):
    """
    Ugly way of filtering and grouping by distance.
    Pandas doesnt seem to allow returning a groupby object from a filter operation, therefore code makes the call twice
    """
    grouped_df = df.groupby('distance_from_central', as_index=False)
    grouped_df = grouped_df.filter(lambda x: len(x) > 10)
    grouped_df = grouped_df.groupby('distance_from_central', as_index=False)
    grouped_df = grouped_df['stars'].mean()
    return grouped_df


def t_test(df):
    from scipy.stats import ttest_ind
    print(ttest_ind(df.stars, df.distance_from_central))


if __name__ == '__main__':
    df = load_csv("distance_col_yelp_business.csv")
    df = df[df['review_count'] > 25]  # Filter low review counts
    df = group_by_distance(df)
    t_test(df)
    svr(df)
    # random_forest(df)
