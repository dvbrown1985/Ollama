**Chatbot Overview**

**Large Language Model (LLM):** Utilizes the Ollama Mistral model, a powerful large language model for generating conversational text with 7B parameters.

**User Interface:** Text-based interaction through standard input/output of the command line.

**User Experience:**

  1. Welcomes the user and explains the interaction flow.
  2. Prompts for user questions.
  3. Sends user questions to the Ollama API for processing.
  4. Presents the LLM's generated response to the user.
  5. Asks if the user has further questions, creating a conversational loop.
  6. Exits the loop at the user’s request. 

**Error Handling:** Ensures user input for continuing the conversation is strictly "yes" or "no".

**Functions:**

  1. **get_response(user_input):** Sends user input to Ollama API and streams the LLM's response.
  2. **main():** Handles user interaction, prompting, and loop control.


**Execution:** The if __name__ == "__main__": block ensures the script runs only when executed directly, not when imported as a module.


**Benefits:**

  - Leverages Ollama's LLM capabilities for informative and potentially creative responses.
  - Simple and user-friendly text-based interface.

**Limitations:**

  - Relies on internet access for Ollama API communication.
  - LLM responses may not always be perfectly accurate or relevant.
