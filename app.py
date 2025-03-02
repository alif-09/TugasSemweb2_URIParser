"""
Tugas Semantik Web
Nama  : Alif Al Husaini
NPM   : 140810220036
Deskripsi: Aplikasi Streamlit untuk parsing URI menggunakan regex.
"""

import streamlit as st
from uriParser import parse_uri

# konfigurasi halaman
st.set_page_config(page_title="🔍 URI Parser", page_icon="🔗")

# identitas mahasiswa
st.sidebar.title("📌 Assignment Info")
st.sidebar.write("**Tugas Semantik Web**")
st.sidebar.write("**Nama:** Alif Al Husaini")
st.sidebar.write("**NPM:** 140810220036")
st.sidebar.write("**Universitas Padjadjaran**")

st.title("🔍 URI Parser with Regex")

# Input URI dari pengguna
uri_input = st.text_input("Enter a URI:", "https://user:password@example.com:8080/docs/resource.txt?name=value#section1")

if st.button("Parse URI"):
    result = parse_uri(uri_input)
    
    if result: 
        st.success("✅ URI parsed successfully!")

        # menampilkan hasil dalam field terpisah
        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Scheme (Protocol):", result.get("scheme", ""))
            st.text_input("User Info:", result.get("userinfo", ""))
            st.text_input("Host (Domain):", result.get("host", ""))
        with col2:
            st.text_input("Port:", result.get("port", ""))
            st.text_input("Path:", result.get("path", ""))
            st.text_input("Query:", result.get("query", ""))
            st.text_input("Fragment:", result.get("fragment", ""))
    else: 
        st.error("⚠️ Invalid URI! Please enter a valid URI.")
