from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
import time

def html_to_png(html_path, output_path):
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--window-size=1920x1080')
    
    # Use WebDriver Manager to get the path to the ChromeDriver
    service = Service(ChromeDriverManager().install())
    
    # Initialize WebDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Open the HTML file
    driver.get(f'file://LandingPage.html')
    
    # Allow some time for the page to load
    time.sleep(2)
    
    # Take screenshot
    screenshot = driver.get_screenshot_as_png()
    
    # Save screenshot to file
    with open(output_path, 'wb') as f:
        f.write(screenshot)
    
    # Close the WebDriver
    driver.quit()
    
    # Optionally, open the image and crop it to the required size using Pillow
    image = Image.open(output_path)
    cropped_image = image.crop(image.getbbox())  # Crop to the content
    cropped_image.save(output_path)

# Example usage
html_file = 'path/to/yourfile.html'
output_file = 'output.png'
html_to_png(html_file, output_file)
