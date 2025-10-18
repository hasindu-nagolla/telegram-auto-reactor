Telegram Auto Reactor BotA simple yet fun Telegram bot that automatically reacts to every message in a group or private chat with a random emoji.FeaturesAutomatic Reactions: Reacts to every new message sent in the chat.Random Emojis: Chooses from a wide variety of emojis for diverse reactions.Easy to Deploy: Can be run locally or deployed on a Virtual Private Server (VPS).Lightweight: Minimal dependencies and resource usage.Getting StartedThese instructions will get you a copy of the project up and running on your local machine for development and testing purposes.PrerequisitesPython 3.8 or higherA Telegram Bot Token. You can get one by talking to the BotFather on Telegram.Local InstallationClone the repository:git clone [https://github.com/your-username/hasindu-nagolla-telegram-auto-reactor.git](https://github.com/your-username/hasindu-nagolla-telegram-auto-reactor.git)
cd hasindu-nagolla-telegram-auto-reactor
Create a virtual environment:python3 -m venv venv
source venv/bin/activate
Install the dependencies:pip install -r requirements.txt
Set up your environment variables:Create a .env file in the project root and add your bot token:BOT_TOKEN="YOUR_TELEGRAM_BOT_TOKEN"
Run the bot:python auto_react.py
Deployment on a VPS (Ubuntu)Here’s how to get your bot running 24/7 on a Virtual Private Server.1. Connect to Your VPSConnect to your server using SSH:ssh your_username@your_server_ip
2. Update and Install PackagesUpdate your package list and install Python, pip, and venv.sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip python3-venv -y
3. Clone Your ProjectClone the repository from your version control system (e.g., GitHub).git clone [https://github.com/your-username/hasindu-nagolla-telegram-auto-reactor.git](https://github.com/your-username/hasindu-nagolla-telegram-auto-reactor.git)
cd hasindu-nagolla-telegram-auto-reactor
4. Set Up the EnvironmentCreate a virtual environment:python3 -m venv venv
Activate the virtual environment:source venv/bin/activate
Install dependencies:pip install -r requirements.txt
Create the .env file:Use a text editor like nano to create and edit the file.nano .env
Add your bot token to the file, then save and exit (press Ctrl+X, then Y, then Enter).BOT_TOKEN="YOUR_TELEGRAM_BOT_TOKEN"
5. Run the Bot as a Service (Using Systemd)To ensure the bot runs continuously, even after you disconnect from the SSH session, we'll set it up as a systemd service.Create a service file:sudo nano /etc/systemd/system/telegram-reactor.service
Add the following configuration. Make sure to replace your_username and the path to your project directory.[Unit]
Description=Telegram Auto Reactor Bot
After=network.target

[Service]
User=your_username
Group=www-data
WorkingDirectory=/home/your_username/hasindu-nagolla-telegram-auto-reactor
ExecStart=/home/your_username/hasindu-nagolla-telegram-auto-reactor/venv/bin/python auto_react.py
Restart=always

[Install]
WantedBy=multi-user.target
Enable and start the service:sudo systemctl daemon-reload
sudo systemctl enable telegram-reactor.service
sudo systemctl start telegram-reactor.service
Check the status of your service:sudo systemctl status telegram-reactor.service
You should see an "active (running)" status.Project Structurehasindu-nagolla-telegram-auto-reactor/
├── .env                  # Environment variables (Bot Token)
├── README.md             # This file
├── auto_react.py         # Main bot script
├── requirements.txt      # Python dependencies
└── sample.env            # Example environment file
ContributingContributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.Fork the ProjectCreate your Feature Branch (git checkout -b feature/AmazingFeature)Commit your Changes (git commit -m 'Add some AmazingFeature')Push to the Branch (git push origin feature/AmazingFeature)Open a Pull RequestLicenseDistributed under the MIT License. See LICENSE for more information.ContactProject Link: https://github.com/your-username/hasindu-nagolla-telegram-auto-reactor