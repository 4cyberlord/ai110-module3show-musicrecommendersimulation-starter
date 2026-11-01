# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

This version is a CLI-first content-based recommender. It loads a small song catalog,
compares songs with a user's genre, mood, energy, and acoustic preferences, and prints
an explained ranking.

---

## How The System Works

Real platforms combine collaborative filtering (patterns from similar listeners) with
content-based filtering (song attributes such as genre, mood, tempo, and energy). This
simulation focuses on content-based matching so the behavior is easy to inspect. A
genre match is worth 2 points, a mood match is worth 1 point, energy similarity adds
up to 1 point, and acoustic preference adds up to 0.5 points. Every song is scored,
sorted highest to lowest, and returned with reasons.

Each song uses title, artist, genre, mood, energy, tempo, valence, danceability, and
acousticness. The user profile stores a favorite genre, favorite mood, target energy,
and whether the listener likes acoustic songs. This recipe may over-prioritize genre
and cannot understand lyrics, context, or a listener's changing mood.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
Loaded songs: 10

High-Energy Pop profile: {'genre': 'pop', 'mood': 'happy', 'energy': 0.8, 'likes_acoustic': False}
1. Sunrise City by Neon Echo - Score: 4.39
   Because: genre match (+2.0); mood match (+1.0); energy similarity (+0.98); acoustic preference (+0.41)
2. Gym Hero by Max Pulse - Score: 3.35
   Because: genre match (+2.0); energy similarity (+0.87); acoustic preference (+0.47)
3. Rooftop Lights by Indigo Parade - Score: 2.29
   Because: genre match (+2.0); energy similarity (+0.87); acoustic preference (+0.47)
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

I tested High-Energy Pop, Chill Lofi, and Deep Intense Rock profiles. Genre and mood
matches moved to the top, while energy broke ties between similar songs. Doubling the
energy weight made high-energy songs rise, but reduced variety.

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

The catalog has only 10 songs, so a profile can quickly run out of strong matches. The
genre bonus can create a filter bubble and hide a song with a better mood match. The
model also ignores lyrics, listening history, popularity, artist diversity, and context.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

I learned that a recommender is a chain of small decisions: represent preferences,
score each candidate, rank the scores, and explain the result. Even a tiny weighted
formula can feel intelligent because the output reflects recognizable musical ideas.
AI helped me draft and debug the logic, but I verified the CSV types, ranking order,
and sample output myself. Next I would add feedback from skips and likes, diversity
controls, and a larger catalog.

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



