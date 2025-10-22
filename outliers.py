import misvalue as mv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

for feature in mv.numeric_features:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=mv.df[feature])
    plt.title(f"Box Plot of {feature}")
    plt.savefig
    plt.show(block=True)
