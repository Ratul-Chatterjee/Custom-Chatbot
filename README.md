# Custom-Chatbot

Creating a custom AI chatbot with LLM and Hugging Face.

## Introduction

This repository demonstrates how to build a tailored AI chatbot that leverages state-of-the-art large language models (LLMs) through the Hugging Face ecosystem. By combining Chainlit for dynamic UI components, Matplotlib for visual outputs, and standard Python libraries for asynchronous data processing, this project showcases end-to-end integration of machine learning and interactive user experiences.

In this chatbot implementation, users can:

* Upload local text files and instantly view character counts directly within the chat interface.
* Send and display inline rich text elements alongside local images.
* Stream and render live video frames from a provided URL into a Matplotlib animation.
* Experience seamless, non-blocking interactions, thanks to Python’s `asyncio`.

## Features

1. **File Upload & Analysis**: Prompt-driven file selection, reading, and character-count feedback.
2. **Rich Chat Elements**: Chainlit-powered inline text and image messaging for engaging conversations.
3. **Live Video Stream**: Fetch and animate video frames in real time with customizable resolution and speed.
4. **Asynchronous Workflow**: Parallel execution of file I/O, messaging, and video processing to maintain responsiveness.

## Purpose of this Project

The main goal of this project is to illustrate how modern AI and visualization tools can be orchestrated into a cohesive chatbot application. Whether you’re exploring how to integrate LLMs for conversational AI, experimenting with real-time media rendering, or learning how to build interactive web components with Python, this codebase offers a hands-on starting point. Use it as a template to:

* Prototype advanced chatbot features with minimal boilerplate.
* Understand asynchronous patterns for multitasking in Python applications.
* Customize and extend messaging UIs for domain-specific workflows.

## Usage

After cloning the repository and installing dependencies (see `requirements.txt` or pip-install `chainlit`, `matplotlib`, `numpy`), run the main script:

```bash
python app.py
```

Follow on-screen prompts to upload a text file or enter a video URL. Chainlit will serve a local web UI where you can observe inline messages and media elements.

## Configuration

* **Video Resolution**: Modify `display_video` reshape dimensions (currently 480×640×3) to fit your stream.
* **Animation Settings**: Tweak `frames` and `interval` in `FuncAnimation` for longer duration or different refresh rates.

## Project Structure

```
custom-chatbot/
├── app.py             # Main application script
├── image1.jpg         # Example local image asset
├── chainlit.yaml      # Chainlit UI configuration
├── README.md          # Project documentation
└── requirements.txt   # Python dependencies
```

This was a simple project developed in Intel Unnati Industrial Program 2024.
