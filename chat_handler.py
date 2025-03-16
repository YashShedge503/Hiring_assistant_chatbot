import os
import streamlit as st
from openai import OpenAI
import json

class ChatHandler:
    def __init__(self):
        self.model = "gpt-4o"
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.using_mock = False  # Flag to indicate if we're using mock responses

    def get_mock_response(self, user_input, current_stage):
        """Provide mock responses for testing when API is unavailable"""
        if "name" in current_stage.lower():
            return f"Thank you for providing your name! Could you please share your email address?"
        elif "email" in current_stage.lower():
            return "Great! Now, could you please provide your phone number?"
        elif "phone" in current_stage.lower():
            return "Excellent! How many years of experience do you have in the technology industry?"
        elif "experience" in current_stage.lower():
            return "Great! What is your current location?"
        elif "location" in current_stage.lower():
            return "Which position are you interested in applying for?"
        elif "position" in current_stage.lower():
            return "Please list your tech stack (programming languages, frameworks, and tools you're proficient in)."
        elif "tech_stack" in current_stage.lower():
            return self.generate_mock_technical_questions(user_input)
        else:
            return "Is there anything specific about these technologies you'd like to discuss?"

    def generate_mock_technical_questions(self, tech_stack):
        """Generate relevant technical questions based on the provided tech stack"""
        questions = []
        techs = [t.strip().lower() for t in tech_stack.split(',')]

        # Questions for C++
        if 'c++' in techs:
            questions.extend([
                "1. Can you explain the difference between stack and heap memory allocation in C++?",
                "2. What are virtual functions in C++ and how do they support polymorphism?",
                "3. Describe the RAII principle and its importance in C++ programming."
            ])

        # Questions for Python
        if 'python' in techs:
            questions.extend([
                "4. How do Python decorators work and what are some common use cases?",
                "5. Explain the difference between deep copy and shallow copy in Python.",
                "6. What is the Global Interpreter Lock (GIL) in Python and how does it affect multithreading?"
            ])

        if questions:
            return "Based on your tech stack, here are some technical questions to assess your expertise:\n\n" + "\n\n".join(questions) + "\n\nPlease feel free to answer any or all of these questions. Your responses will help us better understand your technical proficiency."
        else:
            return "I couldn't generate specific questions for your tech stack. Could you please provide more details about your technical expertise?"

    def process_message(self, user_input):
        try:
            if not self.using_mock:
                # Try using OpenAI API first
                messages = [
                    {
                        "role": "system",
                        "content": """You are a professional hiring assistant for TalentScout, 
                        a recruitment agency specializing in technology placements. 
                        Follow this conversation flow:
                        1. Collect candidate information (name, email, phone, experience, location, desired position)
                        2. Ask about their tech stack
                        3. Generate 3-5 relevant technical questions based on their tech stack
                        4. Maintain professional tone and stay focused on recruitment
                        Only proceed to the next step when current information is complete.
                        """
                    }
                ]

                # Add conversation history from session state
                for msg in st.session_state.messages:
                    messages.append({"role": msg["role"], "content": msg["content"]})

                # Add current user input
                messages.append({"role": "user", "content": user_input})

                # Get response from OpenAI
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    temperature=0.7,
                    max_tokens=800
                )
                return response.choices[0].message.content

            else:
                # Use mock responses if API fails
                current_stage = st.session_state.current_stage
                return self.get_mock_response(user_input, current_stage)

        except Exception as e:
            # If API fails, switch to mock responses
            self.using_mock = True
            current_stage = st.session_state.current_stage
            return self.get_mock_response(user_input, current_stage)

    def should_end_conversation(self, user_input):
        # Check for conversation ending keywords
        end_keywords = ['goodbye', 'bye', 'exit', 'quit', 'end']
        return any(keyword in user_input.lower() for keyword in end_keywords)