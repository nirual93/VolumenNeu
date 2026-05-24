import streamlit as st
import math

# --- DESIGN & TITEL ---
st.set_page_config(page_title="Filterkies-Rechner", page_icon="🪨")
st.title("🪨 Volumen-Rechner: Filterkiesschüttung")
st.subheader("Berechnung des 1,5-fachen Zylindervolumens")
st.write("---")

# --- 1. EINGABEFELDER ---
# Die Werte werden direkt in Metern abgefragt.
durchmesser_m = st.number_input("Bohrlochdurchmesser in Metern (z.B. 0.15 für 15 cm)", min_value=0.0, value=0.15, step=0.01)
maechtigkeit_m = st.number_input("Mächtigkeit der wassererfüllten Filterkiesschüttung in Metern", min_value=0.0, value=5.0, step=0.1)

st.write("---")

# --- 2. BUTTON & BERECHNUNG ---
if st.button("Volumen berechnen", type="primary"):
    
    if durchmesser_m <= 0 or maechtigkeit_m <= 0:
        st.error("❌ Fehler: Bitte geben Sie Werte größer als 0 ein.")
    else:
        # Radius ermitteln (Durchmesser geteilt durch 2)
        radius_m = durchmesser_m / 2
        
        # Die eigentliche Mathematik (Volumen des Zylinders in Kubikmetern)
        zylinder_volumen_m3 = math.pi * (radius_m ** 2) * maechtigkeit_m
        
        # Das Volumen mit dem Faktor 1,5 multiplizieren
        ziel_volumen_m3 = zylinder_volumen_m3 * 1.5
        
        # Umrechnung in Liter für die Praxis (1 m³ = 1000 Liter)
        zylinder_volumen_l = zylinder_volumen_m3 * 1000
        ziel_volumen_l = ziel_volumen_m3 * 1000
        
        # --- 3. ERGEBNIS-AUSGABE ---
        st.success("✅ Berechnung erfolgreich!")
        
        # Übersichtliche Darstellung in zwei Spalten
        col1, col2 = st.columns(2)
        
        col1.metric(
            label="Zylindervolumen (Einfach)", 
            value=f"{zylinder_volumen_m3:.3f} m³", 
            delta=f"≙ {zylinder_volumen_l:.1f} Liter", 
            delta_color="off"
        )
        
        col2.metric(
            label="Abpumpvolumen (1,5-fach)", 
            value=f"{ziel_volumen_m3:.3f} m³", 
            delta=f"≙ {ziel_volumen_l:.1f} Liter", 
            delta_color="normal"
        )
