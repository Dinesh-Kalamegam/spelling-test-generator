# Spelling Test Generator 

An experiment to create a spelling test in the format of the KS1 Spelling Test SATs (so aimed at a 6-7 year old in Year 2 of the UK education system) with an LLM

It then tries converting that into an audio file that can be played - its quite primitive as it just reads the script verbatim with no pauses.

[audio sample](./test.mp4)

## Prompt Engineering
To generate this test I have done the following 

- Shoved the KS1 SATs Content Domain for spelling from the [Gov UK Website](https://www.gov.uk/government/publications/key-stage-1-english-grammar-punctuation-and-spelling-test-framework/key-stage-1-english-grammar-punctuation-and-spelling-test-framework#content-domain) into the prompt to get the right type of words 

- Used the [2024 Spelling Test](https://assets.publishing.service.gov.uk/media/6655bd308f90ef31c23ebb28/STA248823e_2024_ks1_English_GPS_Administering_Paper1_spelling.pdf) as few shot prompts 

- Explicitly tell the LLM to not repeat words since it would do so or if not told otherwise 

- Explictly tell it not to use compound words for the sentences and to keep the sentences in context and be age appropriate

- Explicitly tell it to not give anything other than the spelling test - this command tends to get ignored though

## Requirements 

- [`uv`](https://docs.astral.sh/uv/) for the package management
- [`ollama`](https://ollama.com/) with the `Llama 3.2` model installed - the `3b` parameter model

## Setup

1. Setup the virtual environment & install the dependencies with 

```bash
uv sync
```

2. In a separate terminal have ollama running 

```bash 
ollama serve 
``` 

3. Run the script 

```bash 
uv run python main.py
``` 

Running the script produces two files

- `test.md` for a written transcript of the spelling test 

- `test.mp4` for an audio version of the test. The contents of `test.md` is read verbatim