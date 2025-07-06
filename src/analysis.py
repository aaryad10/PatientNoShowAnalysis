class Analyzer:
    def calculate_dropout_rate(self, df):
        total = len(df)
        dropouts = df['No-show'].sum()
        dropout_rate = (dropouts / total) * 100
        return round(dropout_rate, 2)

    def calculate_gender_distribution(self, df):
        return df['Gender'].value_counts(normalize=True) * 100
