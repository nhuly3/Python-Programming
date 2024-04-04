import seaborn as sns
import matplotlib.pyplot as plt

sns.catplot(x="ocean_proximity", y="median_house_value", kind="box", data=result_pd)
plt.xlabel("Ocean Proximity")
plt.ylabel("Median House Value")
plt.title("The Distribution of Median House Value by Ocean Proximity")

plt.show()
