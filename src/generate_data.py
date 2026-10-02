import pandas as pd 
from sklearn.datasets import load_iris 

iris = load_iris(as_frame=True)
df = iris.frame 

df.to_csv("data/raw/iris_v1.csv", index=False)
print(f"Saved {len(df)} rows to data/raw/iris_v1.csv") 

augmented = df.copy()

augmented.to_csv("data/raw/iris_v1.csv", index=False)

print(f"Dataset now has {len(augmented)} rows")