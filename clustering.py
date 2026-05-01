import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def getDataset():
    df = pd.read_csv("dataset_financiero_colombia_1000.csv")
    df.columns = ["name", "age", "income_COP", "expenses_COP"]
    return df

def ApplyClusteringkmeans():
    df = getDataset()
    features = ["age", "income_COP", "expenses_COP"]
    x = df[features]

    scaler = StandardScaler()
    XScaled = scaler.fit_transform(x)

    model = KMeans(n_clusters=3, random_state=42, n_init=10)
    labels = model.fit_predict(XScaled)

    df["cluster"] = labels
    
    
    result = df.to_dict(orient="records")

    summaryClusters = df["cluster"].value_counts().sort_index().to_dict()

    centers_scaled = model.cluster_centers_.tolist()
  
    return {
        "results": result,
        "SummaryClusters": summaryClusters,
        "centers_scaled": centers_scaled,
        "scaler": scaler,
        "model": model,
        "feature_names": features
    }

if __name__ == "__main__":
    final_result = ApplyClusteringkmeans()
    print("Training complete")
    print(f"Group Summary: {final_result['SummaryClusters']}")