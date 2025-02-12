# Simple ChatBot

This is a simple chatbot implemented using Python and the NLTK library. The chatbot can respond to various user inputs with predefined responses and log interactions.

## Features

- Responds to greetings, questions, and farewells.
- Handles more complex patterns and provides fallback responses.
- Logs user interactions to a file.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/simple_chatbot.git
    cd simple_chatbot
    ```

2. Install the required dependencies:
    ```sh
    pip install nltk
    ```

3. Download the NLTK data:
    ```python
    import nltk
    nltk.download('punkt')
    ```

## Usage

1. Run the chatbot:
    ```sh
    python chatbot.py
    ```

2. Interact with the chatbot by typing your messages. Type 'bye' or 'goodbye' to exit.

## Files

- `chatbot.py`: Main script to run the chatbot.
- `advanced_chatbot.py`: Contains the `AdvancedChatBot` class with advanced features.
- `chatbot.log`: Log file to store user interactions.

## Example

```
Advanced ChatBot: Type 'bye' to exit.
You: hello
ChatBot: Hi there!
You: what is your name?
ChatBot: I'm a simple chatbot!
You: bye
ChatBot: Goodbye!
```

## License

This project is licensed under the MIT License.
