from util.data_io import load_csv, export_csv
import numpy as np
import math

CENTRAL_LAS_VEGAS = [36.114679, -115.172834]  # Center of 'The Strip' as specified by Google Maps





def calculate_distance(lat, long):
    """
    Distance is defined as the euclidean distance between point (x,y) and (a,b).
    This is sufficient for this purpose as I am only looking at one city and do not need to take into account e.g. earth's curvature
    As I am unfamiliar with the road network and transportation links, only absolute distance will be used.
    d = sqrt( |a - x|^2 + |b - y|^2 )
    :param lat: latitude of restaurant
    :param long: longitude of restaurant
    :return: the absolute Pythagoras distance from "CENTRAL_LAS_VEGAS" as defined above
    """

    distance = round(np.sqrt(abs(lat - CENTRAL_LAS_VEGAS[0])**2 + abs(long - CENTRAL_LAS_VEGAS[1])**2) * 100, 0)
    return distance


def add_distance_col(df):
    """
    Aerial distance from "CENTRAL_LAS_VEGAS" is added as a column to the dataframe
    :param df: pandas dataframe that contains the filtered yelp data
    :return: new df with the added column for distance from "CENTRAL_LAS_VEGAS"
    """

    df['distance_from_central'] = calculate_distance(df['latitude'], df['longitude'])
    return df


if __name__ == '__main__':
    df = load_csv("relevant_cols_only_restaurants.csv")
    df = add_distance_col(df)
    export_csv(df, "distance_col_yelp_business.csv")
