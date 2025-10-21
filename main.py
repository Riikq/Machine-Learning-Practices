import pandas as pd

test = pd.read_csv("test.csv")
# print(test.head())

train = pd.read_csv("train.csv")
# print(train.head())

# print(train.info())
# print(train.describe(include="all"))

missing_values = train.isnull().sum()
# print(missing_values[missing_values > 0])

less = missing_values[missing_values < 1000].index
over = missing_values[missing_values >= 1000].index

numeric_features = train[less].select_dtypes(include=["number"]).columns
train[numeric_features] = train[numeric_features].fillna(
    train[numeric_features].median()
)

kategorical_features = train[less].select_dtypes(include=["object"]).columns
for column in kategorical_features:
    train[column] = train[column].fillna(train[column].mode()[0])

df = train.drop(columns=over)

missing_values = df.isnull().sum()
print(missing_values[missing_values > 0])
