# ZADANIE 3: Normalizacja
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = iris.target

plt.figure(figsize=(8,6))
sns.scatterplot(x=df["sepal length (cm)"], y=df["sepal width (cm)"], hue=df["species"], palette="Set1")
plt.title("Oryginalne dane")
plt.show()

scaler = MinMaxScaler()
df_scaled = df.copy()
df_scaled.iloc[:, :-1] = scaler.fit_transform(df.iloc[:, :-1])
plt.figure(figsize=(8,6))
sns.scatterplot(x=df_scaled["sepal length (cm)"], y=df_scaled["sepal width (cm)"], hue=df_scaled["species"], palette="Set1")
plt.title("Min-Max Scaling")
plt.show()

scaler = StandardScaler()
df_standardized = df.copy()
df_standardized.iloc[:, :-1] = scaler.fit_transform(df.iloc[:, :-1])
plt.figure(figsize=(8,6))
sns.scatterplot(x=df_standardized["sepal length (cm)"], y=df_standardized["sepal width (cm)"], hue=df_standardized["species"], palette="Set1")
plt.title("Z-score Scaling")
plt.show()