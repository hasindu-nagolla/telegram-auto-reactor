# Telegram Auto Reactor Bot

A simple yet fun Telegram bot that automatically reacts to every message in a group or private chat with a random emoji.

## 🌐 Live Website

Visit the website at: [https://hasindu-nagolla.github.io/telegram-auto-reactor/](https://hasindu-nagolla.github.io/telegram-auto-reactor/)

The website is built with React + Tailwind CSS and automatically deployed via GitHub Actions.

## Features

- **Automatic Reactions:** Reacts to every new message sent in the chat.  
- **Random Emojis:** Chooses from a wide variety of emojis for diverse reactions.  
- **Easy to Deploy:** Can be run locally or deployed on a Virtual Private Server (VPS).  
- **Lightweight:** Minimal dependencies and resource usage.

## 🚀 Website Development

The website is built using:
- **React** - Modern UI library
- **Tailwind CSS** - Utility-first CSS framework
- **Vite** - Fast build tool
- **GitHub Actions** - Automated deployment to GitHub Pages

### Local Development

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Run development server:**
   ```bash
   npm run dev
   ```

3. **Build for production:**
   ```bash
   npm run build
   ```

4. **Preview production build:**
   ```bash
   npm run preview
   ```  

## Deployment on a VPS (Ubuntu)

Here’s how to get your bot running 24/7 on a Virtual Private Server.

1. **Connect to Your VPS**
    ```bash
    ssh your_username@your_server_ip
    sudo apt update && sudo apt upgrade -y
    sudo apt install python3 python3-pip python3-venv -y
    ```

2. **Clone Project:**
   ```bash
   git clone https://github.com/your-username/hasindu-nagolla-telegram-auto-reactor.git
   cd hasindu-nagolla-telegram-auto-reactor
   ```

3. **Set Up the Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   nano .env   # BOT_TOKEN="YOUR_TELEGRAM_BOT_TOKEN"
   ```
4. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Bot in tmux:**
   ```bash
   tmux new -s telegram-bot
   source venv/bin/activate
   python auto_react.py
   ```