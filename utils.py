import streamlit as st

def initialize_session_state():
    """Initialize session state variables"""
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": """Hello! I'm the TalentScout AI Hiring Assistant. 
                I'll help evaluate your candidacy for technical positions.

                Let's start with your basic information.
                Could you please tell me your full name?"""
            }
        ]

    if "current_stage" not in st.session_state:
        st.session_state.current_stage = "name"

    if "candidate_info" not in st.session_state:
        st.session_state.candidate_info = {
            "name": "",
            "email": "",
            "phone": "",
            "experience": "",
            "location": "",
            "desired_position": "",
            "tech_stack": []
        }

def update_stage(user_input):
    """Update the conversation stage based on user input"""
    current_stage = st.session_state.current_stage

    # Update candidate info based on current stage
    if current_stage == "name":
        st.session_state.candidate_info["name"] = user_input
        st.session_state.current_stage = "email"
    elif current_stage == "email":
        st.session_state.candidate_info["email"] = user_input
        st.session_state.current_stage = "phone"
    elif current_stage == "phone":
        st.session_state.candidate_info["phone"] = user_input
        st.session_state.current_stage = "experience"
    elif current_stage == "experience":
        st.session_state.candidate_info["experience"] = user_input
        st.session_state.current_stage = "location"
    elif current_stage == "location":
        st.session_state.candidate_info["location"] = user_input
        st.session_state.current_stage = "position"
    elif current_stage == "position":
        st.session_state.candidate_info["desired_position"] = user_input
        st.session_state.current_stage = "tech_stack"
    elif current_stage == "tech_stack":
        st.session_state.candidate_info["tech_stack"] = [tech.strip() for tech in user_input.split(",")]
        st.session_state.current_stage = "questions"