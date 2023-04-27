import pandas as pd
import os


class DatasetAnalysis:
    zeros_in_columns = []
    def __init__(self, df):
        self.df = df
        self.df_length = len(df)
        self.df_columns = list(df.columns)

    def get_zeros(self):
        for column in self.df_columns:
            df[column].append()


if __name__ == '__main__':
    cwd = os.getcwd()
    dataset = pd.read_excel(os.path.join(cwd, 'erp_ordens_producao.xlsx'), index_col=0)
    dataAnalytics_erp_ordens_producao = DatasetAnalysis(dataset)
    print(dataAnalytics_erp_ordens_producao.df_length)
    print(dataAnalytics_erp_ordens_producao.df_columns)

