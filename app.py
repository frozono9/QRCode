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

        /* Button styling */
        .stButton>button {
            background-color: #4285F4;
            color: white;
            border-radius: 24px;
            padding: 12px 30px;
            font-size: 16px;
            border: none;
        }

        .stButton>button:hover {
            background-color: #357ae8;
        }

        /* Header styling */
        h1 {
            font-size: 32px;
            font-weight: bold;
            text-align: center;
            color: #202124;
        }

        /* Markdown styling */
        .stMarkdown {
            font-size: 14px;
            color: #5f6368;
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
            cursor: pointer; /* Make the image clickable */
        }
    </style>
""", unsafe_allow_html=True)

# Display the image at the top, centered
st.image("google.png", width=500, use_container_width=False)  # This is the image that stays at the top and centered

# Input field for the user to specify the target, styled like Google Search
new_target = st.text_input(
    "Enter the topic for the Wikipedia article:", 
    value="",
    max_chars=100,
    help="Search for any Wikipedia article."
)

# Triggered automatically when Enter is pressed in the input field
if new_target.strip():
    # Replace spaces with underscores for Wikipedia
    query = new_target.replace(" ", "_")
    # Send the update request to the Flask app
    response = requests.get(update_url, params={"q": query})
    
    if response.status_code == 200:
        st.success(f"Redirect successfully updated to: {response.text}")
        
        # Generate the Google search URL
        google_search_url = f"https://www.google.com/search?q={new_target.replace(' ', '+')}"
        
        # Display image as clickable and redirect to Google search
        st.markdown(f"""
            <a href="{google_search_url}" target="_blank">
                <img src="image.png" width="500" style="display:block;margin-left:auto;margin-right:auto;cursor:pointer;">
            </a>
        """, unsafe_allow_html=True)

    else:
        st.error(f"Failed to update redirect. Status code: {response.status_code}")

# Small info section like the footer in Google
st.write("---")
st.write("Test the current redirect:")
st.markdown("[Click here to test redirection](https://d83b1feb-dfea-4f0e-ad2f-3c342d968ac4-00-3gpxjdoc2m8am.kirk.replit.dev/redirect)", unsafe_allow_html=True)
