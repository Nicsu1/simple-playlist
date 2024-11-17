import streamlit as st
# Mock music database (initially pre-filled)
MUSIC_DATABASE = [
    {"title": "Blinding Lights", "artist": "The Weeknd", "mood": "Energetic", "file": "mp3/1.mp3"},
    {"title": "Shallow", "artist": "Lady Gaga & Bradley Cooper", "mood": "Romantic", "file": "mp3/2.mp3"},
    {"title": "Someone You Loved", "artist": "Lewis Capaldi", "mood": "Sad", "file": "mp3/3.mp3"}
]
user_playlists = {}
def browse_music():
    st.header("Browse Music by Mood")
    moods = sorted(set(song["mood"] for song in MUSIC_DATABASE))
    selected_mood = st.selectbox("Select a mood:", options=moods)
    filtered_songs = [song for song in MUSIC_DATABASE if song["mood"] == selected_mood]

    if filtered_songs:
        st.subheader(f"Songs for mood: {selected_mood}")
        for song in filtered_songs:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"🎵 **{song['title']}** - {song['artist']}")
            with col2:
                if st.button(f"Play '{song['title']}'", key=song["title"]):
                    st.audio(song["file"], format="audio/mp3")
    else:
        st.write("No songs found for this mood.")
def create_playlist():
    st.header("Create Your Playlist")
    playlist_name = st.text_input("Enter a playlist name:")
def view_playlists():
    st.header("Your Playlists")


def upload_music():
    st.header("Upload Your Music")
    uploaded_file = st.file_uploader("Upload MP3 file", type=["mp3"])
    song_title = st.text_input("Enter the song title:")
    artist_name = st.text_input("Enter the artist name:")
    song_mood = st.selectbox("Select the mood of the song:", ["Energetic", "Romantic", "Sad", "Happy", "Relaxed"])
def main():
    st.title("🎵 Music Playlist App (Like Spotify) 🎧")
    st.sidebar.header("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Browse Music", "My Playlists", "Create Playlist", "Upload Music"])
    if page == "Home":
        st.header("Welcome to Your Personal Music Playlist App!")
        st.write("🎶 Explore music by mood, create playlists, upload your music, and enjoy listening!")
    elif page == "Browse Music":
        browse_music()
    elif page == "My Playlists":
        view_playlists()
    elif page == "Create Playlist":
        create_playlist()
    elif page == "Upload Music":
        upload_music()
if __name__ == "__main__":
    main()

