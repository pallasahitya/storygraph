# Time Traveler Adventure

A simple text-based adventure game built with Python, LangGraph, and Ollama.

The game follows a traveler who discovers a mysterious prehistoric book and is transported to the Mesozoic era. Players make choices using natural language, leading to different paths and endings.

## Features

* Natural language player input
* Branching story paths
* Multiple endings
* Local LLM integration with Ollama
* State management using LangGraph

## Tech Stack

* Python
* LangGraph
* Ollama
* Qwen 2.5
* Pydantic

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start Ollama:

```bash
ollama run qwen2.5:1.5b
```

Run the game:

```bash
python main.py
```

## Current Story Flow

Library → Portal → Mesozoic Forest → Dinosaur Encounters → Volcano → Multiple Endings

## Project Status

This project was built to explore LangGraph workflows, local LLMs, and interactive storytelling.
