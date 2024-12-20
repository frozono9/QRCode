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

# Initialize session state to store the selected link type
if "link_type" not in st.session_state:
    st.session_state.link_type = None

# Dropdown for selecting the type of link (shown only if no type is selected yet)
if st.session_state.link_type is None:
    link_type = st.selectbox(
        "Select the type of link you want to redirect to:",
        ["Wikipedia", "Google Images", "Twitter", "Google Search"]
    )
    if link_type:  # Store the selected type in session state
        st.session_state.link_type = link_type

# Function to construct the URL based on the selected link type
def construct_url(link_type, query):
    if link_type == "Wikipedia":
        # Wikipedia requires underscores for spaces
        return f"https://en.wikipedia.org/wiki/{query.replace(' ', '_')}"
    elif link_type == "Google Images":
        # Google Images requires a search query with "+" for spaces
        return f"https://www.google.com/search?tbm=isch&q={query.replace(' ', '+')}"
    elif link_type == "Twitter":
        # Twitter requires spaces to be encoded as "%20"
        return f"https://twitter.com/search?q={query.replace(' ', '%20')}&src=typed_query"
    elif link_type == "Google Search":
        # Google Search also uses "+" for spaces
        return f"https://www.google.com/search?q={query.replace(' ', '+')}"

# Display the image and ensure it's centered
st.image("google.png", width=500, use_container_width=False)

# Input field for the user to specify the target
new_target = st.text_input(
    "Enter your search term or topic:", 
    value="",
    max_chars=100,
    help="Provide your search term here."
)

# After the user enters a topic and presses enter
if new_target.strip():
    # Construct the target URL
    target_url = construct_url(st.session_state.link_type, new_target)
    
    # Send the update request to the Flask app
    response = requests.get(update_url, params={"q": target_url})
    
    if response.status_code == 200:
        st.success(f"Redirect successfully updated to: {target_url}")
        
        # Always display the correct redirect for the selected platform
        st.write(f"You will be redirected to: {st.session_state.link_type}")
        st.markdown(f"[Click here to go to the link]({target_url})")
    else:
        st.error(f"Failed to update redirect. Status code: {response.status_code}")

# Small info section like the footer in Google
st.write("---")
st.write("Test the current redirect:")
st.markdown("[Click here to test redirection](https://d83b1feb-dfea-4f0e-ad2f-3c342d968ac4-00-3gpxjdoc2m8am.kirk.replit.dev/redirect)", unsafe_allow_html=True)
