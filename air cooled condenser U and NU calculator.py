
import streamlit as st
import math
from coolprop.coolprop import PropSI
st.title("Heat Transfer Coefficient and Nusselt Number Calculator for Air-Cooled Condenser")

st.header("Input Parameters")

# User Inputs
D_mm = st.number_input("Tube Outer Diameter (mm)", value=9.525)
D_o = D_mm / 1000  # convert to meters
L = st.number_input("Coil Length (m)", value=2.5)
H = st.number_input("Coil Height (m)", value=2.032)
airflow = st.number_input("Air Volume Flow Rate (m³/s)", value=14.0)
fpi = st.number_input("Fin Density (FPI)", value=10)
coil_thickness = st.number_input("Coil Thickness / Depth (m)", value=0.2)
rows = st.number_input("Number of Rows", value=4)
T_air = st.number_input("Air Inlet Temperature (°C)", value=50.0)
T_freon_in = st.number_input("Freon Superheated Temp In (°C)", value=85.0)

# Air properties at film temp (~60°C)
rho_air = 1.06       # kg/m³
mu_air = 2.1e-5      # Pa·s
k_air = 0.028        # W/m·K
cp_air = 1006        # J/kg·K
Pr_air = cp_air * mu_air / k_air

# Face area and velocity
face_area = L * H
v_air = airflow / face_area

# Reynolds number
Re_air = (rho_air * v_air * D_o) / mu_air

# Nusselt number using empirical correlation (Kays & London)
# For staggered 4-row tube bank: C = 0.41, m = 0.6
C = 0.41
m = 0.6
Nu_air = C * Re_air**m * Pr_air**(1/3)
h_air = Nu_air * k_air / D_o

# Refrigerant-side (assume turbulent single-phase)
Re_ref = 20000
Pr_ref = 4.0
k_ref = 0.08  # W/m·K
Nu_ref = 0.023 * Re_ref**0.8 * Pr_ref**0.4
h_ref = Nu_ref * k_ref / D_o

# Overall heat transfer coefficient
U = 1 / (1/h_air + 1/h_ref)

# Display results
st.header("Results")
st.write(f"**Air Face Velocity:** {v_air:.2f} m/s")
st.write(f"**Air Reynolds Number:** {Re_air:.0f}")
st.write(f"**Air Nusselt Number:** {Nu_air:.2f}")
st.write(f"**Air-side h:** {h_air:.1f} W/m²·K")
st.write(f"**Refrigerant-side Nu:** {Nu_ref:.2f}")
st.write(f"**Refrigerant-side h:** {h_ref:.1f} W/m²·K")
st.write(f"**Overall Heat Transfer Coefficient U:** {U:.1f} W/m²·K")
