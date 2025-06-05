import streamlit as st

# Page config
st.set_page_config(
    page_title="HEAL – Grief Support Agent",
    page_icon="🕊️",
    layout="centered"
)

# Styling
st.markdown("""
    <style>
    .main {
        background-color: #f7f9fa;
    }
    .title {
        text-align: center;
        font-size: 2.5em;
        font-weight: bold;
        color: #333;
    }
    .subtitle {
        text-align: center;
        font-size: 1.2em;
        color: #888;
        margin-bottom: 1em;
    }
    </style>
""", unsafe_allow_html=True)

# Title and subtitle
st.markdown('<div class="title">🕊️ HEAL</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Helping Emotions Adjust to Loss</div>', unsafe_allow_html=True)

# Description
st.markdown("""
**HEAL** is a supportive guide for individuals facing the immediate aftermath of a loss.

We assist with:

- Delivering notifications with compassion  
- Planning meaningful and respectful funeral arrangements  
- Providing emotional guidance during moments of grief  

HEAL is here to walk with you through the difficult first steps of loss — offering both practical help and a comforting presence when it matters most.
""")

# Divider
st.markdown("---")

# Contact Form
st.subheader("💬 Request Support")

with st.form("support_form"):
    name = st.text_input("Your Full Name")
    relationship = st.text_input("Your Relationship to the Deceased")
    contact = st.text_input("Phone or Email")
    needs = st.text_area("How can HEAL support you right now?")
    submitted = st.form_submit_button("Submit Request")

    if submitted:
        st.success(f"Thank you, {name}. HEAL will reach out to support you shortly.")

# Footer
st.markdown("---")
st.caption("© 2025 HEAL Support Services • All rights reserved.")
