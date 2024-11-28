
# Spotify Analyzer

This project is used to analyze the spotify streaming history.

## Installation

Clone the project

```bash
  git clone https://github.com/SirSamX/Spotify-Analyzer.git
```

Go to the project directory

```bash
  cd spotify-analyzer
```

Install dependencies

```bash
  pip install -r requirements.txt
```
## Usage

Get your data from the [Spotify Privacy Page](https://www.spotify.com/account/privacy/) (This usually takes a few days).  
Put the files called "StreamingHistory_music_*" in a folder called "data".

Run the programm

```bash
  python src/main.py
```

## Features

- Total Minutes Played
- Average Minutes Per Day
- Top 10 Artists by Playtime
- Top 10 Songs by Playtime
- Monthly Playtime Visualization (using matplotlib)
