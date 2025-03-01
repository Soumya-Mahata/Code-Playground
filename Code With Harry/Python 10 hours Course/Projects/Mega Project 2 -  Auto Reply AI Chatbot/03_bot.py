import pyautogui
import time
import pyperclip
from openai import OpenAI

client = OpenAI(api_key="OpenAI_API_KEY",)

# Click on the Edge icon
pyautogui.click(990, 1050)
time.sleep(2)  # Wait for Edge to open

while True:
    # Drag from (755, 215) to (1870, 905) to select text
    pyautogui.moveTo(755, 200)
    pyautogui.dragTo(1870, 905, duration=1)

    # Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)  # Wait for the clipboard to update
    pyautogui.click(700, 820) # Click at side to remove the selection

    # Get the text from the clipboard and print it
    chat_history = pyperclip.paste()
    print(chat_history)

    # Check if the last message is from the sender (not from SOUMYA)
    if "SOUMYA" not in chat_history.splitlines()[-1]:
        '''# Use the chat history to generate the next chat message
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a person named Soumya, who can speak Bengali, English and Hindi. He is from India and is a coder. You analyze the chat history and respond like Soumya. Output should be the next chat message as Soumya."},
                {
                    "role": "user",
                    "content": chat_history
                }
            ]
        )
        response = completion.choices[0].message['content']
        print(response)'''
        response = "respond koris na"
        # Type the response in the chat box
        pyautogui.click(950, 950)  # Click on the chat box
        pyperclip.copy(response)  # Copy the response to the clipboard
        pyautogui.hotkey('ctrl', 'v')  # Paste the response
        pyautogui.press('enter')  # Send the message

    time.sleep(10)  # Wait for a while before checking again
