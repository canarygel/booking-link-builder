import streamlit as st
from urllib.parse import urlparse, urlencode, urlunparse

st.set_page_config(page_title="Booking Link Template Builder", layout="centered")

st.title("🏨 Booking Link Template Builder")

st.write("Convert a base booking URL into a dynamic template with placeholders.")

# Input base URL
base_url = st.text_input("Enter base booking URL")

st.subheader("Template Parameters")

# Template placeholders (not real values)
arrival_date_key = st.text_input("Arrival date parameter name", value="arrivalDate")
departure_date_key = st.text_input("Departure date parameter name", value="departureDate")
adults_key = st.text_input("Adults parameter name", value="adults")
children_key = st.text_input("Children parameter name", value="children")
rooms_key = st.text_input("Rooms parameter name", value="rooms")

def build_template_url(base):
    url_parts = urlparse(base)

    template_params = {
        arrival_date_key: "{arrivalDate}",
        departure_date_key: "{departureDate}",
        adults_key: "{adults}",
        children_key: "{children}",
        rooms_key: "{rooms}"
    }

    query_string = urlencode(template_params)

    return urlunparse((
        url_parts.scheme,
        url_parts.netloc,
        url_parts.path,
        url_parts.params,
        query_string,
        url_parts.fragment
    ))

if st.button("Generate Template Link"):
    if not base_url:
        st.error("Please enter a base URL")
    else:
        template_url = build_template_url(base_url)

        st.subheader("Template Link")
        st.code(template_url)

        st.success("This is a reusable template link with placeholders.")
