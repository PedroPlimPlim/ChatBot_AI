import tkinter as tk
import google.generativeai as genai
import pathlib
import textwrap
from IPython.display import display
from IPython.display import Markdown

GOOGLE_API_KEY="Insert your API key here"
genai.configure(api_key=GOOGLE_API_KEY)
