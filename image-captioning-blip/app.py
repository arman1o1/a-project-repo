import os
import warnings
import gradio as gr
from transformers import pipeline

# 1. Setup
# Suppress generic warnings to keep the logs clean
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
warnings.filterwarnings("ignore")

print("Loading model... (this may take a moment)")
# We use the CPU-friendly base model. 
# Optional: Add model_kwargs={"use_fast": True} if you want to silence the 'slow processor' warning, 
# but it is not strictly necessary for the app to work.
captioner_pipeline = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

def captioner(image):
    """
    Generates a caption for the uploaded image.
    """
    try:
        if image is None:
            return "No image provided."
        
        # The pipeline returns a list of dicts: [{'generated_text': 'a cat...'}]
        result = captioner_pipeline(image)
        return result[0]['generated_text']
    except Exception as e:
        return f"Error processing image: {str(e)}"

# 2. Interface
demo = gr.Interface(
    fn=captioner,
    inputs=gr.Image(type="pil", label="Upload Image"), 
    outputs=gr.Textbox(label="Generated Caption", lines=2),
    title="Image Captioning using BLIP",
    description="Upload an image to generate a description using the Salesforce BLIP model.",
    flagging_mode="never", 
    examples=[
        ["dog.jpg"], 
        ["cat.jpg"],
        ["galaxy_space_universe_all.jpg"]
    ]
)

if __name__ == "__main__":
    demo.launch()