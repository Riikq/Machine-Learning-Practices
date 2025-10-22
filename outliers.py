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

Q1 = mv.df[mv.numeric_features].quantile(0.25)
Q3 = mv.df[mv.numeric_features].quantile(0.75)
IQR = Q3 - Q1

condition = ~(
    (mv.df[mv.numeric_features] < (Q1 - 1.5 * IQR))
    | (mv.df[mv.numeric_features] > (Q3 + 1.5 * IQR))
).any(axis=1)

categorical_features = mv.df.select_dtypes(include=["object"]).columns
df = pd.concat(
    [mv.df_filtered_numeric, mv.df.loc[condition, categorical_features]], axis=1
)
