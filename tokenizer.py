import os

os.environ['HF_TOKEN'] = "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" #please do not use this token as it has been removed after testing and will not work for you

from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("google/gemma-3-1b-it")
tokenizer("Hey Kash")

