import pyautogui
import time
import pyperclip
import os
from openai import OpenAI

client = OpenAI(
    api_key = "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",
)

sender_name = input("enter name: ")

def is_last_message_from_sender(chat_log, sender_name):
    # Check if the last message in the chat log is from the sender
    messages = chat_log.strip().split("/2024]")[-1]
    if sender_name in messages:
        return True
    return False

    

# Step 1: Click on the chrome icon at (1014, 1054)
pyautogui.click(1014, 1054)

# Adding a small delay to ensure the click is registered
time.sleep(2)

while True:
    # Step 2: Move to (693, 249), then drag to (1787, 908) to select the text
    pyautogui.moveTo(693, 249)
    pyautogui.dragTo(1018, 916, duration=1, button='left')

    # Adding a small delay to ensure the drag completes
    time.sleep(2)

    # Step 3: Press Ctrl+C (to copy the selected text)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(693, 249)

    # Adding a small delay to ensure the text is copied
    time.sleep(2)

    # Step 4: Get the copied text from the clipboard using pyperclip
    chat_history = pyperclip.paste()

    # Now, 'copied_text' contains the text that was selected and copied
    print(chat_history)

    if is_last_message_from_sender(chat_history):
    
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a person named Naruto who speaks hindi as well as english. You are from india and you are a coder. You have to analyze chat history and respond like Naruto.Output should be the next chat response text message only with emoji if needed"},
                {"role": "user", "content": chat_history}
            ]
        )

        response = completion.choices[0].message.content
        pyperclip.copy(response)

        # Step 5: Click at (978, 960) to focus on the new input field
        pyautogui.click(978, 960)

        # Adding a small delay to ensure the click is registered
        time.sleep(2)

        # Step 6: Paste the copied text (Ctrl+V)
        pyautogui.hotkey('ctrl', 'v')

        # Adding a small delay to ensure the text is pasted
        time.sleep(2)

        # Step 7: Press Enter
        pyautogui.press('enter')