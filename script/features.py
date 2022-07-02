import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler

#prepare data for modelling
def feature_scaling(data:pd.DataFrame,col1:str):
    le = LabelEncoder()
    
    data[col1] = le.fit_transform(data[col1])
    
    cols = data.columns.to_list()
    if col1 in cols:
        cols.remove(col1)
        
    scaled_features = data.copy()
    features = scaled_features[cols]
    scaler = StandardScaler()

    scaled_features[cols] = scaler.fit_transform(features.values)
    return scaled_features