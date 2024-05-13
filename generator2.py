import tkinter as tk
from lyricsgenius import Genius

def extract_lyrics():
    # Get the song name and artist from the text boxes
    song = song_entry.get()
    artist = artist_entry.get()

    # Create a Genius object and search for the song
    genius = Genius("ERTT4AYmrA-Fyht1i8U-a5c042FQSN4gtMZh-5tPdU3gyGO6LyD9UFMxzbC0Zwuh")
    song = genius.search_song(song, artist)

    # Display the lyrics in the text box
    if song is not None:
        lyrics_text.delete(1.0, tk.END)
        lyrics_text.insert(tk.END, song.lyrics)
        lyrics_text.tag_configure("center", justify='center')  
        lyrics_text.tag_add("center", "1.0", "end") 
    else:
        lyrics_text.delete(1.0, tk.END)
        lyrics_text.insert(tk.END, "Lyrics not found.")
        

# Create a new window
window = tk.Tk()
window.title("Lyrics Extractor")

# Set the window background color
window.configure(bg="#FFFFFF")  

# Create a frame for the input fields
input_frame = tk.Frame(window, bg="#FFFFFF")
input_frame.pack(pady=10)

# Add a label for the song name
song_label = tk.Label(input_frame, text="Song Name:", bg="#FFFFFF")
song_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

# Add a text box for the song name
song_entry = tk.Entry(input_frame, width=40, font=("Arial", 10))
song_entry.grid(row=0, column=1, padx=5, pady=5)

# Add a label for the artist name
artist_label = tk.Label(input_frame, text="Artist:", bg="#FFFFFF")
artist_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

# Add a text box for the artist name
artist_entry = tk.Entry(input_frame, width=40, font=("Arial", 10))
artist_entry.grid(row=1, column=1, padx=5, pady=5)

# Create a frame for the buttons
button_frame = tk.Frame(window, bg="#FFFFFF")
button_frame.pack()

# Add a button to extract the lyrics
extract_button = tk.Button(button_frame, text="Extract Lyrics", command=extract_lyrics, bg="#4CAF50", fg="#FFFFFF", bd=0)
extract_button.pack(pady=5)

# Create a frame for the lyrics display
lyrics_frame = tk.Frame(window, bg="#FFFFFF")
lyrics_frame.pack(pady=10)

# Add a text box to display the lyrics
lyrics_text = tk.Text(lyrics_frame, width=80, height=80, borderwidth=0, bg="pink", fg="white", font=("Consolas", 14))
lyrics_text.pack()

# Run the tkinter event loop
window.mainloop()