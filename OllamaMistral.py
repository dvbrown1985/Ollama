#!/usr/bin/env python
# coding: utf-8

# In[2]:


import ollama # an open-source platform for running large language models locally, accessible via API. 

def get_response(user_input): # sends the user input to the Ollama API.s
    stream = ollama.chat(
        model='mistral',
        messages=[{'role': 'user', 'content': user_input}],
        stream=True
    )
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)

        
def main(): # welcomes the user and asks for a question. Generates a response, and then asks for more questions. Continues or exits based on a user's resopnse.
    print(
        "Hi, I'm an AI generative chatbot using the Ollama Mistral model. Here's how I work:\n"
        "\n"
        "1. You will ask me a question, I'll answer it.\n"
        "2. Then, I will ask you if you have another question.\n"
        "\n"
        "    a. If you respond **yes**, we will restart the loop, and you ask another question.\n"
        "\n"
        "    b. If you respond **no**, the loop breaks, and the conversation ends.")

    user_prompt = input("Let's get started!" # this variable is designed to store the user's prompt which is sent to the LLM model. 
    "\n"
    "\nHow can I help you?  ")
    get_response(user_prompt) # passes the user's prompt to the get_response function so the prompt can be sent to the Ollama API. 

    while True:
        user_prompt2 = input("\n\nDo you have another question (yes or no)? ").strip().lower() # stripts user input of whitespace and converts to lowercase.  
        
        if user_prompt2 == "yes":
            user_prompt = input("\nWhat's up? ")
            get_response(user_prompt) # passes user prompt to the get_response function so the prompt can be sent to the Ollama API. 
        elif user_prompt2 == "no":
            print("\nThat was fun! Thanks for chatting. Have a great day :) ")
            break
        else:
            print("Please respond with 'yes' or 'no'.") # when the user's prompt equals anything but 'yes' or 'no'.

if __name__ == "__main__": # executes code only when script is run directly, not imported.
    main()


# In[ ]:





# In[ ]:




