# НОМЕРОК — Telegram Mini App

A small prototype of a car-number collecting game. The interface has spin animation, country selection, rarity tiers, garage, selling for fictional in-game coins, and a profile.

## Mini App URL
https://kotlinhgs2w.github.io/nomerok/

## Publish with GitHub Pages
Open **Settings → Pages**. Under **Build and deployment**, choose **Deploy from a branch**, select **main** and **/(root)**, then Save. GitHub Pages publishes the root `index.html`. It can take a few minutes to appear.

## Run the Telegram bot in Pydroid 3
Install Python packages:
```bash
pip install -r requirements.txt
```

Create a local file named `.env` (do not upload it to GitHub):
```env
BOT_TOKEN=YOUR_BOTFATHER_TOKEN
WEBAPP_URL=https://kotlinhgs2w.github.io/nomerok/
```

Run:
```bash
python bot.py
```

## Prototype limits
- Browser progress (coins, spins, garage) is currently kept in memory and resets after refreshing.
- There is no multiplayer backend or secure server-side account storage yet.
- This prototype is for a free, fictional-coin collection game only. It does not implement paid random spins, paid luck boosts, betting, cash-out, or real-money prizes.
- Before public multiplayer launch, add a backend and verify Telegram Web App initData on the server.
- Never commit `.env` or share your bot token.
