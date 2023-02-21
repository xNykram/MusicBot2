# MusicBot2
![version](https://img.shields.io/github/v/tag/xNykram/MusicBot2?style=plastic)
![build](https://img.shields.io/github/actions/workflow/status/xNykram/Musicbot2/ci-cd.yml)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)

Rewritten version of MusicBot in Python

### Description

**MusicBot2** - play your favourite music on your discord server!

#### Features:

- plays music from yt search using a link or the song name,
- simple to use, quick time of song downloads

#### Commands:
- play
- join
- leave
- queue
- skip
- stop

### Plans

- new commands

### How to set up app localy

1. To set up the app locally you have to use the command `git clone [link]`. <br />
2. The link you will find it on the main site of the repo by clicking clone.
3. After getting a copy of the repo on your device, create a `.env` file and copy variables from `configs`.
4. To dockerize this app for the first-time use the command
`docker-compose -f docker-compose-local.yml up --build` <br />
5. When using it after it you use the same command just without `--build`
