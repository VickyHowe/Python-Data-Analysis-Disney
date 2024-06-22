#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 05 12:32:19 2024

@author: Marie Howe

"""

import pandas as pd


def clean_movie_data(df):
    """
        Cleans movie data by performing the following steps:
        1. Checks if the input is a DataFrame.
        2. Drops rows with NaN values.
        3. Converts 'inflation_adjusted_gross' to integer format,
                     removing '$' and ',' characters.
        4. Drops columns 'release_date',
                         'MPAA_rating',
                         'total_gross',
                          and 'inflation_adjusted_gross'.

        Parameters:
        df (DataFrame): Input DataFrame containing movie data.

        Returns:
        DataFrame: Cleaned DataFrame without NaN values,
        with 'gross_revenue' as int, and specified columns dropped.

        Raises:
        TypeError: If the input argument df is not of type DataFrame.

        AssertionError:
            - If 'genre' column does not exist in the DataFrame.
            - If 'inflation_adjusted_gross' column does not exist in the DataFrame.

        Example:
        >>> clean_movie_data(df)
        movie_title genre 	gross_revenue
    0 	Snow White 	Musical 	5228953251
    1 	Pinocchio 	Adventure 	2188229052
    2 	Fantasia 	Musical 	2187090808
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("The data is not of type DataFrame")

    assert "genre" in df.columns, "The genre column does not exist in the dataframe"
    assert (
        "inflation_adjusted_gross" in df.columns
    ), "The inflation_adjusted_gross column does not exist in the dataframe"

    cleaned_df = (
        df.dropna()
        .assign(
            gross_revenue=lambda x: x["inflation_adjusted_gross"]
            .replace({"\$": "", ",": ""}, regex=True)
            .astype(int)
        )
        .drop(
            columns=[
                "release_date",
                "MPAA_rating",
                "total_gross",
                "inflation_adjusted_gross",
            ]
        )
    )

    return cleaned_df
