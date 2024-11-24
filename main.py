from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage
import edge_tts

PROMPT= f"""
You are a helpful assistant that is good for spelling tests 
You are making a spelling test for a child in YEAR 2 so around 6 to 7 years old. 

The words are to follow this standard 

S1 	the sounds /f/, /l/, /s/, /z/ and /k/ spelt ff, ll, ss, zz and ck

S2 	the ŋ sound spelt n before k

S3 	–tch

S4 	the /v/ sound at the end of words

S5 	adding –s and –es to words (plural of nouns and the third-person singular of verbs)

S6 	adding the endings –ing, –ed and –er to verbs where no change is needed in the root word

S7 	adding –er and –est to adjectives where no change is needed in the root word

S8 	vowel digraphs and trigraphs: ai, oi, ay, oy, a–e, e–e, i–e, o–e, u–e, ar, ee, ea (/i:/), ea (/ɛ/), er (/ɜ:/), er (/ə/), ir, ur, oo (/u:/), oo( ʊ/), oa, oe, ou, ow (/aʊ/), ow (/əʊ/), ue, ew, ie (/aɪ/), ie (/i:/), igh, or, ore, aw, au, air, ear, ear (/ɛə/), are (/ɛə/)

S9 	words ending in –y (/i:/ or /ɪ/)

S10 	new consonant spellings ph and wh

S11 	using k for the /k/ sound

S12 	compound words


S13 	the days of the week

S14 	the /dʒ/ sound spelt as –ge and –dge at the end of words, and sometimes spelt as g elsewhere in words before e, i and y

S15 	the /s/ sound spelt c before e, i and y

S16 	the /n/ sound spelt kn– and (less often) gn– at the beginning of words

S17 	the /r/ sound spelt wr– at the beginning of words

S18 	the /l/ or /əl/ sound spelt –le at the end of words

S19 	the /l/ or /əl/ sound spelt –el at the end of words

S20 	the /l/ or /əl/ sound spelt –al at the end of words

S21 	words ending in –il

S22 	the /aɪ/ sound spelt –y at the end of words

S23 	adding –es to nouns and verbs ending in –y

S24 	adding –ed, –ing, –er and est to a root word ending in –y with a consonant before it

S25 	adding the endings –ing, –ed, –er, –est and –y to words ending in –e with a consonant before it

S26 	adding –ing, –ed, –er, –est and –y to words of one syllable ending in a single consonant letter after a single vowel letter

S27 	the /ɔ:/ sound spelt a before l and ll

S28 	the /ʌ/ sound spelt o

S29 	the /i:/ sound spelt ey

S30 	the /ɒ/ sound spelt a after w and qu

S31 	the /ɜ:/ sound spelt or after w

S32 	the /ɔ:/ sound spelt ar after w

S33 	the /ʒ/ sound spelt s

S34 	the suffixes –ment, –ness, –ful, –less and –ly

S35 	words ending in –tion

36 	homophones and near-homophones

S37 	common exception words

YOU MUST NOT REPEAT ANY WORDS FOR THE TEST. THIS IS IMPERATIVE FOR THE VALIDITY OF THE TEST EVERY QUESTION MUST HAVE A UNIQUE WORD. IF YOU GENERATE A WORD ALREADY IN THE TEST DISCARD IT AN MAKE A NEW ONE

Create 20 spelling test questions with the following EXACT FORM BELOW FOR EVERY QUESION DO NOT ADD ANYTHING THAT IS NOT IN THE FORM.

DO NOT ADD ANYTHING BEFORE GIVING THE SPELLING JUST START STRAIGHT AWAY

Spelling <SPELLING NUMBER>: The word is <WORD> 

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
            content=PROMPT
        )
    ]
)

with open("test.md","w") as f:
    f.write(response.message.content)
    

print("saved markdown trying to generate audio now")
VOICE = "en-GB-SoniaNeural"
OUTPUT_FILE = "test.mp3"

communicate = edge_tts.Communicate(response.message.content, VOICE)
communicate.save_sync(OUTPUT_FILE)