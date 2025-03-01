import pyautogui

while True:
    p = pyautogui.position()
    print(p)

#Observations:
# Edge icon is at (990, 1050)
# Chat box is from (755, 215) to (1870, 905)

# Prompt to AI: 
# Write a pyautogui script which will first click on edge icon at (990, 1050) and then drags from (755, 215) to (1870, 905) to select the texts and copy it to the clipboard and print the texts
# Click at (700, 820) to remove the selection
# Generate the next chat message as Soumya using the chat history
# Check if the last message is from the sender (not from SOUMYA)
# If not, then paste the response at (950, 950) and send the message by pressing enter
# Wait for 10 seconds before checking again
# Loop this process infinitely