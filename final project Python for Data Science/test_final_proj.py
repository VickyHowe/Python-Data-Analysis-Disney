# #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 05 12:32:19 2024

@author: Marie Howe

This function creates data to test the final_proj_cleaning script created for
the final_project for the course: Python Programmign for Data Science.
"""

import pandas as pd
from final_proj_clean_func import clean_movie_data


def test_clean_movie_data():
    # Create a sample DataFrame with NaN values and columns
    data = {
        "movie_title": ["Movie 1", "Movie 2", "Movie 3"],
        "inflation_adjusted_gross": [1000000, None, 2000000],
        "release_date": ["2022-01-01", "2023-01-01", "2024-01-01"],
        "MPAA_rating": ["PG", "PG-13", "R"],
        "total_gross": [1500000, 1800000, 2200000],
    }
    df = pd.DataFrame(data)

    # Call the function to clean the DataFrame
    result = clean_movie_data(df)

    # Check if NaN values are dropped
    assert result.isnull().sum().sum() == 0

    # Check if 'gross_revenue' is converted to int
    assert result["gross_revenue"].dtype == "int64"

    # Check if specified columns are dropped
    assert "release_date" not in result.columns
    assert "MPAA_rating" not in result.columns
    assert "total_gross" not in result.columns
    assert "inflation_adjusted_gross" not in result.columns


test_clean_movie_data()
