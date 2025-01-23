import os
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv
from prompt import SYSTEM_MESSAGE

# Chargement des variables d'environnement
load_dotenv()

# Configuration de Streamlit
st.set_page_config(page_title="Bible Verse Finder", page_icon="📖")

# Initialisation du modèle DeepSeek
def init_model():
    return ChatOpenAI(
        api_key=os.getenv("DEEPSEEK_API_KEY"),
        base_url="https://api.deepseek.com/v1",  # URL de base de DeepSeek
        model="deepseek-chat",  # Modèle DeepSeek
        temperature=0.3
    )

# Prompt personnalisé
def create_prompt_template():
    return PromptTemplate(
        input_variables=["user_input"],
        template=f"""
        {SYSTEM_MESSAGE}
        
        Contexte utilisateur: {{user_input}}
        Réponse:
        """
    )

# Interface Streamlit
def main():
    st.title("🔍 Trouveur de Versets Bibliques - Louis Segond")
    
    user_input = st.text_area("Décrivez votre contexte biblique:", height=100)
    
    if st.button("Trouver le verset"):
        if user_input:
            with st.spinner("Recherche dans les Écritures..."):
                try:
                    llm = init_model()
                    prompt_template = create_prompt_template()
                    
                    # Nouvelle méthode recommandée : utiliser une chaîne Runnable
                    chain = (
                        {"user_input": RunnablePassthrough()} 
                        | prompt_template 
                        | llm
                    )
                    
                    # Utilisation de `invoke` pour exécuter la chaîne
                    response = chain.invoke(user_input)
                    
                    # Extraire uniquement le texte brut du verset
                    verse_text = response.content
                    
                    # Afficher le résultat
                    st.subheader("Résultat:")
                    st.write(verse_text)  # Affiche uniquement le texte brut
                except Exception as e:
                    st.error(f"Une erreur est survenue: {str(e)}")
        else:
            st.warning("Veuillez entrer une description")

if __name__ == "__main__":
    main()