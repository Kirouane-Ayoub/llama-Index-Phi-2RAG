
from utils import predict
import gradio as gr
gr.ChatInterface(predict).launch(share=True)