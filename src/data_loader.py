# #data loader -- load the data into proper dataframes -- data mapping and filtering. 

# import pandas as pd

# class DataLoader:
#     def __init__(self, filepath):
#         self.filepath = filepath

#     def load_data(self):
#         df = pd.read_csv(self.filepath)
#         df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'])
#         df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'])
#         df['No-show'] = df['No-show'].map({'No': 0, 'Yes': 1})
#         df = df[df['Age'] >= 0]
#         return df


# data_loader.py

import pandas as pd

class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_data(self):
        df = pd.read_csv(self.filepath)
        df.columns = [col.strip().lower().replace('-', '_') for col in df.columns]

        df['scheduledday'] = pd.to_datetime(df['scheduledday'], errors='coerce')
        df['appointmentday'] = pd.to_datetime(df['appointmentday'], errors='coerce')
        df['no_show'] = df['no_show'].map({'No': 0, 'Yes': 1, 'no': 0, 'yes': 1})
        df = df[df['age'] >= 0]

        # Create Age Group
        bins = [0, 12, 18, 30, 45, 60, 75, 100]
        labels = ['Child', 'Teen', 'Young Adult', 'Adult', 'Middle Age', 'Senior', 'Elderly']
        df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels)

        # Create Time Slot
        df['scheduledhour'] = df['scheduledday'].dt.hour
        df['time_slot'] = df['scheduledhour'].apply(self._time_of_day)

        return df

    def _time_of_day(self, hour):
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
