import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()
print("Loaded API Key:", os.getenv("GROQ_API_KEY"))
api_key = os.getenv("GROQ_API_KEY")

st.set_page_config(page_title="Health Details Form", page_icon="🩺", layout="centered", initial_sidebar_state="expanded")

if "page" not in st.session_state:
    st.session_state.page = "Basic Details"
if "data" not in st.session_state:
    st.session_state.data = {
        "Basic Details": {},
        "Lifestyle & Habits": {},
        "Health Conditions & Medical History": {},
        "Dietary Preferences & Restrictions": {},
        "Activity & Fitness Goals": {},
        "Sleep & Recovery": {},
        "Hydration & Nutrition Details": {},
        "Mental & Emotional Wellbeing": {},
        "Personalized Goals": {}
    }

def navigate_to_page():
    st.session_state.page = st.sidebar.radio(
        "Navigate to:", 
        [
            "Basic Details", "Lifestyle & Habits", "Health Conditions & Medical History",
            "Dietary Preferences & Restrictions", "Activity & Fitness Goals",
            "Sleep & Recovery", "Hydration & Nutrition Details", "Mental & Emotional Wellbeing",
            "Personalized Goals"
        ],
        index=0
    )
    if st.sidebar.button("Go to Analytics"):
        st.session_state.page = "Analytics"
    
    if st.sidebar.button("AI Assistance"):
        st.session_state.page = 'AIAssistance'

def main():
    navigate_to_page()
    page = st.session_state.page

    if page == "Basic Details":
        basic_details()
    elif page == "Lifestyle & Habits":
        lifestyle_habits()
    elif page == "Health Conditions & Medical History":
        health_conditions()
    elif page == "Dietary Preferences & Restrictions":
        dietary_preferences()
    elif page == "Activity & Fitness Goals":
        activity_fitness()
    elif page == "Sleep & Recovery":
        sleep_recovery()
    elif page == "Hydration & Nutrition Details":
        hydration_nutrition()
    elif page == "Mental & Emotional Wellbeing":
        mental_emotional()
    elif page == "Personalized Goals":
        personalized_goals()
    elif page == "Analytics":
        analytics()
    elif page == "AIAssistance":
        assistantai()

def basic_details():
    st.header("Basic Details")
    name = st.text_input("Name", value=st.session_state.data["Basic Details"].get("Name", ""))
    age = st.slider("Age", 0, 100, value=st.session_state.data["Basic Details"].get("Age", 25))
    gender = st.radio("Gender", ["Male", "Female", "Other"], index=["Male", "Female", "Other"].index(st.session_state.data["Basic Details"].get("Gender", "Male")))
    weight = st.number_input("Weight (kg)", min_value=0.0, value=st.session_state.data["Basic Details"].get("Weight", 0.0), step=0.1)
    height = st.number_input("Height (cm)", min_value=0.0, value=st.session_state.data["Basic Details"].get("Height", 0.0), step=0.1)
    
    if weight > 0 and height > 0:
        bmi = weight / ((height / 100) ** 2)
        st.write(f"Your BMI is: {bmi:.2f}")

    if st.button("Save"):
        st.session_state.data["Basic Details"] = {
            "Name": name,
            "Age": age,
            "Gender": gender,
            "Weight": weight,
            "Height": height,
            "BMI": bmi
        }
        st.success("Basic Details saved successfully!")

def lifestyle_habits():
    st.header("Lifestyle & Habits")
    smoking = st.radio("Do you smoke?", ["Yes", "No"], index=["Yes", "No"].index(st.session_state.data["Lifestyle & Habits"].get("Smoking", "No")))
    alcohol = st.selectbox("Do you consume alcohol?", ["Never", "Occasionally", "Frequently"], index=["Never", "Occasionally", "Frequently"].index(st.session_state.data["Lifestyle & Habits"].get("Alcohol", "Never")))
    caffeine = st.slider("How many cups of coffee/tea do you drink daily?", 0, 10, value=st.session_state.data["Lifestyle & Habits"].get("Caffeine", 1))
    stress = st.radio("How would you rate your stress levels?", ["Low", "Moderate", "High"], index=["Low", "Moderate", "High"].index(st.session_state.data["Lifestyle & Habits"].get("Stress", "Low")))
    
    sleep_hours = st.slider("How many hours do you sleep daily?", 0, 12, value=st.session_state.data["Lifestyle & Habits"].get("Sleep Hours", 7))
    exercise_frequency = st.radio("How often do you exercise?", ["Never", "Occasionally", "Regularly"], index=["Never", "Occasionally", "Regularly"].index(st.session_state.data["Lifestyle & Habits"].get("Exercise Frequency", "Never")))

    if st.button("Save"):
        st.session_state.data["Lifestyle & Habits"] = {
            "Smoking": smoking,
            "Alcohol": alcohol,
            "Caffeine": caffeine,
            "Stress": stress,
            "Sleep Hours": sleep_hours,
            "Exercise Frequency": exercise_frequency
        }
        st.success("Lifestyle & Habits saved successfully!")

def health_conditions():
    st.header("Health Conditions & Medical History")
    existing_conditions = st.text_area("Do you have any existing health conditions? (e.g., diabetes, hypertension, etc.)", value=st.session_state.data["Health Conditions & Medical History"].get("Existing Conditions", ""))
    medications = st.text_area("Are you currently on any medication? (Please specify)", value=st.session_state.data["Health Conditions & Medical History"].get("Medications", ""))
    allergies = st.text_area("Do you have any food allergies? (e.g., nuts, dairy, gluten, etc.)", value=st.session_state.data["Health Conditions & Medical History"].get("Allergies", ""))
    family_history = st.text_area("Does your family have a history of any major medical conditions? (e.g., heart disease, cancer, etc.)", value=st.session_state.data["Health Conditions & Medical History"].get("Family History", ""))

    if st.button("Save"):
        st.session_state.data["Health Conditions & Medical History"] = {
            "Existing Conditions": existing_conditions,
            "Medications": medications,
            "Allergies": allergies,
            "Family History": family_history
        }
        st.success("Health Conditions & Medical History saved successfully!")

def dietary_preferences():
    st.header("Dietary Preferences & Restrictions")
    food_allergies = st.text_area("List any specific food allergies you have.", value=st.session_state.data["Dietary Preferences & Restrictions"].get("Food Allergies", ""))
    diet_restrictions = st.text_area("Do you follow any specific diet? (e.g., keto, gluten-free, vegan)", value=st.session_state.data["Dietary Preferences & Restrictions"].get("Diet Restrictions", ""))
    favorite_foods = st.text_area("What are your favorite foods?", value=st.session_state.data["Dietary Preferences & Restrictions"].get("Favorite Foods", ""))
    disliked_foods = st.text_area("Are there any foods you dislike or avoid?", value=st.session_state.data["Dietary Preferences & Restrictions"].get("Disliked Foods", ""))

    if st.button("Save"):
        st.session_state.data["Dietary Preferences & Restrictions"] = {
            "Food Allergies": food_allergies,
            "Diet Restrictions": diet_restrictions,
            "Favorite Foods": favorite_foods,
            "Disliked Foods": disliked_foods
        }
        st.success("Dietary Preferences & Restrictions saved successfully!")

def activity_fitness():
    st.header("Activity & Fitness Goals")
    exercise_days = st.slider("How many days per week do you exercise?", 0, 7, value=st.session_state.data["Activity & Fitness Goals"].get("Exercise Days", 3))
    exercise_type = st.text_area("What type of physical activities do you engage in?", value=st.session_state.data["Activity & Fitness Goals"].get("Exercise Type", ""))
    fitness_goals = st.text_area("What are your current fitness goals?", value=st.session_state.data["Activity & Fitness Goals"].get("Fitness Goals", ""))
    step_count = st.number_input("How many steps do you walk on an average day?", min_value=0, value=st.session_state.data["Activity & Fitness Goals"].get("Step Count", 0), step=100)

    if st.button("Save"):
        st.session_state.data["Activity & Fitness Goals"] = {
            "Exercise Days": exercise_days,
            "Exercise Type": exercise_type,
            "Fitness Goals": fitness_goals,
            "Step Count": step_count
        }
        st.success("Activity & Fitness Goals saved successfully!")

def sleep_recovery():
    st.header("Sleep & Recovery")
    sleep_quality = st.radio("How would you rate the quality of your sleep?", ["Poor", "Fair", "Good", "Excellent"], index=["Poor", "Fair", "Good", "Excellent"].index(st.session_state.data["Sleep & Recovery"].get("Sleep Quality", "Good")))
    sleep_disorders = st.text_area("Do you have any sleep disorders? (e.g., insomnia, sleep apnea)", value=st.session_state.data["Sleep & Recovery"].get("Sleep Disorders", ""))
    recovery_activities = st.text_area("What activities do you do to aid recovery?", value=st.session_state.data["Sleep & Recovery"].get("Recovery Activities", ""))

    if st.button("Save"):
        st.session_state.data["Sleep & Recovery"] = {
            "Sleep Quality": sleep_quality,
            "Sleep Disorders": sleep_disorders,
            "Recovery Activities": recovery_activities
        }
        st.success("Sleep & Recovery details saved successfully!")

def hydration_nutrition():
    st.header("Hydration & Nutrition Details")
    water_intake = st.number_input("How many liters of water do you drink daily?", min_value=0.0, value=st.session_state.data["Hydration & Nutrition Details"].get("Water Intake", 2.0), step=0.1)
    meals_per_day = st.slider("How many meals do you eat daily?", 1, 10, value=st.session_state.data["Hydration & Nutrition Details"].get("Meals Per Day", 3))
    nutritional_supplements = st.text_area("Are you taking any nutritional supplements?", value=st.session_state.data["Hydration & Nutrition Details"].get("Nutritional Supplements", ""))

    if st.button("Save"):
        st.session_state.data["Hydration & Nutrition Details"] = {
            "Water Intake": water_intake,
            "Meals Per Day": meals_per_day,
            "Nutritional Supplements": nutritional_supplements
        }
        st.success("Hydration & Nutrition Details saved successfully!")

def mental_emotional():
    st.header("Mental & Emotional Wellbeing")
    mental_health_status = st.radio("How would you describe your mental health?", ["Poor", "Fair", "Good", "Excellent"], index=["Poor", "Fair", "Good", "Excellent"].index(st.session_state.data["Mental & Emotional Wellbeing"].get("Mental Health Status", "Good")))
    stress_management_techniques = st.text_area("What techniques do you use for stress management?", value=st.session_state.data["Mental & Emotional Wellbeing"].get("Stress Management Techniques", ""))
    support_system = st.text_area("Do you have a support system? (e.g., friends, family, therapist)", value=st.session_state.data["Mental & Emotional Wellbeing"].get("Support System", ""))

    if st.button("Save"):
        st.session_state.data["Mental & Emotional Wellbeing"] = {
            "Mental Health Status": mental_health_status,
            "Stress Management Techniques": stress_management_techniques,
            "Support System": support_system
        }
        st.success("Mental & Emotional Wellbeing details saved successfully!")

def personalized_goals():
    st.header("Personalized Goals")
    personal_goals = st.text_area("What are your personalized health goals?", value=st.session_state.data["Personalized Goals"].get("Personal Goals", ""))
    timeline = st.text_input("What is your timeline for achieving these goals?", value=st.session_state.data["Personalized Goals"].get("Timeline", ""))

    if st.button("Save"):
        st.session_state.data["Personalized Goals"] = {
            "Personal Goals": personal_goals,
            "Timeline": timeline
        }
        st.success("Personalized Goals saved successfully!")

def calculate_bmi(weight, height):
    if height > 0:  
        return weight / (height ** 2)
    return 0

def bmi_classification(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def analytics():
    st.header("Analytics")
    weight = st.session_state.data["Basic Details"].get("Weight", 70)  
    height = st.session_state.data["Basic Details"].get("Height", 1.75)  

    bmi = calculate_bmi(weight, height)
    bmi_status = bmi_classification(bmi)

    st.write(f"### Calculated BMI: {bmi:.2f}")
    st.write(f"### BMI Status: {bmi_status}")

    st.subheader("BMI Classification Chart")
    bmi_labels = ["Underweight", "Normal weight", "Overweight", "Obesity"]
    bmi_values = [18.5, 24.9, 29.9, 40]  
    bmi_fig = px.bar(x=bmi_values, y=bmi_labels, orientation='h',
                    color=bmi_labels,
                    color_discrete_sequence=["lightblue", "lightgreen", "orange", "red"],
                    labels={'x': 'BMI', 'y': 'Classification'},
                    title="BMI Classification")
    bmi_fig.add_vline(x=bmi, line_color="black", line_dash="dash", annotation_text=f"Your BMI: {bmi:.2f}")
    st.plotly_chart(bmi_fig)

    st.subheader("Weight Status Chart")

    weight_categories = ["Slim", "Normal", "Overweight", "Obese"]
    weight_thresholds = [50, 70, 90, 110]  

    weight_fig = px.bar(x=weight_thresholds, y=weight_categories, orientation='h',
                        color=weight_categories,
                        color_discrete_sequence=["lightblue", "lightgreen", "orange", "red"],
                        labels={'x': 'Weight (kg)', 'y': 'Category'},
                        title="Weight Status")
    weight_fig.add_vline(x=weight, line_color="black", line_dash="dash", annotation_text=f"Your Weight: {weight}kg")
    st.plotly_chart(weight_fig)

    labels = ['Carbohydrates', 'Proteins', 'Fats', 'Fiber', 'Vitamins', 'Minerals']
    sizes = [50, 30, 15, 3, 1, 1] 
    colors = ['gold', 'lightcoral', 'lightskyblue', 'yellowgreen', 'violet', 'lightgrey']

    macronutrient_fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, 
                                                hole=.3, 
                                                textinfo='label+percent',
                                                marker=dict(colors=colors))])
    macronutrient_fig.update_layout(title_text='Daily Macronutrient Intake')
    st.plotly_chart(macronutrient_fig)

    activity_levels = ['Sedentary', 'Lightly Active', 'Moderately Active', 'Very Active']
    recommended_intake = [2.0, 2.5, 3.0, 3.5]  
    water_intake_fig = px.bar(x=activity_levels, 
                            y=recommended_intake,
                            color=activity_levels,
                            labels={'x': 'Activity Level', 'y': 'Recommended Water Intake (Liters)'},
                            color_discrete_sequence=["lightblue", "lightgreen", "orange", "red"],
                            title="Daily Water Intake Recommendations")

    st.plotly_chart(water_intake_fig)

def assistantai():
    st.header("AI HealthCare Assistant")

    client = Groq(api_key=api_key)

    user_input = st.session_state.data if isinstance(st.session_state.data, str) else str(st.session_state.data)

    if not user_input:
        user_input = "No data provided."

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a health and wellness nutrition advisor. If no data is present, consider it no data and provide details of patient first your name and then their information and according to that give info you give as a Advisor and use markup and give info after each section"},
                {"role": "user", "content": user_input}
            ],
            model="llama3-8b-8192",
            temperature=0.5,
            max_tokens=1024,
            top_p=1,
            stop=None,
            stream=False,
        )

        nutrition_suggestion = chat_completion.choices[0].message.content
        st.subheader("Nutrition Suggestions:")
        st.write(nutrition_suggestion)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
