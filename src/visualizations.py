# #all visualizations -- data preparing -- dropout by age, gender weekday, neighborhood, time slot -- correlation heatmap.

# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd

# class Visualizer:
#     def __init__(self, df):
#         self.df = df.copy()
#         self._prepare_data()

#     def _prepare_data(self):
#         self.df.columns = [col.strip().lower().replace('-', '_') for col in self.df.columns]

#         if 'no_show' in self.df.columns:
#             if self.df['no_show'].dtype == object:
#                 self.df['no_show'] = self.df['no_show'].map({'Yes': 1, 'No': 0, 'yes': 1, 'no': 0}).fillna(self.df['no_show'])
#             self.df['no_show'] = pd.to_numeric(self.df['no_show'], errors='coerce')

#         if 'gender' in self.df.columns:
#             unique_genders = self.df['gender'].unique()
#             if set(unique_genders).issubset({0, 1}):
#                 self.df['gender_label'] = self.df['gender'].map({0: 'Male', 1: 'Female'})
#             elif set(unique_genders).issubset({'M', 'F'}):
#                 self.df['gender_label'] = self.df['gender'].map({'M': 'Male', 'F': 'Female'})
#             else:
#                 self.df['gender_label'] = self.df['gender']

#         if 'appointmentday' in self.df.columns:
#             self.df['appointmentday'] = pd.to_datetime(self.df['appointmentday'], errors='coerce')

#         if 'scheduledday' in self.df.columns:
#             self.df['scheduledday'] = pd.to_datetime(self.df['scheduledday'], errors='coerce')
#             self.df['scheduledhour'] = self.df['scheduledday'].dt.hour
#             self.df['time_slot'] = self.df['scheduledhour'].apply(self.time_of_day)

#     def time_of_day(self, hour):
#         if pd.isnull(hour):
#             return 'Unknown'
#         if 6 <= hour < 12:
#             return 'Morning'
#         elif 12 <= hour < 17:
#             return 'Afternoon'
#         elif 17 <= hour < 21:
#             return 'Evening'
#         else:
#             return 'Night'

#     def plot_dropout_by_age(self):
#         if 'age' not in self.df.columns or 'no_show' not in self.df.columns:
#             return None

#         bins = [0, 12, 18, 30, 45, 60, 75, 100]
#         labels = ['Child', 'Teen', 'Young Adult', 'Adult', 'Middle Age', 'Senior', 'Elderly']
#         self.df['age_group'] = pd.cut(self.df['age'], bins=bins, labels=labels)

#         dropout_by_age = self.df.groupby('age_group')['no_show'].mean().reset_index()
#         dropout_by_age['dropout_rate'] = dropout_by_age['no_show'] * 100

#         fig, ax = plt.subplots()
#         sns.barplot(data=dropout_by_age, x='age_group', y='dropout_rate', palette='magma', ax=ax)
#         plt.xticks(rotation=45)
#         plt.ylabel('Dropout Rate (%)')
#         plt.grid(axis='y', linestyle='--', alpha=0.5)
#         plt.title('No-show Rate by Age Group')
#         return fig

#     def plot_dropout_by_weekday(self):
#         if 'appointmentday' not in self.df.columns or 'no_show' not in self.df.columns:
#             return None

#         self.df['weekday'] = self.df['appointmentday'].dt.day_name()
#         dropout_by_day = self.df.groupby('weekday')['no_show'].mean().reset_index()
#         dropout_by_day['dropout_rate'] = dropout_by_day['no_show'] * 100

#         weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#         dropout_by_day['weekday'] = pd.Categorical(dropout_by_day['weekday'], categories=weekday_order, ordered=True)
#         dropout_by_day = dropout_by_day.sort_values('weekday')

#         fig, ax = plt.subplots()
#         sns.barplot(data=dropout_by_day, x='weekday', y='dropout_rate', palette='magma', ax=ax)
#         plt.xticks(rotation=45)
#         plt.ylabel('Dropout Rate (%)')
#         plt.grid(axis='y', linestyle='--', alpha=0.5)
#         plt.title('No-show Rate by Weekday')
#         return fig

#     def plot_dropout_by_gender(self):
#         if 'gender_label' not in self.df.columns or 'no_show' not in self.df.columns:
#             return None

#         dropout_by_gender = self.df.groupby('gender_label')['no_show'].mean().reset_index()
#         dropout_by_gender['dropout_rate'] = dropout_by_gender['no_show'] * 100

#         fig, ax = plt.subplots()
#         sns.barplot(data=dropout_by_gender, x='gender_label', y='dropout_rate', palette='magma', ax=ax)
#         plt.ylabel('Dropout Rate (%)')
#         plt.grid(axis='y', linestyle='--', alpha=0.5)
#         plt.title('No-show Rate by Gender')
#         return fig

#     def plot_correlation_heatmap(self):
#         numeric_df = self.df.select_dtypes(include=['number'])
#         if numeric_df.empty:
#             return None

#         corr_matrix = numeric_df.corr()

#         fig, ax = plt.subplots(figsize=(12, 8))
#         sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, ax=ax)
#         plt.title('Correlation Heatmap')
#         plt.xticks(rotation=45)
#         plt.yticks(rotation=0)
#         plt.tight_layout()
#         return fig

#     def plot_dropout_by_neighborhood(self):
#         if 'neighbourhood' not in self.df.columns or 'no_show' not in self.df.columns:
#             return None

#         top_neighborhoods = self.df['neighbourhood'].value_counts().head(10).index
#         df_top = self.df[self.df['neighbourhood'].isin(top_neighborhoods)]

#         dropout_by_neighborhood = df_top.groupby('neighbourhood')['no_show'].mean().reset_index()
#         dropout_by_neighborhood['dropout_rate'] = dropout_by_neighborhood['no_show'] * 100

#         fig, ax = plt.subplots(figsize=(6, 4))
#         sns.barplot(data=dropout_by_neighborhood, x='neighbourhood', y='dropout_rate', palette='magma', ax=ax)
#         plt.title('No-show Rate by Top 10 Neighborhoods')
#         plt.ylabel('Dropout Rate (%)')
#         plt.xlabel('Neighborhood')
#         plt.xticks(rotation=45)
#         plt.grid(axis='y', linestyle='--', alpha=0.5)
#         plt.tight_layout()
#         return fig

#     def plot_dropout_by_time_slot(self):
#         if 'time_slot' not in self.df.columns or 'no_show' not in self.df.columns:
#             return None

#         dropout_by_time = self.df.groupby('time_slot')['no_show'].mean().reset_index()
#         dropout_by_time['dropout_rate'] = dropout_by_time['no_show'] * 100

#         time_order = ['Morning', 'Afternoon', 'Evening', 'Night']
#         dropout_by_time['time_slot'] = pd.Categorical(dropout_by_time['time_slot'], categories=time_order, ordered=True)
#         dropout_by_time = dropout_by_time.sort_values('time_slot')

#         fig, ax = plt.subplots(figsize=(6, 4))
#         sns.barplot(data=dropout_by_time, x='time_slot', y='dropout_rate', palette='magma', ax=ax)
#         plt.title('No-show Rate by Scheduled Time Slot', fontsize=13)
#         plt.xlabel('Time Slot')
#         plt.ylabel('Dropout Rate (%)')
#         plt.grid(axis='y', linestyle='--', alpha=0.5)
#         plt.tight_layout()
#         return fig

# Updated `visualizations.py`

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class Visualizer:
    def __init__(self, df):
        self.df = df.copy()
        self._prepare_data()

    def _prepare_data(self):
        self.df.columns = [col.strip().lower().replace('-', '_') for col in self.df.columns]

        if 'no_show' in self.df.columns:
            if self.df['no_show'].dtype == object:
                self.df['no_show'] = self.df['no_show'].map({'Yes': 1, 'No': 0, 'yes': 1, 'no': 0}).fillna(self.df['no_show'])
            self.df['no_show'] = pd.to_numeric(self.df['no_show'], errors='coerce')

        if 'gender' in self.df.columns:
            unique_genders = self.df['gender'].unique()
            if set(unique_genders).issubset({0, 1}):
                self.df['gender_label'] = self.df['gender'].map({0: 'Male', 1: 'Female'})
            elif set(unique_genders).issubset({'M', 'F'}):
                self.df['gender_label'] = self.df['gender'].map({'M': 'Male', 'F': 'Female'})
            else:
                self.df['gender_label'] = self.df['gender']

        if 'appointmentday' in self.df.columns:
            self.df['appointmentday'] = pd.to_datetime(self.df['appointmentday'], errors='coerce')

        if 'scheduledday' in self.df.columns:
            self.df['scheduledday'] = pd.to_datetime(self.df['scheduledday'], errors='coerce')
            self.df['scheduledhour'] = self.df['scheduledday'].dt.hour
            self.df['time_slot'] = self.df['scheduledhour'].apply(self.time_of_day)

        if 'age' in self.df.columns:
            bins = [0, 12, 18, 30, 45, 60, 75, 100]
            labels = ['Child', 'Teen', 'Young Adult', 'Adult', 'Middle Age', 'Senior', 'Elderly']
            self.df['age_group'] = pd.cut(self.df['age'], bins=bins, labels=labels)

    def time_of_day(self, hour):
        if pd.isnull(hour):
            return 'Unknown'
        if 6 <= hour < 12:
            return 'Morning'
        elif 12 <= hour < 17:
            return 'Afternoon'
        elif 17 <= hour < 21:
            return 'Evening'
        else:
            return 'Night'

    def plot_dropout_by_age(self):
        if 'age_group' not in self.df.columns or 'no_show' not in self.df.columns:
            return None
        dropout_by_age = self.df.groupby('age_group')['no_show'].mean().reset_index()
        dropout_by_age['dropout_rate'] = dropout_by_age['no_show'] * 100
        fig, ax = plt.subplots()
        sns.barplot(data=dropout_by_age, x='age_group', y='dropout_rate', palette='magma', ax=ax)
        plt.xticks(rotation=45)
        plt.ylabel('Dropout Rate (%)')
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.title('No-show Rate by Age Group')
        return fig

    def plot_dropout_by_weekday(self):
        if 'appointmentday' not in self.df.columns or 'no_show' not in self.df.columns:
            return None
        self.df['weekday'] = self.df['appointmentday'].dt.day_name()
        weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        dropout_by_day = self.df.groupby('weekday')['no_show'].mean().reset_index()
        dropout_by_day['dropout_rate'] = dropout_by_day['no_show'] * 100
        dropout_by_day['weekday'] = pd.Categorical(dropout_by_day['weekday'], categories=weekday_order, ordered=True)
        dropout_by_day = dropout_by_day.sort_values('weekday')
        fig, ax = plt.subplots()
        sns.barplot(data=dropout_by_day, x='weekday', y='dropout_rate', palette='magma', ax=ax)
        plt.xticks(rotation=45)
        plt.ylabel('Dropout Rate (%)')
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.title('No-show Rate by Weekday')
        return fig

    def plot_dropout_by_gender(self):
        if 'gender_label' not in self.df.columns or 'no_show' not in self.df.columns:
            return None
        dropout_by_gender = self.df.groupby('gender_label')['no_show'].mean().reset_index()
        dropout_by_gender['dropout_rate'] = dropout_by_gender['no_show'] * 100
        fig, ax = plt.subplots()
        sns.barplot(data=dropout_by_gender, x='gender_label', y='dropout_rate', palette='magma', ax=ax)
        plt.ylabel('Dropout Rate (%)')
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.title('No-show Rate by Gender')
        return fig

    def plot_correlation_heatmap(self):
        numeric_df = self.df.select_dtypes(include=['number'])
        if numeric_df.empty:
            return None
        corr_matrix = numeric_df.corr()
        fig, ax = plt.subplots(figsize=(12, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, ax=ax)
        plt.title('Correlation Heatmap')
        plt.xticks(rotation=45)
        plt.yticks(rotation=0)
        plt.tight_layout()
        return fig

    def plot_dropout_by_neighborhood(self):
        if 'neighbourhood' not in self.df.columns or 'no_show' not in self.df.columns:
            return None
        top_neighborhoods = self.df['neighbourhood'].value_counts().head(10).index
        df_top = self.df[self.df['neighbourhood'].isin(top_neighborhoods)]
        dropout_by_neighborhood = df_top.groupby('neighbourhood')['no_show'].mean().reset_index()
        dropout_by_neighborhood['dropout_rate'] = dropout_by_neighborhood['no_show'] * 100
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.barplot(data=dropout_by_neighborhood, x='neighbourhood', y='dropout_rate', palette='magma', ax=ax)
        plt.title('No-show Rate by Top 10 Neighborhoods')
        plt.ylabel('Dropout Rate (%)')
        plt.xlabel('Neighborhood')
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.tight_layout()
        return fig

    def plot_dropout_by_time_slot(self):
        if 'time_slot' not in self.df.columns or 'no_show' not in self.df.columns:
            return None
        dropout_by_time = self.df.groupby('time_slot')['no_show'].mean().reset_index()
        dropout_by_time['dropout_rate'] = dropout_by_time['no_show'] * 100
        time_order = ['Morning', 'Afternoon', 'Evening', 'Night']
        dropout_by_time['time_slot'] = pd.Categorical(dropout_by_time['time_slot'], categories=time_order, ordered=True)
        dropout_by_time = dropout_by_time.sort_values('time_slot')
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.barplot(data=dropout_by_time, x='time_slot', y='dropout_rate', palette='magma', ax=ax)
        plt.title('No-show Rate by Scheduled Time Slot', fontsize=13)
        plt.xlabel('Time Slot')
        plt.ylabel('Dropout Rate (%)')
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.tight_layout()
        return fig