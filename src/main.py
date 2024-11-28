import json
import os
from collections import defaultdict
import matplotlib.pyplot as plt
from datetime import datetime

data_path = "./data"

def calculate_total_minutes(data_path):
    total_ms_played = 0
    for filename in os.listdir(data_path):
        if filename.endswith(".json"):
            filepath = os.path.join(data_path, filename)
            with open(filepath, "r", encoding="utf-8") as file:
                data = json.load(file)
                for track in data:
                    total_ms_played += track.get("msPlayed", 0)
    return total_ms_played / (1000 * 60)

def calculate_top_10_artists(data_path):
    artist_playtime = defaultdict(int)
    for filename in os.listdir(data_path):
        if filename.endswith(".json"):
            filepath = os.path.join(data_path, filename)
            with open(filepath, "r", encoding="utf-8") as file:
                data = json.load(file)
                for track in data:
                    ms_played = track.get("msPlayed", 0)
                    artist_name = track.get("artistName", "Unknown Artist")
                    artist_playtime[artist_name] += ms_played
    top_10_artists = sorted(artist_playtime.items(), key=lambda x: x[1], reverse=True)[:10]
    return [(artist, ms / (1000 * 60)) for artist, ms in top_10_artists]

def calculate_top_10_songs(data_path):
    track_playtime = defaultdict(int)
    for filename in os.listdir(data_path):
        if filename.endswith(".json"):
            filepath = os.path.join(data_path, filename)
            with open(filepath, "r", encoding="utf-8") as file:
                data = json.load(file)
                for track in data:
                    ms_played = track.get("msPlayed", 0)
                    track_name = track.get("trackName", "Unknown Track")
                    artist_name = track.get("artistName", "Unknown Artist")
                    track_key = f"{track_name} by {artist_name}"
                    track_playtime[track_key] += ms_played
    top_10_songs = sorted(track_playtime.items(), key=lambda x: x[1], reverse=True)[:10]
    return [(song, ms / (1000 * 60)) for song, ms in top_10_songs]

def calculate_playtime_per_month(data_path):
    monthly_playtime = defaultdict(int)
    for filename in os.listdir(data_path):
        if filename.endswith(".json"):
            filepath = os.path.join(data_path, filename)
            with open(filepath, "r", encoding="utf-8") as file:
                data = json.load(file)
                for track in data:
                    ms_played = track.get("msPlayed", 0)
                    end_time = track.get("endTime", "")
                    date_obj = datetime.strptime(end_time, "%Y-%m-%d %H:%M")
                    month_key = date_obj.strftime("%Y-%m")
                    monthly_playtime[month_key] += ms_played
    return {month: ms / (1000 * 60) for month, ms in monthly_playtime.items()}

def plot_playtime_per_month(monthly_playtime):
    months = sorted(monthly_playtime.keys())
    minutes_played = [monthly_playtime[month] for month in months]
    output_dir = "./output"
    os.makedirs(output_dir, exist_ok=True)
    plt.figure(figsize=(10, 6))
    plt.bar(months, minutes_played, color="skyblue")
    plt.xticks(rotation=45, ha="right")
    plt.xlabel("Month")
    plt.ylabel("Minutes Played")
    plt.title("Total Minutes Played Per Month")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "playtime_per_month.png"))

if __name__ == "__main__":
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"The specified directory does not exist: {data_path}")
    
    total_minutes = calculate_total_minutes(data_path)
    top_10_artists = calculate_top_10_artists(data_path)
    top_10_songs = calculate_top_10_songs(data_path)
    monthly_playtime = calculate_playtime_per_month(data_path)
    plot_playtime_per_month(monthly_playtime)

    print(f"# Total minutes played: {total_minutes:.0f} ({total_minutes / 60:.1f} hours / {total_minutes / 60 / 24:.1f} days / {total_minutes / 60 / 24 / 30.436875:.2f} months)")
    print(f"# Daily average: {total_minutes / 365:.0f} minutes ({total_minutes / 60 / 365:.1f} hours)")
    print("\n# Top 10 Artists by Playtime:")
    for index, (artist, minutes) in enumerate(top_10_artists, start=1):
        print(f"{index}. {artist}: {minutes:.0f} minutes")
    print("\n# Top 10 Songs by Playtime:")
    for index, (song, minutes) in enumerate(top_10_songs, start=1):
        print(f"{index}. {song}: {minutes:.0f} minutes")
