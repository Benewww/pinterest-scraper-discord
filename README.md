# Pinterest Image Scraper to Discord

A Python script that automatically scrapes Pinterest images based on search queries and sends them to Discord channels via webhooks.

## Description

This script uses Selenium to automate Pinterest browsing, extracts image URLs from search results, and automatically sends them to a configured Discord channel. It's useful for monitoring new visual content or creating automated content feeds.

## Features

- Automated Pinterest search functionality
- High-quality image URL extraction
- Automatic Discord webhook integration
- Optional headless browser mode
- Customizable configuration options
- Automatic scrolling to load more images

## Installation

### Prerequisites

- Python 3.7 or higher
- Google Chrome browser installed
- ChromeDriver compatible with your Chrome version

### Dependencies

```bash
pip install selenium requests
```

### ChromeDriver Setup

#### Option 1: Automatic installation
```bash
pip install webdriver-manager
```

#### Option 2: Manual installation
1. Download ChromeDriver from [https://chromedriver.chromium.org/](https://chromedriver.chromium.org/)
2. Place the executable in your PATH or project folder

## Configuration

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/pinterest-scraper-discord.git
cd pinterest-scraper-discord
```

2. **Configure the `config.py` file**
```python
# Your Pinterest search query
SEARCH_QUERY = 'nature landscape'

# Discord webhook URL
DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/YOUR_WEBHOOK_ID/YOUR_TOKEN'

# Maximum number of scrolls
MAX_SCROLLS = 20

# Pause between scrolls (seconds)
SCROLL_PAUSE = 3

# Delay between Discord sends (seconds)
DISCORD_SEND_DELAY = 1

# Headless mode (True = no GUI)
HEADLESS_MODE = True
```

### Getting a Discord Webhook

1. Go to your Discord server settings
2. Select "Integrations" then "Webhooks"
3. Click "New Webhook"
4. Configure the name and channel
5. Copy the webhook URL

## Usage

```bash
python main.py
```

The script will:
1. Open Pinterest and search for your query
2. Automatically scroll to load more images
3. Extract URLs from found images
4. Send each new image to your Discord channel

## Project Structure

```
pinterest-scraper-discord/
├── main.py          # Main script
├── config.py        # Configuration file
├── README.md        # Documentation
└── requirements.txt # Dependencies
```

## Configuration Options

| Variable | Description | Default Value |
|----------|-------------|---------------|
| `SEARCH_QUERY` | Pinterest search term | `'YOUR_QUERY_SEARCH'` |
| `DISCORD_WEBHOOK_URL` | Discord webhook URL | Must be configured |
| `MAX_SCROLLS` | Maximum scroll attempts | `20` |
| `SCROLL_PAUSE` | Pause between scrolls (s) | `3` |
| `DISCORD_SEND_DELAY` | Delay between Discord sends (s) | `1` |
| `HEADLESS_MODE` | Run without GUI | `True` |

## Troubleshooting

### Common Issues

**ChromeDriver not found**
```bash
# Install webdriver-manager
pip install webdriver-manager
```

**Discord webhook error (404)**
- Check that the webhook URL is correct
- Ensure the webhook hasn't been deleted

**No images found**
- Pinterest may block automated requests
- Try reducing `SCROLL_PAUSE` or changing `SEARCH_QUERY`
- Check your internet connection

## Important Notes

- This script is for educational purposes
- Respect Pinterest's terms of service
- Avoid excessive requests to prevent being blocked
- Use appropriate delays between requests

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements
- Submit pull requests

## Support

If you encounter issues, please open a GitHub issue including:
- Your Python version
- Operating system
- Complete error message
