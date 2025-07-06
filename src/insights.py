class InsightGenerator:
    def __init__(self, df):
        self.df = df

    def format_insight(self, insight_text, plain_text=False):
        if plain_text:
            return insight_text
        return f"<b>Insight:</b><br>{insight_text}"

    def get_age_group_insight(self, plain_text=False):
        insight = """
        Younger patients (especially children and teenagers) tend to have lower no-show rates.<br>
        Older adults and senior citizens may exhibit slightly higher dropout rates.<br>
        <br><b>Possible Reasons:</b><br>
        - Younger patients are often accompanied by guardians, ensuring attendance.<br>
        - Older patients may face mobility or health-related challenges.<br>
        <br><b>Recommendation:</b><br>
        - Clinics can provide transport support or tele-consult options for elderly patients.<br>
        - Encourage reminder calls for higher-risk age groups.
        """
        return self.format_insight(insight, plain_text)

    def get_weekday_insight(self, plain_text=False):
        insight = """
        Some weekdays (especially Saturdays) consistently show higher no-show rates.<br>
        <br><b>Possible Reasons:</b><br>
        - Patients may forget end-of-week appointments.<br>
        - Travel plans or weekend engagements can lead to cancellations.<br>
        <br><b>Recommendation:</b><br>
        - Increase reminder frequencies on higher-risk days.<br>
        - Avoid scheduling critical follow-ups on peak no-show days.
        """
        return self.format_insight(insight, plain_text)

    def get_gender_insight(self, plain_text=False):
        insight = """
        Minor variations are observed in no-show rates between genders.<br>
        <br><b>Possible Reasons:</b><br>
        - Gender-specific societal responsibilities or accessibility may impact attendance.<br>
        <br><b>Recommendation:</b><br>
        - Further explore gender-based barriers to medical attendance in specific regions.
        """
        return self.format_insight(insight, plain_text)

    def get_neighborhood_insight(self, plain_text=False):
        insight = """
        Certain neighborhoods have consistently higher no-show rates.<br>
        <br><b>Possible Reasons:</b><br>
        - Distance from the clinic or limited public transport.<br>
        - Socio-economic factors influencing medical priorities.<br>
        <br><b>Recommendation:</b><br>
        - Clinics could offer transport partnerships or mobile clinics for high-risk neighborhoods.<br>
        - Increase targeted communication in these areas.
        """
        return self.format_insight(insight, plain_text)

    def get_time_slot_insight(self, plain_text=False):
        insight = """
        Evening and night slots show higher no-show rates compared to mornings.<br>
        <br><b>Possible Reasons:</b><br>
        - End-of-day fatigue or unexpected commitments.<br>
        - Patients may deprioritize appointments later in the day.<br>
        <br><b>Recommendation:</b><br>
        - Encourage morning scheduling for critical appointments.<br>
        - Provide flexible rescheduling options for later slots.
        """
        return self.format_insight(insight, plain_text)
