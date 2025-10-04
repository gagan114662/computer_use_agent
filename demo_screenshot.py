#!/usr/bin/env python3
"""
Simple demo: Take a screenshot and display info
"""

import pyautogui
import sys

def main():
    print("Taking screenshot...")

    try:
        # Take screenshot
        screenshot = pyautogui.screenshot()

        # Save it
        screenshot.save("demo_screenshot.png")

        # Get screen info
        width, height = pyautogui.size()

        print(f"✅ Screenshot saved as demo_screenshot.png")
        print(f"   Screen size: {width}x{height}")
        print(f"   Image saved successfully!")

        return 0

    except Exception as e:
        print(f"❌ Error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
