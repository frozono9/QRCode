import streamlit as st
import requests

# Flask app's update URL
update_url = "https://d83b1feb-dfea-4f0e-ad2f-3c342d968ac4-00-3gpxjdoc2m8am.kirk.replit.dev/update"

# Set page config to get rid of the sidebar (for a cleaner look)
st.set_page_config(page_title="Dynamic Redirect Link Manager", layout="centered")

# Custom styles to replicate Google's clean and minimalistic look
st.markdown("""
    <style>
        body {
            background-color: #ffffff;
            font-family: 'Arial', sans-serif;
        }

        /* Input field customization */
        .stTextInput>div>div>input {
            background-color: #f8f8f8;
            border: 1px solid #dcdcdc;
            border-radius: 24px;
            padding: 10px 20px;
            font-size: 18px;
            width: 100%;
            color: #202124;  /* Ensure text is visible */
        }

        .stTextInput>div>div>input:focus {
            outline: none;  /* Remove focus outline for cleaner look */
        }

        /* Header styling */
        h1 {
            font-size: 32px;
            font-weight: bold;
            text-align: center;
            color: #202124;
        }

        /* Success/Error messages styling */
        .stSuccess, .stError {
            text-align: center;
            font-size: 16px;
        }

        /* Center the image */
        .stImage {
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
    </style>
""", unsafe_allow_html=True)

# Display the image instead of the title
st.image("google.png", width=500, use_column_width=False)  # Use your own image URL or path

# Input field for the user to specify the target, styled like Google Search
new_target = st.text_input(
    "Enter the topic for the Wikipedia article:", 
    value="",
    max_chars=100,
    help="Search for any Wikipedia article."
)

# After the user enters a topic and presses enter
if new_target.strip():
    # Replace spaces with underscores for Wikipedia
    query = new_target.replace(" ", "_")
    # Send the update request to the Flask app
    response = requests.get(update_url, params={"q": query})
    
    if response.status_code == 200:
        st.success(f"Redirect successfully updated to: {response.text}")
        
        # Generate the Google search URL
        google_search_url = f"https://www.google.com/search?q={new_target.replace(' ', '+')}"
        
        # Display the clickable link to Google search (opens in a new tab)
        st.write("Click below to be redirected to Google search:")
        st.markdown(f"[Go to Google search]({google_search_url})", unsafe_allow_html=True)

    else:
        st.error(f"Failed to update redirect. Status code: {response.status_code}")

# Small info section like the footer in Google
st.write("---")
st.write("Test the current redirect:")
st.markdown("[Click here to test redirection](https://d83b1feb-dfea-4f0e-ad2f-3c342d968ac4-00-3gpxjdoc2m8am.kirk.replit.dev/redirect)", unsafe_allow_html=True)
