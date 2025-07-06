# # import streamlit as st
# # import pandas as pd
# # from visualizations import Visualizer
# # from insights import InsightGenerator
# # #from report_generator import create_pdf_report  

# # st.title("Medical Appointment No-Show Analysis")

# # uploaded_file = st.file_uploader("Upload your dataset (CSV file)", type=['csv'])

# # if uploaded_file:
# #     df = pd.read_csv(uploaded_file)

# #     st.write("### Dataset Preview")
# #     st.dataframe(df.head())


# V E R S I O N  1


# import streamlit as st
# import pandas as pd
# from visualizations import Visualizer
# from insights import InsightGenerator
# from data_loader import DataLoader

# st.title("Medical Appointment No-Show Analysis")

# uploaded_file = st.file_uploader("Upload your dataset (CSV file)", type=['csv'])

# if uploaded_file:
#     df = DataLoader(uploaded_file).load_data()

#     st.write("### Dataset Preview")
#     st.dataframe(df.head())

#     # Sidebar Filters with Error Handling
#     st.sidebar.title("🔎 Filter Options")

#     age_groups = df['Age_Group'].dropna().unique() if 'Age_Group' in df.columns else []
#     time_slots = df['time_slot'].dropna().unique() if 'time_slot' in df.columns else []

#     if len(age_groups) > 0:
#         selected_age_group = st.sidebar.selectbox("Select Age Group", sorted(age_groups))
#     else:
#         selected_age_group = None
#         st.sidebar.warning("Age Group column not found!")

#     if len(time_slots) > 0:
#         selected_time_slot = st.sidebar.selectbox("Select Time Slot", sorted(time_slots))
#     else:
#         selected_time_slot = None
#         st.sidebar.warning("Time Slot column not found!")


#     # Apply filters if available
#     if selected_age_group and selected_time_slot:
#         filtered_df = df[(df['Age_Group'] == selected_age_group) & (df['Time_Slot'] == selected_time_slot)]
#     else:
#         filtered_df = df

#     visualizer = Visualizer(filtered_df)
#     insights = InsightGenerator(filtered_df)

#     # Reusable Insight Display Function
#     def display_insight(insight_text):
#         st.markdown(f"""
#         <div style="padding:10px;border-radius:10px;margin-top:10px">
#             {insight_text}
#         </div>
#         """, unsafe_allow_html=True)

#     st.markdown("## Dropout Rate by Age Group")
#     fig1 = visualizer.plot_dropout_by_age()
#     if fig1:
#         st.pyplot(fig1)
#         display_insight(insights.get_age_group_insight())
#     else:
#         st.warning("Age or No-show columns not found!")

#     st.markdown("## Dropout Rate by Weekday")
#     fig2 = visualizer.plot_dropout_by_weekday()
#     if fig2:
#         st.pyplot(fig2)
#         display_insight(insights.get_weekday_insight())
#     else:
#         st.warning("AppointmentDay or No-show columns not found or not in correct format!")

#     st.markdown("## Dropout Rate by Gender")
#     fig3 = visualizer.plot_dropout_by_gender()
#     if fig3:
#         st.pyplot(fig3)
#         display_insight(insights.get_gender_insight())
#     else:
#         st.warning("Gender or No-show columns not found!")

#     st.markdown("## Correlation Heatmap")
#     heatmap = visualizer.plot_correlation_heatmap()
#     if heatmap:
#         st.pyplot(heatmap)
#     else:
#         st.warning("No numeric columns found for correlation heatmap.")

#     st.markdown("## Dropout Rate by Top 10 Neighborhoods")
#     fig4 = visualizer.plot_dropout_by_neighborhood()
#     if fig4:
#         st.pyplot(fig4)
#         display_insight(insights.get_neighborhood_insight())
#     else:
#         st.warning("Neighbourhood or No-show columns not found!")

#     st.markdown("## Dropout Rate by Time Slot")
#     fig5 = visualizer.plot_dropout_by_time_slot()
#     if fig5:
#         st.pyplot(fig5)
#         display_insight(insights.get_time_slot_insight())
#     else:
#         st.warning("ScheduledDay or No-show columns not found or not in correct format!")

#     # PDF Report Generation
#     if st.button("📄 Generate PDF Report"):
#         insights_dict = {
#             "Age Group Insight": insights.get_age_group_insight(plain_text=True),
#             "Weekday Insight": insights.get_weekday_insight(plain_text=True),
#             "Gender Insight": insights.get_gender_insight(plain_text=True),
#             "Neighborhood Insight": insights.get_neighborhood_insight(plain_text=True),
#             "Time Slot Insight": insights.get_time_slot_insight(plain_text=True)
#         }

#         # filename = create_pdf_report(insights_dict)

#         # with open(filename, "rb") as file:
#         #     st.download_button(
#         #         label="📥 Download Report",
#         #         data=file,
#         #         file_name=filename,
#         #         mime="application/pdf"
#         #     )
# else:
#     st.info("Please upload a CSV file to proceed.")


# V E R S I O N  2


# import streamlit as st
# import pandas as pd
# from visualizations import Visualizer
# from insights import InsightGenerator
# from data_loader import DataLoader

# st.set_page_config(page_title="No-Show Analysis", layout="wide")

# st.title("📊 Medical Appointment No-Show Analysis")

# uploaded_file = st.file_uploader("Upload your dataset (CSV file)", type=['csv'])

# if uploaded_file:
#     df = DataLoader(uploaded_file).load_data()

#     st.write("### Dataset Preview")
#     st.dataframe(df.head())

#     # Sidebar Filters with Error Handling
#     st.sidebar.title("🔎 Filter Options")

#     age_groups = df['age_group'].dropna().unique() if 'age_group' in df.columns else []
#     time_slots = df['time_slot'].dropna().unique() if 'time_slot' in df.columns else []

#     if len(age_groups) > 0:
#         selected_age_group = st.sidebar.selectbox("Select Age Group", sorted(age_groups))
#     else:
#         selected_age_group = None
#         st.sidebar.warning("Age Group column not found!")

#     if len(time_slots) > 0:
#         selected_time_slot = st.sidebar.selectbox("Select Time Slot", sorted(time_slots))
#     else:
#         selected_time_slot = None
#         st.sidebar.warning("Time Slot column not found!")

#     # Apply filters if available
#     if selected_age_group and selected_time_slot:
#         filtered_df = df[(df['age_group'] == selected_age_group) & (df['time_slot'] == selected_time_slot)]
#     else:
#         filtered_df = df

#     visualizer = Visualizer(filtered_df)
#     insights = InsightGenerator(filtered_df)

#     # Reusable Insight Display Function
#     def display_insight(insight_text):
#         st.markdown(f"""
#         <div style="padding:10px;border-radius:10px;margin-top:10px">
#             {insight_text}
#         </div>
#         """, unsafe_allow_html=True)

#     st.markdown("## Dropout Rate by Age Group")
#     fig1 = visualizer.plot_dropout_by_age()
#     if fig1:
#         st.pyplot(fig1)
#         display_insight(insights.get_age_group_insight())
#     else:
#         st.warning("Age or No-show columns not found!")

#     st.markdown("## Dropout Rate by Weekday")
#     fig2 = visualizer.plot_dropout_by_weekday()
#     if fig2:
#         st.pyplot(fig2)
#         display_insight(insights.get_weekday_insight())
#     else:
#         st.warning("AppointmentDay or No-show columns not found or not in correct format!")

#     st.markdown("## Dropout Rate by Gender")
#     fig3 = visualizer.plot_dropout_by_gender()
#     if fig3:
#         st.pyplot(fig3)
#         display_insight(insights.get_gender_insight())
#     else:
#         st.warning("Gender or No-show columns not found!")

#     st.markdown("## Correlation Heatmap")
#     heatmap = visualizer.plot_correlation_heatmap()
#     if heatmap:
#         st.pyplot(heatmap)
#     else:
#         st.warning("No numeric columns found for correlation heatmap.")

#     st.markdown("## Dropout Rate by Top 10 Neighborhoods")
#     fig4 = visualizer.plot_dropout_by_neighborhood()
#     if fig4:
#         st.pyplot(fig4)
#         display_insight(insights.get_neighborhood_insight())
#     else:
#         st.warning("Neighbourhood or No-show columns not found!")

#     st.markdown("## Dropout Rate by Time Slot")
#     fig5 = visualizer.plot_dropout_by_time_slot()
#     if fig5:
#         st.pyplot(fig5)
#         display_insight(insights.get_time_slot_insight())
#     else:
#         st.warning("ScheduledDay or No-show columns not found or not in correct format!")

#     # PDF Report Generation
#     if st.button("📄 Generate PDF Report"):
#         insights_dict = {
#             "Age Group Insight": insights.get_age_group_insight(plain_text=True),
#             "Weekday Insight": insights.get_weekday_insight(plain_text=True),
#             "Gender Insight": insights.get_gender_insight(plain_text=True),
#             "Neighborhood Insight": insights.get_neighborhood_insight(plain_text=True),
#             "Time Slot Insight": insights.get_time_slot_insight(plain_text=True)
#         }
#         # Placeholder for PDF function
#         st.success("✅ Report generated (PDF export function can be integrated here).")
# else:
#     st.info("Please upload a CSV file to proceed.")


# V E R S I O N  3

# import streamlit as st
# import pandas as pd
# from visualizations import Visualizer
# from insights import InsightGenerator
# from data_loader import DataLoader

# st.set_page_config(layout="wide")
# st.title("Medical Appointment No-Show Analysis")

# uploaded_file = st.file_uploader("Upload your dataset (CSV file)", type=['csv'])

# if uploaded_file:
#     df = DataLoader(uploaded_file).load_data()

#     st.write("### Dataset Preview")
#     st.dataframe(df.head())

#     # Sidebar Filters
#     st.sidebar.title("🔎 Filter Options")

#     # Age Group Filter
#     # age_groups = df['Age_Group'].dropna().unique().tolist() if 'Age_Group' in df.columns else []
#     # age_groups = sorted(age_groups)
#     # if age_groups:
#     #     age_groups.insert(0, "All")
#     #     selected_age_group = st.sidebar.selectbox("Select Age Group", age_groups)
#     # else:
#     #     selected_age_group = "All"
#     #     st.sidebar.warning("Age Group column not found!")

#     age_groups = df['Age_Group'].dropna().astype(str).unique().tolist() if 'Age_Group' in df.columns else []
#     age_groups = sorted(age_groups)
#     if age_groups:
#         selected_age_groups = st.sidebar.multiselect(
#             "Select Age Group",
#             options=["All"] + age_groups,
#             default=["All"]
#         )
#         if "All" in selected_age_groups:
#             selected_age_groups = age_groups  # select all if 'All' is selected
#     else:
#         selected_age_groups = []
#         st.sidebar.warning("Age Group column not found!")

#     # Time Slot Filter
#     # time_slots = df['time_slot'].dropna().unique().tolist() if 'time_slot' in df.columns else []
#     # time_slots = sorted(time_slots)
#     # if time_slots:
#     #     time_slots.insert(0, "All")
#     #     selected_time_slot = st.sidebar.selectbox("Select Time Slot", time_slots)
#     # else:
#     #     selected_time_slot = "All"
#     #     st.sidebar.warning("Time Slot column not found!")

#     time_slots = df['time_slot'].dropna().astype(str).unique().tolist() if 'time_slot' in df.columns else []
#     time_slots = sorted(time_slots)
#     if time_slots:
#         selected_time_slots = st.sidebar.multiselect(
#             "Select Time Slot",
#             options=["All"] + time_slots,
#             default=["All"]
#         )
#         if "All" in selected_time_slots:
#             selected_time_slots = time_slots  # select all if 'All' is selected
#     else:
#         selected_time_slots = []
#         st.sidebar.warning("Time Slot column not found!")

#     # Apply filters
#     filtered_df = df.copy()
#     if selected_age_groups:
#         filtered_df = filtered_df[filtered_df['Age_Group'].astype(str).isin(selected_age_groups)]
#     if selected_time_slots:
#         filtered_df = filtered_df[filtered_df['time_slot'].astype(str).isin(selected_time_slots)]

#     # Visualizations and Insights
#     visualizer = Visualizer(filtered_df)
#     insights = InsightGenerator(filtered_df)

#     def display_insight(insight_text):
#         st.markdown(f"""
#         <div style="padding:10px;border-radius:10px;margin-top:10px">
#             {insight_text}
#         </div>
#         """, unsafe_allow_html=True)

#     st.markdown("## Dropout Rate by Age Group")
#     fig1 = visualizer.plot_dropout_by_age()
#     if fig1:
#         st.pyplot(fig1)
#         display_insight(insights.get_age_group_insight())
#     else:
#         st.warning("Age or No-show columns not found!")

#     st.markdown("## Dropout Rate by Weekday")
#     fig2 = visualizer.plot_dropout_by_weekday()
#     if fig2:
#         st.pyplot(fig2)
#         display_insight(insights.get_weekday_insight())
#     else:
#         st.warning("AppointmentDay or No-show columns not found or not in correct format!")

#     st.markdown("## Dropout Rate by Gender")
#     fig3 = visualizer.plot_dropout_by_gender()
#     if fig3:
#         st.pyplot(fig3)
#         display_insight(insights.get_gender_insight())
#     else:
#         st.warning("Gender or No-show columns not found!")

#     st.markdown("## Correlation Heatmap")
#     heatmap = visualizer.plot_correlation_heatmap()
#     if heatmap:
#         st.pyplot(heatmap)
#     else:
#         st.warning("No numeric columns found for correlation heatmap.")

#     st.markdown("## Dropout Rate by Top 10 Neighborhoods")
#     fig4 = visualizer.plot_dropout_by_neighborhood()
#     if fig4:
#         st.pyplot(fig4)
#         display_insight(insights.get_neighborhood_insight())
#     else:
#         st.warning("Neighbourhood or No-show columns not found!")

#     st.markdown("## Dropout Rate by Time Slot")
#     fig5 = visualizer.plot_dropout_by_time_slot()
#     if fig5:
#         st.pyplot(fig5)
#         display_insight(insights.get_time_slot_insight())
#     else:
#         st.warning("ScheduledDay or No-show columns not found or not in correct format!")

#     # Future scope: PDF report generation button (disabled)
#     # if st.button("📄 Generate PDF Report"):
#     #     insights_dict = {
#     #         "Age Group Insight": insights.get_age_group_insight(plain_text=True),
#     #         "Weekday Insight": insights.get_weekday_insight(plain_text=True),
#     #         "Gender Insight": insights.get_gender_insight(plain_text=True),
#     #         "Neighborhood Insight": insights.get_neighborhood_insight(plain_text=True),
#     #         "Time Slot Insight": insights.get_time_slot_insight(plain_text=True)
#     #     }
#     #     filename = create_pdf_report(insights_dict)
#     #     with open(filename, "rb") as file:
#     #         st.download_button(
#     #             label="📥 Download Report",
#     #             data=file,
#     #             file_name=filename,
#     #             mime="application/pdf"
#     #         )

# else:
#     st.info("Please upload a CSV file to proceed.")


# V E R S I O N 4

import streamlit as st
import pandas as pd
from visualizations import Visualizer
from insights import InsightGenerator
from data_loader import DataLoader

st.title("Medical Appointment No-Show Analysis")

uploaded_file = st.file_uploader("Upload your dataset (CSV file)", type=['csv'])

if uploaded_file:
    df = DataLoader(uploaded_file).load_data()

    st.write("### Dataset Preview")
    st.dataframe(df.head())

    st.sidebar.title("🔎 Filter Options")

    # Add "All" option explicitly
    age_groups = sorted(df['age_group'].dropna().unique().astype(str))
    time_slots = sorted(df['time_slot'].dropna().unique().astype(str))

    age_group_options = ['All'] + age_groups
    time_slot_options = ['All'] + time_slots

    selected_age_group = st.sidebar.selectbox("Select Age Group", age_group_options)
    selected_time_slot = st.sidebar.selectbox("Select Time Slot", time_slot_options)

    # Apply filters only if not "All"
    filtered_df = df.copy()
    if selected_age_group != 'All':
        filtered_df = filtered_df[filtered_df['age_group'].astype(str) == selected_age_group]
    if selected_time_slot != 'All':
        filtered_df = filtered_df[filtered_df['time_slot'].astype(str) == selected_time_slot]


#     visualizer = Visualizer(filtered_df)

#     st.markdown("## Dropout Rate by Age Group")
#     fig1 = visualizer.plot_dropout_by_age()
#     if fig1:
#         st.pyplot(fig1)
#     else:
#         st.warning("Required columns not found.")

#     st.markdown("## Dropout Rate by Weekday")
#     fig2 = visualizer.plot_dropout_by_weekday()
#     if fig2:
#         st.pyplot(fig2)
#     else:
#         st.warning("Required columns not found or improperly formatted.")

#     st.markdown("## Dropout Rate by Gender")
#     fig3 = visualizer.plot_dropout_by_gender()
#     if fig3:
#         st.pyplot(fig3)
#     else:
#         st.warning("Required columns not found.")

#     st.markdown("## Correlation Heatmap")
#     heatmap = visualizer.plot_correlation_heatmap()
#     if heatmap:
#         st.pyplot(heatmap)
#     else:
#         st.warning("No numeric data for heatmap.")

#     st.markdown("## Dropout Rate by Top 10 Neighborhoods")
#     fig4 = visualizer.plot_dropout_by_neighborhood()
#     if fig4:
#         st.pyplot(fig4)
#     else:
#         st.warning("Required columns not found.")

#     st.markdown("## Dropout Rate by Time Slot")
#     fig5 = visualizer.plot_dropout_by_time_slot()
#     if fig5:
#         st.pyplot(fig5)
#     else:
#         st.warning("Required columns not found or improperly formatted.")

# else:
#     st.info("Please upload a CSV file to proceed.")
    # Visualizations and Insights
    visualizer = Visualizer(filtered_df)
    insights = InsightGenerator(filtered_df)

    def display_insight(insight_text):
        st.markdown(f"""
        <div style="padding:10px;border-radius:10px;margin-top:10px">
            {insight_text}
        </div>
        """, unsafe_allow_html=True)

    st.markdown("## Dropout Rate by Age Group")
    fig1 = visualizer.plot_dropout_by_age()
    if fig1:
        st.pyplot(fig1)
        display_insight(insights.get_age_group_insight())
    else:
        st.warning("Age or No-show columns not found!")

    st.markdown("## Dropout Rate by Weekday")
    fig2 = visualizer.plot_dropout_by_weekday()
    if fig2:
        st.pyplot(fig2)
        display_insight(insights.get_weekday_insight())
    else:
        st.warning("AppointmentDay or No-show columns not found or not in correct format!")

    st.markdown("## Dropout Rate by Gender")
    fig3 = visualizer.plot_dropout_by_gender()
    if fig3:
        st.pyplot(fig3)
        display_insight(insights.get_gender_insight())
    else:
        st.warning("Gender or No-show columns not found!")

    st.markdown("## Correlation Heatmap")
    heatmap = visualizer.plot_correlation_heatmap()
    if heatmap:
        st.pyplot(heatmap)
    else:
        st.warning("No numeric columns found for correlation heatmap.")

    st.markdown("## Dropout Rate by Top 10 Neighborhoods")
    fig4 = visualizer.plot_dropout_by_neighborhood()
    if fig4:
        st.pyplot(fig4)
        display_insight(insights.get_neighborhood_insight())
    else:
        st.warning("Neighbourhood or No-show columns not found!")

    st.markdown("## Dropout Rate by Time Slot")
    fig5 = visualizer.plot_dropout_by_time_slot()
    if fig5:
        st.pyplot(fig5)
        display_insight(insights.get_time_slot_insight())
    else:
        st.warning("ScheduledDay or No-show columns not found or not in correct format!")

    # Future scope: PDF report generation button (disabled)
    # if st.button("📄 Generate PDF Report"):
    #     insights_dict = {
    #         "Age Group Insight": insights.get_age_group_insight(plain_text=True),
    #         "Weekday Insight": insights.get_weekday_insight(plain_text=True),
    #         "Gender Insight": insights.get_gender_insight(plain_text=True),
    #         "Neighborhood Insight": insights.get_neighborhood_insight(plain_text=True),
    #         "Time Slot Insight": insights.get_time_slot_insight(plain_text=True)
    #     }
    #     filename = create_pdf_report(insights_dict)
    #     with open(filename, "rb") as file:
    #         st.download_button(
    #             label="📥 Download Report",
    #             data=file,
    #             file_name=filename,
    #             mime="application/pdf"
    #         )

else:
    st.info("Please upload a CSV file to proceed.")