import streamlit as st
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Set up the page
st.set_page_config(page_title="Mystery + Pronouns Game", page_icon="🕵️", layout="centered")
st.title("🕵️‍♀️ Grammar + Mystery Game Combo")

# -----------------------------
# Part 1: Pronoun Clarity Activity
# -----------------------------
st.header("📘 Activity 6: Pronoun-Antecedent Agreement")

st.subheader("1️⃣ Unclear Paragraph (Find the Problem 👀)")
unclear_paragraph = """
When Alex met Jordan at the library, he was carrying a large stack of books. 
He offered to help, but he dropped them on the floor. It made them both laugh, 
and he said he was clumsy. Then he told him to be more careful next time.
"""
st.write(unclear_paragraph)

st.subheader("✍️ 2️⃣ Rewrite the Paragraph (Clear Pronouns)")
user_rewrite = st.text_area("Rewrite the paragraph with clear pronouns and proper antecedents:", height=150)

if user_rewrite:
    doc = nlp(user_rewrite)
    st.success("✅ Thanks! Let's take a look at your pronoun usage.")

    # Extract pronouns and named entities
    pronouns = [token for token in doc if token.pos_ == "PRON"]
    ents = [ent.text for ent in doc.ents if ent.label_ in ["PERSON", "ORG"]]

    pronoun_texts = [p.text for p in pronouns]
    if pronouns:
        st.markdown("**Detected Pronouns:** " + ", ".join(pronoun_texts))
    else:
        st.markdown("✅ No pronouns detected.")

    if ents:
        st.markdown("**Named Entities (Possible Antecedents):** " + ", ".join(ents))
    else:
        st.markdown("⚠️ No named entities found.")

    # Check for clarity issues
    issues = []
    for token in pronouns:
        sentence = token.sent
        prior_ents = [ent.text for ent in sentence.ents if ent.label_ == "PERSON"]
        if not prior_ents:
            issues.append(f"❌ Pronoun '**{token.text}**' in sentence '**{sentence.text.strip()}**' might be unclear.")

    if issues:
        st.warning("🚨 Potential Clarity Issues Detected:")
        for issue in issues:
            st.markdown(issue)
    else:
        st.success("🎯 All pronouns seem to have clear antecedents. Great work!")

# Divider
st.markdown("---")

# -----------------------------
# Part 2: Murder Mystery Game
# -----------------------------
st.header("🕵️ Murder Mystery: Guess from Pronouns")

# Fixed answers
victim = "Professor Plum"
suspect = "Miss Scarlet"
weapon = "Candlestick"
location = "Library"

characters = ["Mr. Green", "Miss Scarlet", "Professor Plum", "Colonel Mustard", "Mrs. Peacock"]
weapons = ["Candlestick", "Revolver", "Rope", "Wrench", "Poison"]

# Story setup
if 'story' not in st.session_state:
    st.session_state.story = f"""
The storm had just begun when the guests arrived at Blackwood Mansion. Professor Plum came in late, soaked from the rain. Miss Scarlet didn’t look at **him**, not after what had happened between **them** last year.

Dinner was awkward. He spilled wine on **his** jacket and left the room. Then **she** followed **him** out a few minutes later, claiming she needed fresh air.

Mr. Green, known for **his** temper, argued with someone earlier that evening. **He** slammed the library door shut just before the scream echoed through the mansion.

When they all ran to the {location}, they found **someone** on the floor. **He** wasn’t moving. **She** was the first to speak, her voice trembling. A **{weapon}** was lying near the body — cold, heavy, and stained.
"""

# Show the story
st.subheader("📖 The Mystery (Pronoun Clues)")
doc_story = nlp(st.session_state.story)
pronouns_story = [token.text for token in doc_story if token.pos_ == "PRON"]
ents_story = [ent.text + " (" + ent.label_ + ")" for ent in doc_story.ents]

with st.expander("🔍 Show NLP Analysis of the Story"):
    st.markdown("**Pronouns in the Story:** " + ", ".join(pronouns_story))
    st.markdown("**Named Entities (People/Places):** " + ", ".join(ents_story))

st.markdown(st.session_state.story)

# Guess section
st.subheader("🔍 Your Guess:")
guess_victim = st.selectbox("👤 Who was the victim?", characters)
guess_suspect = st.selectbox("🚨 Who was the suspect?", characters)
guess_weapon = st.selectbox("🗡️ What was the weapon?", weapons)

if st.button("✅ Submit Your Guess"):
    if guess_victim == victim and guess_suspect == suspect and guess_weapon == weapon:
        st.success("🎉 Correct! You cracked the case!")
        st.balloons()
    else:
        st.error("❌ Not quite. Pay close attention to the pronouns and clues!")

# Reveal the answer
if st.button("🕵️ Reveal the Truth"):
    st.markdown(f"""
### 🧩 The Truth:
- **Victim**: {victim}  
- **Suspect**: {suspect}  
- **Weapon**: {weapon}  
- **Location**: {location}  

**Professor Plum** arrived late, soaked from the storm. He had a tense past with **Miss Scarlet**, who hadn’t spoken to him since last year.

During dinner, **Colonel Mustard** spilled wine and left. **Miss Scarlet** followed — but not for fresh air. She entered the **library**, where **Plum** had gone, and during an argument, struck him with a **candlestick**.
""")





