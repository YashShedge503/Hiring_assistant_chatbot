TalentScout AI Hiring Assistant

Project Overview

TalentScout AI Hiring Assistant is a chatbot designed to streamline the hiring process for technology recruitment agencies. Built using Streamlit and OpenAI's GPT-4o, it engages candidates in a structured conversation, collects relevant information, and generates personalized technical questions based on their expertise. The chatbot ensures a smooth recruitment process by automating candidate evaluations efficiently.

Installation Instructions

Prerequisites

Python 3.11 or later

Pip (Python Package Manager)

VS Code (or any preferred IDE)

OpenAI API Key

Setup Steps

Clone or Download the Repository

git clone <repository_url>
cd <project_folder>

(Optional) Create a Virtual Environment

python -m venv venv

Activate it:

Windows: venv\Scripts\activate

Mac/Linux: source venv/bin/activate

Install Dependencies

pip install -r requirements.txt

If requirements.txt is missing, manually install dependencies:

pip install openai streamlit

Set Your OpenAI API Key

export OPENAI_API_KEY="your_api_key_here"  # Mac/Linux
$env:OPENAI_API_KEY="your_api_key_here"  # Windows (PowerShell)

Run the Application

streamlit run app.py

Access the Chatbot in Browser

Open: http://localhost:8501 (or the URL shown in the terminal)

Usage Guide

Open the chatbot in your browser.

The assistant will guide candidates through the hiring process by:

Collecting personal and professional details (name, email, experience, location, etc.).

Asking about their technical expertise (programming languages, frameworks, tools).

Generating tailored technical questions to assess their skills.

The recruiter can review responses and evaluate the candidate's suitability.

Technical Details

Frontend & Interaction: Streamlit

Backend Processing: OpenAI's GPT-4o

Main Dependencies:

openai (for AI-powered conversation)

streamlit (for UI rendering)

File Structure:

app.py: Main entry point for Streamlit app.

chat_handler.py: Handles AI responses and logic.

utils.py: Manages session state and conversation flow.

pyproject.toml: Defines project dependencies.

Prompt Design

The chatbot follows a structured prompting approach:

Guided Information Collection:

Step-by-step collection of candidate details.

Ensures completion before proceeding.

Custom Question Generation:

Extracts tech stack and generates tailored questions.

Adapts dynamically based on responses.

Professional & Engaging Tone:

Maintains a recruitment-focused, engaging conversation.

Challenges & Solutions

1. Handling API Failures

Problem: OpenAI API failures or key misconfiguration.
Solution: Implemented a mock response mode to continue interaction when the API is unavailable.

2. Structuring Conversations Efficiently

Problem: Managing multi-step conversations without confusion.
Solution: Used session state management in Streamlit (st.session_state) to track progress.

3. Generating Relevant Technical Questions

Problem: Ensuring high-quality, job-relevant questions.
Solution: Designed custom question templates for major technologies (C++, Python, etc.).
