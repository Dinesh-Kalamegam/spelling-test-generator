# Spelling Test Generator 

An experiment to create a spelling test in the format of the KS1 Spelling Test SATs (so aimed at a 6-7 year old in Year 2 in the UK education system) 

It then tries converting that into an audio file that can be played

I also tried throwing the KS1 SATs Content Domain for spelling from the [Gov UK Website](https://www.gov.uk/government/publications/key-stage-1-english-grammar-punctuation-and-spelling-test-framework/key-stage-1-english-grammar-punctuation-and-spelling-test-framework#content-domain) into the prompt to see if that improves the quality of the test

[test.mp3](./test.mp3)

[[TOC]]

## Requirements 

- [`uv`](https://docs.astral.sh/uv/) for the package management
- [`ollama`](https://ollama.com/) with the `Llama 3.2` model installed - the `3b` parameter 

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

- `test.mp3` for an audio version of the test. The contents of `test.md` is read verbatim