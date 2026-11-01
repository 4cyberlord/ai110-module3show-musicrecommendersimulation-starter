# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeFinder 1.0**

---

## 2. Intended Use  

It suggests songs for classroom exploration from a stated taste profile. It is not a
production service or a replacement for a real music platform.

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

The model gives 2 points for a genre match and 1 point for a mood match. It adds up to
1 point when energy is close to the user's target and up to 0.5 points for acoustic
preference. It ranks every song by total score and reports the matching reasons.

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

The catalog has 10 songs with genre, mood, energy, tempo, valence, danceability, and
acousticness. It includes pop, lofi, rock, ambient, jazz, synthwave, and indie pop.
This hand-written dataset is small and does not represent all music.

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

It works well when the profile resembles a catalog row, such as happy pop or chill
lofi. The explanations make it clear why an exact genre and mood match wins.

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Genre receives the largest single bonus, so it can over-prioritize a genre even when
another song has a closer energy or mood. Small genres are underrepresented. The model
has no lyrics, listening history, popularity, artist diversity, or skip data.

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

## 7. Evaluation  

I tested High-Energy Pop, Chill Lofi, and Deep Intense Rock. Pop favored Sunrise City
and Rooftop Lights; lofi favored Midnight Coding and Library Rain; rock favored Storm
Runner. Genre and mood bonuses shift the top results, while energy orders close
matches. Doubling the energy weight made high-energy songs rise, but reduced variety.

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---

## 8. Future Work  

I would add more songs, learn weights from likes and skips, and add a diversity penalty
so the top results are not all from one genre or artist.

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

My biggest learning moment was seeing that scoring and ranking are separate jobs. AI
helped me draft a clean first version, but I double-checked types and output against
the tests. I was surprised that a few transparent rules could feel like a real vibe
match. Next I would add collaborative signals and compare several scoring strategies.
