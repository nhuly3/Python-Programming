sns.lmplot(x="median_income",
           y="median_house_value",
           col="ocean_proximity",
           hue="ocean_proximity",
           data=result_pd,
           palette="viridis",
           scatter_kws={'s':10, 'color':'orange'},
           line_kws={"color":"blue"})

plt.title("The Correlation between Median Income and Median House Value by Ocean Proximity")

plt.show()
