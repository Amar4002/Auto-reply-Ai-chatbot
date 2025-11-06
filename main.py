import time
import pyautogui
import pyperclip
from google import genai

client = genai.Client(api_key="Api_key")

time.sleep(1)  # Time to switch to the correct screen

pyautogui.moveTo(1373, 1049, duration=0.5)
pyautogui.click()
time.sleep(1)


    # Step 2: Select the message text
pyautogui.moveTo(677, 182, duration=1)
pyautogui.dragTo(823, 987, duration=1, button='left')
time.sleep(1)

    # Step 3: Copy the selected text
pyautogui.hotkey('ctrl', 'c')
pyautogui.click(676,320)
time.sleep(1)

    # Step 4: Save copied message
chat_history = pyperclip.paste()
print("Copied Message:", chat_history)


response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Reply casually like a human from India in Hinglish: {chat_history}"
)
    # Extract output text
reply = response.text.strip()
print("AI Reply:", reply)
        # Step 6: Copy reply to clipboard
pyperclip.copy(reply)

        #  Step 7: Click chat box & paste response & send
pyautogui.click(1299, 969)  # ensure this location is input box
time.sleep(1)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
pyautogui.press('enter')
