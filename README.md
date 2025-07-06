📊 Medical Appointment No-Show Analysis

This project analyzes patient no-shows for medical appointments using an interactive and insightful Streamlit dashboard. It helps identify trends and patterns behind missed appointments based on factors such as age, gender, time of day, weekday, and neighborhood. It also generates visualizations and actionable insights to support decision-making for clinics and hospitals.

🚀 Features
  - Upload your custom CSV dataset
  - Visual analysis by:
      Age groups
      Gender
      Weekday
      Time of day (time slots)
      Neighborhood
      Correlation heatmap
  - Insights with recommendations
  - Sidebar filters for age group and time slot
  - PDF report generation
  - Tableau dashboard integration

📦 Installation & Setup
  - Clone this repository:
    git clone https://github.com/your-username/no-show-analysis.git
    cd no-show-analysis
    
  - Create a virtual environment
    python -m venv venv
    venv\Scripts\activate   #or venv/bin/activate for IOS
    
  - Install the dependencies:
    pip install -r requirements.txt
    
  - Run the Streamlit app:
    streamlit run app.py

📊 Dataset Format
  - Ensure your dataset (CSV) has the following columns:
    | Column Name      | Description                                 |
    | ---------------- | ------------------------------------------- |
    | `ScheduledDay`   | Appointment scheduling timestamp            |
    | `AppointmentDay` | Actual appointment day                      |
    | `Age`            | Patient's age                               |
    | `Gender`         | M or F                                      |
    | `Neighbourhood`  | Patient's neighborhood                      |
    | `No-show`        | 'Yes' if the patient missed the appointment |

🧠 Sample Insights

    Insight:
    Minor variations are observed in no-show rates between genders.

    Possible Reasons:
    - Gender-specific societal responsibilities or accessibility may impact attendance.

    Recommendation:
    - Further explore gender-based barriers to medical attendance in specific regions.

📷 Screenshots
![image](https://github.com/user-attachments/assets/6b6b263f-d3ab-4752-bf06-3a6adf11d0c1)
![image](https://github.com/user-attachments/assets/4e68a60b-56e9-41f0-aeb1-23845a100d86)

