from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage

MARKDOWN_PROMPT= f"""
You are a helpful assistant that is good for spelling tests 
You are making a spelling test for a child in YEAR 2 so around 6 to 7 years old. 
You are to GIVE A MARKDOWN STRING AS A RESPONSE 

Create 20 spelling test questions with the following EXACT FORM BELOW  

**Spelling <SPELLING NUMBER>**: The word is <SPELLING> 
<SENTENCE WITH SPELLING> 
The word is <SPELLING>

Here are some examples on how to give the output 

Spelling 1: The word is dive.
I am learning to dive in my swimming lesson.
The word is dive.

Spelling 2: The word is later.
I am going to the shops later.
The word is later.

Spelling 3: The word is think.
Think of a good game.
The word is think.

Spelling 4: The word is move.
Jack wanted to move next to his friend.
The word is move.

"""

llm = Ollama(model="llama3.2")
response = llm.chat(
    [   
        ChatMessage(role="system",content="You are helpful LLM answer in the exact form asked. if you cannot return an empty json"),
        ChatMessage(
            role="user", 
            content=MARKDOWN_PROMPT
        )
    ]
)

print(response.message.content)