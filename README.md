# MusicBot

![version](https://img.shields.io/github/v/tag/xNykram/MusicBot2?style=flat-square)
![size](https://img.shields.io/docker/image-size/websoftdevs/musicbot?style=flat-square)
![build](https://img.shields.io/github/actions/workflow/status/xNykram/Musicbot2/ci-cd.yml?style=flat-square)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)

### Description

**MusicBot** is a simple-to-use Discord bot that allows you to play music from various platforms such as YouTube and SoundCloud. With integration to popular streaming platforms, you can easily search and play your favorite tunes right from your Discord server.

### Features:

- Integration with YouTube and SoundCloud
- Fast and responsive
- Simple to use
- Easy installation
- Lightweight

### Commands:

MusicBot supports a range of commands that are intuitive and easy to use. Here's a quick rundown of the available commands:

- `!help`: Displays all available commands
- `!play`: Plays a song by URL or search query.
- `!join`: Joins the voice channel you are in.
- `!leave`: Leaves the voice channel.
- `!queue`: Displays the current song queue.
- `!skip`: Skips the current song.
- `!stop`: Stops playback entirely.

### Plans

- Integration with Spotify

### Local development

To set up and run the app locally, follow these steps:

1. Open the terminal and run the command `git clone [link]` to copy the repository to your local device.
2. Once you have a copy of the repository on your device, create a new file named `.env` and set below variables in mentioned file:

```
BOT_TOKEN=your_token_goes_here
PREFIX=!
```

3. Run the command `docker-compose -f docker-compose-local.yml up --build` to dockerize the app for the first time. When using the app subsequently, run the same command without `--build` flag.
4. Finally, add the bot to your development server and type !help to get started.
