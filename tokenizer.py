import os

os.environ['HF_TOKEN'] = "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"

from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("google/gemma-3-1b-it")
tokenizer("Hey Kash")

