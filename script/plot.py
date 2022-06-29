import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


class Plot:
    def plotly_plot_pie(df, column, limit=None, title=None):
        a = pd.DataFrame({'count': df.groupby([column]).size()}).reset_index()
        a = a.sort_values("count", ascending=False)
        if limit:
            a.loc[a['count'] < limit, column] = f'Other {column}s'
        if title == None:
            title=f'Distribution of {column}'
            fig = px.pie(a, values='count', names=column, title=title, width=800, height=500)
            fig.show()

    def plot_hist(df:pd.DataFrame, column:str, color:str='cornflowerblue')->None:
        sns.displot(data=df, x=column, color=color, kde=True, height=6, aspect=2)
        plt.title(f'Distribution of {column}', size=20, fontweight='bold')
        plt.show()

    def plot_count(df:pd.DataFrame, column:str) -> None:
        plt.figure(figsize=(12, 7))
        sns.countplot(data=df, x=column)
        plt.title(f'Distribution of {column}', size=20, fontweight='bold')
        plt.show()
    
    
    def plotly_plot_scatter(df, x_col, y_col, marker_size, hover=[]):
        fig = px.scatter(
            df,
            x=x_col,
            y=y_col,
            opacity=0.8,
            hover_data=hover,
            title=f'{x_col} vs. {y_col}')
        fig.update_traces(marker_size=marker_size)
        fig.show()
    
