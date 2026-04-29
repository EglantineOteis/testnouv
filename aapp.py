# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 14:24:33 2026

@author: eglantine.masseau
"""

import streamlit as st

# ----------------------------
# CONFIG
# ----------------------------
st.set_page_config(page_title="Outil Bas Carbone", layout="wide")

st.title("🌱 Outil Bas Carbone APS/APD")

# ----------------------------
# SIDEBAR
# ----------------------------
st.sidebar.header("Paramètres projet")

surface = st.sidebar.number_input("Surface (m²)", value=1000)

chauffage = st.sidebar.selectbox(
    "Chauffage",
    ["PAC air/eau", "PAC géothermique", "Chaudière gaz", "Chaudière biomasse"]
)

ventilation = st.sidebar.selectbox(
    "Ventilation",
    ["double flux", "simple flux"]
)

# ----------------------------
# CALCUL SIMPLE
# ----------------------------
CVC_DATA = {
    "PAC air/eau": 45,
    "PAC géothermique": 25,
    "Chaudière gaz": 85,
    "Chaudière biomasse": 55,
    "double flux": 8,
    "simple flux": 15,
}

kwh = 30  # base

kwh += CVC_DATA.get(chauffage, 0)
kwh += CVC_DATA.get(ventilation, 0)

ic_energie = kwh * 0.0485
ic_batiment = 5
ic_total = ic_energie + ic_batiment

# ----------------------------
# DASHBOARD
# ----------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Ic énergie", round(ic_energie, 2))
col2.metric("Ic bâtiment", ic_batiment)
col3.metric("Ic total", round(ic_total, 2))
col4.metric("Cep", round(kwh, 1))

st.divider()

# ----------------------------
# ANALYSE
# ----------------------------
st.subheader("Analyse")

if ic_energie < 5:
    st.success("Projet conforme RE2020")
else:
    st.warning("Projet à optimiser")

# ----------------------------
# INFOS PROJET
# ----------------------------
st.subheader("Données projet")

st.json({
    "surface": surface,
    "chauffage": chauffage,
    "ventilation": ventilation
})