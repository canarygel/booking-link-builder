import streamlit as st
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

st.set_page_config(page_title="Booking Link Builder", layout="centered")

st.title("🏨 Booking Link Builder")

st.write("Convert a base booking link into a dynamic link with parameters.")

# Input base URL
base_url = st.text_input("Enter base booking URL")

# Parameter inputs
st.subheader("Booking Parameters")

arrival_date = st.text_input("Check-in date (YYYY-MM-DD)")
departure_date = st.text_input("Check-out date (YYYY-MM-DD)")
adults = st.number_input("Adults", min_value=1, value=2)
children = st.number_input("Children", min_value=0, value=0)
rooms = st.number_input("Rooms", min_value=1, value=1)

def build_url(base, params):
    url_parts = urlparse(base)
    query = parse_qs(url_parts.query)
    
    # Merge existing + new params
    query.update(params)
    
    # Flatten query
    flat_query = {k: v if isinstance(v, list) else [str(v)] for k, v in query.items()}
    
    new_query = urlencode(flat_query, doseq=True)
    
    return urlunparse((
        url_parts.scheme,
        url_parts.netloc,
        url_parts.path,
        url_parts.params,
        new_query,
        url_parts.fragment
    ))

if st.button("Generate Dynamic Link"):
    if not base_url:
        st.error("Please enter a base URL")
    else:
        params = {
            "arrivalDate": arrival_date,
            "departureDate": departure_date,
            "adults": adults,
            "children": children,
            "rooms": rooms
        }

        # Remove empty values
        params = {k: v for k, v in params.items() if v not in ["", None]}

        dynamic_url = build_url(base_url, params)

        st.subheader("Generated Link")
        st.code(dynamic_url)
        st.success("Copy and share this link")
