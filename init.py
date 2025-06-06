from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import requests
import config

def send_to_discord(image_url, webhook_url):
    data = {"content": image_url}
    response = requests.post(webhook_url, json=data)
    if response.status_code != 204:
        print("Erreur webhook:", response.status_code, response.text)


def get_images(driver):
    pins = driver.find_elements(By.CSS_SELECTOR, "div[data-test-id='pin'] img")
    urls = set()

    for img in pins:
        srcset = img.get_attribute('srcset')
        src = img.get_attribute('src')

        if srcset:
            parts = srcset.split(',')
            if parts:
                last_part = parts[-1].strip()
                url = last_part.split(' ')[0]
                urls.add(url)
        elif src:
            urls.add(src)
    return urls


def main():
    options = Options()

    if config.HEADLESS_MODE:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get(f'https://www.pinterest.com/search/pins/?q={config.SEARCH_QUERY}')
    time.sleep(5)

    all_urls = set()
    scroll_count = 0

    while scroll_count < config.MAX_SCROLLS:
        new_urls = get_images(driver)
        new_images = new_urls - all_urls

        if not new_images:
            break

        all_urls.update(new_images)
        print(f"Scroll #{scroll_count + 1}: {len(new_images)} nouvelles images, total {len(all_urls)}")

        for url in new_images:
            print(url)
            send_to_discord(url, config.DISCORD_WEBHOOK_URL)
            time.sleep(config.DISCORD_SEND_DELAY)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(config.SCROLL_PAUSE)
        scroll_count += 1

    driver.quit()


if __name__ == "__main__":
    main()
