# Murder_mystery_pronoun_Antecedent-Agreement
---

````
# 🕵️ Grammar + Mystery Game Combo

An interactive and educational **NLP-based Streamlit app** that combines **grammar correction** (pronoun-antecedent clarity) with a **fun murder mystery game** where players solve a case using only **pronoun clues**.

---

## 🎯 What This App Does

1. **Activity 1: Pronoun-Antecedent Agreement**
   - Displays a paragraph with unclear pronouns.
   - Users rewrite the paragraph using clearer references.
   - NLP analysis detects pronouns and named entities.
   - Highlights possible pronoun clarity issues.

2. **Activity 2: Murder Mystery Game**
   - Players read a short mystery story.
   - Story is filled with pronoun cues and subtle hints.
   - Users guess the victim, suspect, and weapon.
   - App evaluates the guess and reveals the actual story resolution.

---

## 🛠️ Tech Stack

- **Python 3.7+**
- **[Streamlit](https://streamlit.io/)** – Web app UI
- **[spaCy](https://spacy.io/)** – NLP analysis
- Built-in Python libraries: `re`, `textwrap`
- Streamlit session state for storing dynamic content

---

## 📦 Installation

### Clone the repository

```bash
git clone https://github.com/harshii-02/grammar-mystery-game.git
cd grammar-mystery-game
````

### Create virtual environment (optional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

---

## 🚀 Run the App

```bash
streamlit run nlp2.py
```

Then open the app in your browser at `http://localhost:8501`.

---



---

## 🧠 Sample Activity Flow

### 🔤 Grammar Fixing

> Original:
> “When Alex met Jordan at the library, **he** was carrying a large stack of books...”
>
> Rewrite:
> “When Alex met Jordan at the library, **Alex** was carrying a large stack of books...”

### 🕵️ Mystery Solving

> Who killed Professor Plum? With what? And where?
> Use the pronouns to infer the truth.

---

## ✅ Dependencies

```txt
streamlit
spacy
```

After installing, also run:

```bash
python -m spacy download en_core_web_sm
```

---

## 📬 Author

Created with ❤️ by [@harshii-02](https://github.com/harshii-02)

---



---

