import streamlit as st

st.set_page_config(page_title="Sébastien Stival – BI & Dashboarding",
                   page_icon="📊", layout="wide")

# --- Menu latéral ---
st.sidebar.title("Menu")
page = st.sidebar.radio("Aller à", ["Accueil", "Projets", "À propos", "Contact"])

def header():
    st.title("Transformer les données en décisions")
    st.caption("Portfolio de **Sébastien Stival** – Manager Gestion du Risque & Data Product Manager")
    st.markdown(
        """
        <div style="
             height: 6px;
             background: #E8F2EC;           /* même ton que secondaryBackgroundColor */
             border-radius: 9999px;
             margin: 0.5rem 0 1.5rem 0;">
        </div>
        """,
        unsafe_allow_html=True
    )
    st.image("logo.jpg", width=500)
    st.markdown("</div>", unsafe_allow_html=True)



# --- Pages ---
if page == "Accueil":
    header()
    st.write(
        "Bienvenue ! Je conçois des tableaux de bord **Power BI / Excel** pour les organismes "
        "de Sécurité sociale. Les visuels présentés sont **anonymisés**."
    )
    st.markdown("—")

elif page == "Projets":
    header()
    # Projet 1
    st.subheader("📊 Pilotage des dépenses de transport — CPAM des Pyrénées-Orientales")
    st.markdown(
        "**Contexte :** hausse des dépenses de transport.\n\n"
        "**Action :** modélisation des données, indicateurs clés, visualisations Power BI, diffusion sécurisée.\n\n"
        "**Impact :** accès immédiat aux dérives, meilleure priorisation des actions de régulation."
    )
    st.markdown("---")
    # Projet 2
    st.subheader("📊 Tableau de bord Qualité & Performance — organisme public (anonymisé)")
    st.markdown(
        "**Contexte :** indicateurs dispersés dans plusieurs fichiers Excel.\n\n"
        "**Action :** normalisation et consolidation → tableau de bord Power BI avec page spéciale CODIR.\n\n"
        "**Impact :** réduction du temps de préparation des réunions, fiabilisation des chiffres."
    )
    st.info("🔐 Visuels disponibles avec données fictives, sur demande.")

elif page == "À propos":
    header()
    st.write(
        "**Sébastien Stival**, Manager **Gestion du Risque** (CPAM des Pyrénées-Orientales, depuis 2019) "
        "et **Data Product Manager** certifié (DataScientest). 10 ans d’audit interne **ISO 9001**. "
        "Je transforme les besoins métier en outils de pilotage concrets."
    )
    st.write("**Valeurs :** confidentialité • rigueur • discrétion")

elif page == "Contact":
    header()
    st.write("📫 **Contact**")
    st.write("- Email : sebastien.stival@assurance-maladie.fr")
    st.write("- LinkedIn : https://www.linkedin.com (remplace par ton lien)")
    st.caption("Astuce : on ajoutera ici un bouton de téléchargement de CV ensuite.")
