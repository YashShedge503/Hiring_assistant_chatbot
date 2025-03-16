import streamlit as st
from chat_handler import ChatHandler
from utils import initialize_session_state, update_stage

def main():
    st.title("TalentScout AI Hiring Assistant")

    # Initialize session state
    initialize_session_state()

    # Initialize chat handler
    chat_handler = ChatHandler()

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Chat input
    if user_input := st.chat_input("Type your message here..."):
        # Display user message
        with st.chat_message("user"):
            st.write(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Update conversation stage
        update_stage(user_input)

        # Generate and display assistant response
        with st.chat_message("assistant"):
            response = chat_handler.process_message(user_input)
            st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

        # Check if conversation should end
        if chat_handler.should_end_conversation(user_input):
            st.success("Thank you for your time! We'll be in touch soon.")
            st.stop()

if __name__ == "__main__":
    main()