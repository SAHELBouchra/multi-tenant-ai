# multi-tenant-ai

Ce projet met en place un backend IA multi-locataires utilisant FastAPI et Google Gemini. Chaque client dispose de documents isolés, et l'IA répond aux questions en se basant uniquement sur le contexte spécifique au client. Une interface Streamlit est fournie comme interface frontend.

 ## Requirements
- Python 3.10+
- FastAPI
- Uvicorn
- Streamlit
- google-generativeai

## Installation

```bash
git clone https://github.com/SAHELBouchra/multi-tenant-ai.git
cd multi-tenant-ai
pip install -r backend/requirements.txt

```
---

##  a/ Comment lancer l’interface (UI)

```md
## Run the UI (Streamlit)

```bash
cd ui
streamlit run ui.py
```
The UI will be available at:
http://localhost:8501

##  b/ Comment lancer le backend

```md
## Run the Backend (FastAPI)

```bash
cd backend
uvicorn main:app --reload

```
The API will be available at:
http://127.0.0.1:8000

## c/ Pour tester :
- Change "client_a" → "client_b"
- Pose la question
- Cliquer sur envoyer la question
- Observe la réponse

==>La même question produit des réponses différentes selon le contexte du client.

## Résumé de l'approche

Ce projet suit une architecture modulaire et évolutive :
- FastAPI gère l'orchestration des requêtes
- Un système multi-tenant basé sur les dépendances isole les clients
- Les documents spécifiques à chaque client sont chargés dynamiquement
- Un agent IA construit des invites et interroge Gemini
- Streamlit fournit une interface frontend légère

Cette approche permet des réponses IA personnalisées sans entraîner plusieurs modèles.


