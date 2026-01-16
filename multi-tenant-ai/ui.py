import streamlit as st
import requests

API_URL = "http://localhost:8000/ask"

# Mapping clients → API Keys
CLIENT_KEYS = {
    "Client A": "tenantA_key",
    "Client B": "tenantB_key"
}

st.set_page_config(page_title="Mini SaaS IA", layout="centered")

st.title("🤖 Mini SaaS IA – Test technique")
st.write("Chaque client interroge uniquement **ses propres documents**.")

# =========================
# Sélection du client
# =========================
client = st.selectbox("Sélectionnez le client :", list(CLIENT_KEYS.keys()))

# =========================
# Question utilisateur
# =========================
question = st.text_area("Votre question :", height=120)

# =========================
# Bouton envoyer
# =========================
if st.button("Envoyer la question"):
    if not question.strip():
        st.warning("Veuillez entrer une question.")
    else:
        headers = {
            "X-API-KEY": CLIENT_KEYS[client]
        }

        payload = {
            "question": question
        }

        try:
            response = requests.post(API_URL, json=payload, headers=headers)

            if response.status_code == 200:
                data = response.json()
                st.success("Réponse de l'agent :")
                st.write(data["answer"])
            else:
                st.error(f"Erreur API : {response.status_code}")

        except Exception as e:
            st.error(f"Erreur de connexion à l'API : {e}")
