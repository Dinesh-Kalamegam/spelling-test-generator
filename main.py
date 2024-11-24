from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage

MARKDOWN_PROMPT= f"""
You are a helpful assistant that is good for spelling tests 
You are making a spelling test for a child in YEAR 2 so around 6 to 7 years old. 
You are to GIVE A MARKDOWN STRING AS A RESPONSE 

Create 20 spelling test questions with the following EXACT FORM BELOW FOR EVERY QUESION DO NOT ADD ANYTHING THAT IS NOT IN THE FORM

**Spelling <SPELLING NUMBER>**: The word is <WORD> 

<SENTENCE WITH WORD> 

The word is <WORD>

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

Spelling 5: The word is found.

She found her tissues in her bag.

The word is found.

Spelling 6: The word is dance.

Jordan is learning to dance.

The word is dance.

Spelling 7: The word is other.

He crossed to the other side of the road.

The word is other.

Spelling 8: The word is puff.

Mo blew out the candles with one puff.

The word is puff.

Spelling 9: The word is shy.

My sister is quiet and shy.

The word is shy.

Spelling 10: The word is coldest.

Amaya wore her gloves on the coldest day.

The word is coldest.

Spelling 11: The word is also.

I like drawing but I also like reading.

The word is also.

Spelling 12: The word is worked.

We worked hard to fnish the project.

The word is worked.

Spelling 13: The word is tried.

He tried the soup for lunch.

The word is tried.

Spelling 14: The word is pancakes.

We eat pancakes for a treat.

The word is pancakes.

Spelling 15: The word is biggest.

I let her have the biggest slice of pizza.

The word is biggest.

Spelling 16: The word is phonics.

We are learning phonics at school.

The word is phonics.

Spelling 17: The word is catches.

The goalkeeper catches the ball.

The word is catches.

Spelling 18: The word is beautiful.

The sunset was beautiful.

The word is beautiful.

Spelling 19: The word is fudge.

Fudge is a type of sweet.

The word is fudge.

Spelling 20: The word is usual.

It was usual to have a story before home time.

The word is usual.


"""

llm = Ollama(model="llama3.2")
response = llm.chat(
    [   
        ChatMessage(role="system",content="You are helpful LLM answer in the exact form asked. If you cannot answer say 'Sorry I cannot do this' "),
        ChatMessage(
            role="user", 
            content=MARKDOWN_PROMPT
        )
    ]
)

with open("test.md","w") as f:
    f.write(response.message.content)