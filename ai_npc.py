import ollama
import platform
from pathlib import Path
import json
import ast

import chrs
import vars

#Prompt for user to select the character they want to converse with; see list in chrs.py
chr_select = input("Select character: ").strip()
chr_obj = getattr(chrs, chr_select)
chr_select_content = getattr(chr_obj, "character_prompt")

#Stores the file location of a character's chat history as a variable
file = f"chat_hist_{chr_select}.txt"
file_dir = Path(__file__).parent.resolve()
dir_slash = ""
if platform.system().lower() == "windows":
    dir_slash = "\\" 
else:
    dir_slash = "/" #For linux systems
file_abs_path = f"{file_dir}{dir_slash}{file}"

#Checks if above file exists; if so, continues and if not, it gets created
if Path(file).is_file():
    pass
else:
    with open(file, 'w') as new_file:
        new_file.write("")

#Initializes a list of dictionaries that maintains conversation history to keep context
messages = [
    {'role': 'system',
     'content': chr_select_content}
]

#Function that appends the list of dictionaries "messages" with user input and ai npc response; accepts one paramter and returns ai npc response
def chat_with_character(user_input):
    messages.append({'role': 'user', 'content': user_input})
    response = ollama.chat(model=vars.ai_model,
                           messages=messages,
                           options={'temperature': 0.1})
    ai_response = response['message']['content']
    messages.append({'role': 'assistant', 'content': ai_response})
    return ai_response

#Begin chat with ai npc
print(f"{chr_select}: {getattr(chr_obj, "greeting")}")

#Checks chat history file size; if greater than 0 bytes, reads content of file and assigns it to previously created variable "messages"
if Path(file_abs_path).stat().st_size != 0:
    with open(file_abs_path, 'r', encoding='utf-8') as chat_hist_file:
        messages = ast.literal_eval(chat_hist_file.read())

#Prompts for user input; if user enters "quit", the chat ends. Returns a response from ai npc otherwise.
#Also writes the contents of the "messages" variable to the chat history file for the current ai npc; does so after every response.
while True:
    user_input = input("You: ").lower().strip()
    if user_input == 'quit':
        break
    print(f"{chr_select}: {chat_with_character(user_input)}")
    with open(file_abs_path, 'w', encoding='utf-8') as chat_hist_file:
        json.dump(messages, chat_hist_file, ensure_ascii=False, indent=4)