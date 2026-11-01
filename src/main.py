"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

try:
    from .recommender import load_songs, recommend_songs
except ImportError:  # Supports running the file directly from the src directory.
    from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    profiles = {
        "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.8, "likes_acoustic": False},
        "Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.4, "likes_acoustic": True},
        "Deep Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.9, "likes_acoustic": False},
    }
    for name, user_prefs in profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)
        print(f"\n{name} profile: {user_prefs}")
        print("Top recommendations:")
        for position, (song, score, explanation) in enumerate(recommendations, 1):
            print(f"{position}. {song['title']} by {song['artist']} - Score: {score:.2f}")
            print(f"   Because: {explanation}")


if __name__ == "__main__":
    main()
