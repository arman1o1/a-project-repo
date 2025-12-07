#  Image Captioning with BLIP

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Transformers-yellow?style=for-the-badge&logo=huggingface&logoColor=black)
![Gradio](https://img.shields.io/badge/Gradio-UI-orange?style=for-the-badge&logo=gradio&logoColor=white)

A lightweight, local AI application that automatically generates descriptive captions for images. Built using Python, the **Salesforce BLIP** model, and **Gradio** for the user interface.

##  Features

*   **Offline Capable:** Runs locally on your machine after the initial model download.
*   **No API Keys:** Does not require a Hugging Face token or OpenAI key. Completely free to run.
*   **User-Friendly:** Simple drag-and-drop web interface.
*   **Clean Output:** Optimized code to suppress unnecessary warnings and logs.

##  Installation

### 1. Clone the Repository
```bash
git clone https://github.com/arman1o1/a-project-repo.git
cd a-project-repo/image-captioning-blip
```

### 2. Install Dependencies
It is recommended to use a virtual environment.
```bash
pip install -r requirements.txt
```

## Usage

Run the application using Python:

```bash
python app.py
```

Wait for the model to load (approx. 1 minute on the first run). Once ready, the terminal will show a local URL:

```text
Running on local URL:  http://127.0.0.1:7860
```

Open that link in your browser to use the app.

##  Technical Details

*   **Model:** [Salesforce/blip-image-captioning-base](https://huggingface.co/Salesforce/blip-image-captioning-base)
*   **Task:** Image-to-Text
*   **Framework:** PyTorch & Transformers
*   **Logic:** The script uses a `pipeline` to download and cache the model. It automatically utilizes the CPU (or GPU if configured) to perform inference.

##  License
This project uses the BLIP model which falls under the [BSD-3-Clause License](https://huggingface.co/Salesforce/blip-image-captioning-base).
```
