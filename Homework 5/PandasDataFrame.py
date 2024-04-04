summary=result_pd.groupby('ocean_proximity').agg({
    'median_income':'mean',
    'median_house_value': 'mean',
    'housing_median_age': 'mean'
}).reset_index()
print(summary)
