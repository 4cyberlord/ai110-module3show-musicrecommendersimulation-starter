from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        def score(song: Song) -> float:
            value = 0.0
            value += 2.0 if song.genre.lower() == user.favorite_genre.lower() else 0.0
            value += 1.0 if song.mood.lower() == user.favorite_mood.lower() else 0.0
            value += max(0.0, 1.0 - abs(song.energy - user.target_energy))
            if user.likes_acoustic:
                value += song.acousticness
            else:
                value += 1.0 - song.acousticness
            return value

        return sorted(self.songs, key=score, reverse=True)[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        reasons = []
        if song.genre.lower() == user.favorite_genre.lower():
            reasons.append("favorite genre match")
        if song.mood.lower() == user.favorite_mood.lower():
            reasons.append("favorite mood match")
        reasons.append(f"energy is {abs(song.energy - user.target_energy):.2f} from target")
        if user.likes_acoustic and song.acousticness >= 0.6:
            reasons.append("acoustic sound")
        elif not user.likes_acoustic and song.acousticness < 0.6:
            reasons.append("less acoustic sound")
        return "; ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    with open(csv_path, newline="", encoding="utf-8") as file:
        songs = []
        for row in csv.DictReader(file):
            for field in ("id",):
                row[field] = int(row[field])
            for field in ("energy", "tempo_bpm", "valence", "danceability", "acousticness"):
                row[field] = float(row[field])
            songs.append(row)
    print(f"Loaded songs: {len(songs)}")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons = []
    if song["genre"].lower() == user_prefs.get("genre", "").lower():
        score += 2.0
        reasons.append("genre match (+2.0)")
    if song["mood"].lower() == user_prefs.get("mood", "").lower():
        score += 1.0
        reasons.append("mood match (+1.0)")
    if "energy" in user_prefs:
        similarity = max(0.0, 1.0 - abs(song["energy"] - float(user_prefs["energy"])))
        score += similarity
        reasons.append(f"energy similarity (+{similarity:.2f})")
    if user_prefs.get("likes_acoustic") is not None:
        acoustic_match = song["acousticness"] if user_prefs["likes_acoustic"] else 1.0 - song["acousticness"]
        score += acoustic_match * 0.5
        reasons.append(f"acoustic preference (+{acoustic_match * 0.5:.2f})")
    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    ranked = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        ranked.append((song, score, "; ".join(reasons)))
    ranked.sort(key=lambda item: item[1], reverse=True)
    return ranked[:k]
