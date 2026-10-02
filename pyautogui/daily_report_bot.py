import pyautogui
import pyperclip
import time
import os
from datetime import datetime

# --------------------------------------------------
# SETTINGS
# --------------------------------------------------

REPORT_FOLDER = os.path.join(os.getcwd(), "daily_reports")

os.makedirs(REPORT_FOLDER, exist_ok=True)

now = datetime.now()

datetime_string = now.strftime("%Y-%m-%d %H:%M:%S")
date_string = now.strftime("%Y-%m-%d")

excel_filename = f"daily_report_{date_string}.xlsx"
screenshot_filename = f"daily_report_{date_string}.png"

excel_path = os.path.join(REPORT_FOLDER, excel_filename)
screenshot_path = os.path.join(REPORT_FOLDER, screenshot_filename)


# --------------------------------------------------
# PYAutoGUI SETTINGS
# --------------------------------------------------

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True


def wait(seconds):
    time.sleep(seconds)


# --------------------------------------------------
# STEP 1: OPEN CHROME IN GUEST MODE
# --------------------------------------------------

print("Opening Chrome in Guest mode...")

pyautogui.hotkey("win", "r")
wait(1)

pyautogui.write(
    "chrome.exe --guest",
    interval=0.05
)

pyautogui.press("enter")

wait(6)

print("Chrome Guest mode opened.")


# --------------------------------------------------
# STEP 2: OPEN WEATHER WEBSITE
# --------------------------------------------------

print("Opening weather website...")

pyautogui.hotkey("ctrl", "l")

pyautogui.write(
    "https://www.google.com/search?q=weather+Sanford+Florida",
    interval=0.01
)

pyautogui.press("enter")

wait(6)
'''
```python
import pyautogui
import time
from datetime import datetime
import os


# ---------------------------------------------------------
# SETTINGS
# ---------------------------------------------------------

# Website to open
WEBSITE = "https://www.google.com/search?q=weather+Sanford+Florida"

# Folder where the report and screenshot will be saved
OUTPUT_FOLDER = os.path.join(os.getcwd(), "daily_reports")

# Create output folder if it does not exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


# ---------------------------------------------------------
# HELPER FUNCTIONS
# ---------------------------------------------------------

def wait(seconds=2):
    """Pause so applications/web pages have time to respond."""
    time.sleep(seconds)


def click_and_type(x, y, text):
    """Click a screen position and type text."""
    pyautogui.click(x, y)
    pyautogui.write(text, interval=0.02)


# ---------------------------------------------------------
# GET CURRENT DATE AND TIME
# ---------------------------------------------------------

now = datetime.now()

date_string = now.strftime("%Y-%m-%d")
datetime_string = now.strftime("%Y-%m-%d %H:%M:%S")

excel_filename = f"daily_report_{date_string}.xlsx"
screenshot_filename = f"daily_report_{date_string}.png"

excel_path = os.path.join(OUTPUT_FOLDER, excel_filename)
screenshot_path = os.path.join(OUTPUT_FOLDER, screenshot_filename)

# ---------------------------------------------------------
# STEP 1: OPEN CHROME
# ---------------------------------------------------------

print("Opening Chrome...")

pyautogui.hotkey("win", "r")
wait(1)

pyautogui.write("chrome", interval=0.05)
pyautogui.press("enter")

wait(4)


# ---------------------------------------------------------
# STEP 2: OPEN PUBLIC WEBSITE
# ---------------------------------------------------------

print("Opening weather website...")

pyautogui.hotkey("ctrl", "l")
pyautogui.write(WEBSITE, interval=0.01)
pyautogui.press("enter")

# Give the website time to load
wait(6)
'''

# ---------------------------------------------------------
# STEP 3: COPY IMPORTANT INFORMATION
# ---------------------------------------------------------

print("Getting weather information...")

# Select the page text and copy it.
# This demonstrates using the screen/keyboard rather than
# requesting weather data through an API.

pyautogui.hotkey("ctrl", "a")
pyautogui.hotkey("ctrl", "c")

wait(1)

# Get clipboard contents using tkinter.
import tkinter as tk

root = tk.Tk()
root.withdraw()

try:
    page_text = root.clipboard_get()
except tk.TclError:
    page_text = ""

root.destroy()


# Try to find a temperature from the copied page text.
# Google weather results commonly contain a temperature
# such as "82°F".

temperature = "Weather information unavailable"

words = page_text.split()

for i, word in enumerate(words):
    cleaned = word.replace("°", "")

    if cleaned.endswith("F") or cleaned.endswith("C"):
        temperature = word
        break

    # Look for a numeric value followed by °F / °C
    if i + 1 < len(words):
        next_word = words[i + 1]

        if "°F" in next_word or "°C" in next_word:
            temperature = words[i] + " " + next_word
            break


print("Fetched data:", temperature)


# ---------------------------------------------------------
# STEP 4: OPEN MICROSOFT EXCEL
# ---------------------------------------------------------

print("Opening Microsoft Excel...")

pyautogui.hotkey("win", "r")
wait(1)

pyautogui.write("excel", interval=0.05)
pyautogui.press("enter")

# Give Excel time to open
wait(6)


# ---------------------------------------------------------
# STEP 5: CREATE A NEW WORKBOOK
# ---------------------------------------------------------

print("Creating report...")

# If Excel displays its start screen, press Enter.
pyautogui.press("enter")

wait(3)


# ---------------------------------------------------------
# STEP 6: ENTER REPORT HEADERS
# ---------------------------------------------------------

# Excel should have cell A1 selected.

pyautogui.write("Date & Time")
pyautogui.press("tab")

pyautogui.write("Fetched Data")
pyautogui.press("tab")

pyautogui.write("Comment")

pyautogui.press("enter")


# ---------------------------------------------------------
# STEP 7: ENTER TODAY'S REPORT DATA
# ---------------------------------------------------------

pyautogui.write(datetime_string)
pyautogui.press("tab")

pyautogui.write(temperature)
pyautogui.press("tab")

pyautogui.write("Good for outdoor activities")
pyautogui.press("enter")


# ---------------------------------------------------------
# STEP 8: FORMAT THE SHEET
# ---------------------------------------------------------

# Select the first three columns.
pyautogui.hotkey("ctrl", "a")

# Automatically adjust column widths.
# Alt + H + O + I is Excel's AutoFit Column Width shortcut.
pyautogui.hotkey("alt", "h")
pyautogui.press("o")
pyautogui.press("i")

wait(2)


# ---------------------------------------------------------
# STEP 9: SAVE EXCEL FILE
# ---------------------------------------------------------

print("Saving Excel file...")

pyautogui.hotkey("ctrl", "shift", "s")
wait(3)

# Type the complete path into the Save As dialog.
pyautogui.hotkey("ctrl", "a")
pyautogui.write(excel_path, interval=0.01)

pyautogui.press("enter")

wait(5)

# If Excel asks whether to use the Excel format,
# press Enter to accept the default.
pyautogui.press("enter")

wait(3)


# ---------------------------------------------------------
# STEP 10: TAKE SCREENSHOT OF FINAL EXCEL SHEET
# ---------------------------------------------------------

print("Taking screenshot...")

# Make sure Excel is visible.
pyautogui.hotkey("alt", "tab")
wait(2)

# Screenshot of the entire screen.
screenshot = pyautogui.screenshot()

screenshot.save(screenshot_path)


# ---------------------------------------------------------
# FINISHED
# ---------------------------------------------------------

print()
print("======================================")
print("Daily report completed successfully!")
print("======================================")
print(f"Excel file: {excel_path}")
print(f"Screenshot: {screenshot_path}")
print()

