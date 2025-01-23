
# Bible-AI 📖

Bible-AI est une application intelligente qui aide les utilisateurs à trouver des versets bibliques en fonction d'un contexte donné. L'application utilise l'API DeepSeek, LangChain et Streamlit pour analyser le contexte fourni par l'utilisateur et renvoyer les versets correspondants de la Bible Louis Segond.

## Fonctionnalités ✨

- **Recherche de versets par contexte** : Décrivez une situation ou un thème, et l'application trouvera les versets bibliques pertinents.
- **Basé sur la Bible Louis Segond** : Les résultats sont tirés de la version authentique de la Bible Louis Segond.
- **Interface simple et intuitive** : Une interface utilisateur conviviale grâce à Streamlit.
- **Technologie IA avancée** : Utilisation de l'API DeepSeek pour une compréhension précise du contexte.

## Technologies utilisées 🛠️

- **DeepSeek** : Modèle de langage pour comprendre le contexte et trouver les versets appropriés.
- **LangChain** : Framework pour créer des chaînes de traitement de langage naturel.
- **Streamlit** : Framework pour créer des interfaces utilisateur web interactives.
- **Python** : Langage de programmation principal.

## Installation 🚀

### Prérequis

- Python 3.8 ou supérieur
- Un compte DeepSeek pour obtenir une clé API

### Étapes d'installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/Shalom-302/Bible-AI.git
   cd Bible-AI
   ```

2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

3. Configurez votre clé API DeepSeek :
   - Créez un fichier `.env` à la racine du projet.
   - Ajoutez votre clé API DeepSeek dans le fichier `.env` :
     ```env
     DEEPSEEK_API_KEY=votre_cle_api_ici
     ```

4. Exécutez l'application :
   ```bash
   streamlit run main.py
   ```

5. Ouvrez votre navigateur et accédez à l'application :
   ```
   http://localhost:8501
   ```

## Utilisation 🖥️

1. Décrivez votre contexte biblique dans la zone de texte.
2. Cliquez sur "Trouver le verset".
3. L'application affichera les versets correspondants de la Bible Louis Segond.

## Exemple de résultat 📜

**Contexte utilisateur :**
```
Un verset qui parle de l'amour de Dieu pour le monde.
```

**Résultat :**
```
Jean 3:16 - Car Dieu a tant aimé le monde qu'il a donné son Fils unique, afin que quiconque croit en lui ne périsse point, mais qu'il ait la vie éternelle.
```

## Structure du projet 📂

```
Bible-AI/
├── .env                     # Fichier de configuration pour la clé API
├── main.py                  # Script principal de l'application
├── requirements.txt         # Dépendances du projet
└── prompt.py                # Fichier contenant les prompts système
```

## Contribuer 🤝

Les contributions sont les bienvenues ! Voici comment vous pouvez contribuer :

1. Forkez le projet.
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/NouvelleFonctionnalité`).
3. Committez vos changements (`git commit -m 'Ajouter une nouvelle fonctionnalité'`).
4. Pushez la branche (`git push origin feature/NouvelleFonctionnalité`).
5. Ouvrez une Pull Request.

## Licence 📄

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

## Auteur 🧑‍💻

- **Shalom-302** - [GitHub](https://github.com/Shalom-302)

---

## Remerciements 🙏

- Merci à l'équipe de **DeepSeek** pour leur API puissante.
- Merci à la communauté **LangChain** pour leur framework incroyable.
- Merci à **Streamlit** pour rendre la création d'interfaces utilisateur si simple.

```

---

### Comment ajouter ce fichier à votre projet

1. Créez un fichier `README.md` à la racine de votre projet.
2. Copiez le contenu ci-dessus dans ce fichier.
3. Enregistrez et poussez les modifications sur GitHub :
   ```bash
   git add README.md
   git commit -m "Ajout du fichier README.md"
   git push origin main
   ```

