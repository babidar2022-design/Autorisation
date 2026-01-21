import streamlit as st
import datetime

st.set_page_config(page_title="Dépôt Autorisation Agence Recrutement", layout="wide")

st.title("📂 Demande d'Autorisation d'Exercer - Article 477")
st.info("Conformément à la loi 65-99 relative au Code du Travail.")

# --- SECTION 1: IDENTIFICATION DU REPRÉSENTANT ---
st.header("1. Identification du Représentant Légal")
col1, col2 = st.columns(2)
with col1:
    nom = st.text_input("Nom et Prénom", placeholder="ex: SRAIDI Saad")
    nationalite = st.text_input("Nationalité", placeholder="Marocaine")
    cin = st.text_input("N° CIN / Passeport", placeholder="ex: T232789")
with col2:
    tel = st.text_input("Téléphone", placeholder="06XXXXXXXX")
    email = st.text_input("E-mail", placeholder="contact@agence.ma")
    adresse_perso = st.text_area("Adresse personnelle complète")

# --- SECTION 2: INFORMATIONS SUR L'ENTREPRISE ---
st.header("2. Informations sur l'Agence")
col3, col4 = st.columns(2)
with col3:
    denomin = st.text_input("Dénomination sociale", placeholder="ex: WELL JOB S.A.R.L")
    ice = st.text_input("ICE (Identifiant Commun de l’Entreprise)")
    rc = st.text_input("N° Registre de Commerce (RC)")
with col4:
    cnss = st.text_input("N° Affiliation CNSS")
    banque = st.text_input("Banque et Agence")
    rib = st.text_input("RIB (24 chiffres)")

# --- SECTION 3: NATURE DE L'ACTIVITÉ ---
st.header("3. Activités visées")
activite_1 = st.checkbox("Rapprochement des offres et demandes d'emploi")
activite_2 = st.checkbox("Services favorisant l'insertion professionnelle")
activite_3 = st.checkbox("Travail temporaire (Mise à disposition de salariés)")

# --- SECTION 4: UPLOAD DES PIÈCES (AVEC INTERCALAIRES) ---
st.header("4. Dossier de pièces jointes")
st.caption("Veuillez uploader chaque pièce sous son intercalaire dédié.")

pieces = [
    "01 - Demande d'autorisation (F1 signé/légalisé)",
    "02 - Fiche de renseignements (F2)",
    "03 - Statuts de la société",
    "04 - Registre de Commerce (Modèle J)",
    "05 - Attestation d'affiliation CNSS",
    "06 - Relevé d'Identité Bancaire (RIB)",
    "07 - Copie CIN / Passeport",
    "08 - Liste nominative des associés",
    "09 - Liste des mandataires habilités",
    "10 - Justificatif de dépôt du capital social"
]

dossier = {}
for piece in pieces:
    dossier[piece] = st.file_uploader(f"Téléverser : {piece}", type=["pdf", "jpg", "png"])

# --- BOUTON DE SOUMISSION ---
if st.button("🚀 Soumettre le dossier complet"):
    if nom and denomin and all(dossier.values()):
        st.success(f"Dossier de {denomin} enregistré avec succès le {datetime.date.today()}.")
    else:
        st.error("Veuillez remplir tous les champs et uploader toutes les pièces obligatoires.")