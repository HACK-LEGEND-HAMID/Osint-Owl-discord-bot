# DAY 23: Discord Bot Setup - Complete Step-by-Step Guide

## 📌 What You Will Learn

Today you will learn how to create a Discord bot from scratch, add it to your server, and set up all the necessary configurations. This is a complete step-by-step guide for beginners.

---

## 🎥 VIDEO TUTORIALS (Watch First)

| Topic | Video Link | Duration | Language |
|-------|------------|----------|----------|
| **Complete Discord Bot Setup** | https://youtu.be/7wnove7K-ZQ | 30 min | Hindi |
| **Discord Developer Portal Guide** | https://youtu.be/37i1nZRiWZQ | 15 min | English |
| **Bot Invite Link Generation** | https://youtu.be/nW8c7vT6H9k | 10 min | English |
| **Discord.py Crash Course** | https://youtu.be/SPTfmiYmuok | 1 hour | English |

### Best Playlist for Beginners:
- **CodeWithHarry Discord Bot Playlist (Hindi):** https://youtube.com/playlist?list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg
- **freeCodeCamp Discord Bot Course (English):** https://youtu.be/SPTfmiYmuok

---

## 📖 Step 1: Create a Discord Application

The first step is to create an application on the Discord Developer Portal. This application will hold your bot and all its settings.

**How to do it:**

1. Go to https://discord.com/developers/applications
2. Log in with your Discord account
3. Click the "New Application" button at the top right
4. Give your application a name (like "My First Bot" or anything you want)
5. Click "Create"

**Video Reference:** https://youtu.be/37i1nZRiWZQ?t=60

Once created, you will see your application dashboard. Here you will find important information like:
- **Application ID** - A unique number that identifies your app
- **Public Key** - Used for verification

Do not close this tab. You will need it throughout the setup process.

---

## 📖 Step 2: Create a Bot User

Now you need to create the actual bot user inside your application.

**How to do it:**

1. In your application dashboard, look at the left sidebar
2. Click on "Bot" (it has a puzzle piece icon)
3. Click the "Add Bot" button
4. Click "Yes, do it!" to confirm

**Video Reference:** https://youtu.be/37i1nZRiWZQ?t=120

You will now see your bot's information page. This includes:
- **Bot Username** - You can change this
- **Bot Avatar** - You can upload a profile picture
- **Token** - A long string of characters (KEEP THIS SECRET!)

**⚠️ About the Bot Token:** The token is like a password for your bot. Anyone who has this token can control your bot. Never share it with anyone, never post it on GitHub, and never paste it in public forums.

---

## 📖 Step 3: Enable Privileged Intents

Discord has special permissions called "Privileged Intents" that your bot needs for certain features.

**What are Privileged Intents?**

| Intent Name | What it allows | When to enable |
|-------------|----------------|----------------|
| **Message Content Intent** | Read message content | If bot needs to read what people type |
| **Server Members Intent** | See when members join/leave | If bot needs to track members |
| **Presence Intent** | See user online status | If bot needs presence status |

**How to enable them:**

1. In the "Bot" section of your application
2. Scroll down to "Privileged Gateway Intents"
3. Toggle ON the intents you need
4. Click "Save Changes"

**Video Reference:** https://youtu.be/nW8c7vT6H9k?t=180

For a basic bot that responds to commands, you only need the **Message Content Intent**. [citation:1]

---

## 📖 Step 4: Generate OAuth2 Invite Link

To add your bot to a server, you need to create an invite link with the correct permissions.

**How to generate the invite link:**

1. Click on "OAuth2" in the left sidebar
2. Click on "URL Generator"
3. Under "Scopes", select:
   - **bot** - Adds your bot to the server
   - **applications.commands** - Enables slash commands

4. Under "Bot Permissions", select what your bot can do:

| Permission | Why Needed |
|------------|------------|
| Send Messages | Bot can send messages |
| Read Messages | Bot can see messages |
| Manage Messages | Bot can delete/pin messages |
| Read Message History | Bot can see past messages |
| Add Reactions | Bot can add emoji reactions |
| Attach Files | Bot can send images/files |

5. Copy the generated URL at the bottom of the page
6. Paste this URL in a new browser tab
7. Select the server you want to add the bot to
8. Click "Authorize"

**Video Reference:** https://youtu.be/nW8c7vT6H9k?t=300

**⚠️ Permission Tip:** Do not select "Administrator" unless absolutely necessary. Giving Administrator permission means your bot can do anything in the server.

---
