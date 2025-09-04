# Create_Your_Own_Tokenizer


🤖 Tokenizer Test with Hugging Face Transformers

This is a simple script that demonstrates how to load and use a tokenizer from Hugging Face's Transformers library, specifically using the `google/gemma-3-1b-it` model.


📋 Requirements

* Python 3.8+
* [transformers](https://pypi.org/project/transformers/)
* A valid Hugging Face token with access to the required model.
* Please do not use token mentioned in the code, after this test I have removed it so will not work for you


🚀 Installation

First, install the required library:

```bash
pip install transformers
```


🔐 Hugging Face Token

To access certain models, you may need an access token from Hugging Face.

1. Sign in or create an account at [huggingface.co](https://huggingface.co/)
2. Go to your [Access Tokens page](https://huggingface.co/settings/tokens)
3. Create a new token and copy it

Then, either:

* Set it in your environment manually, or
* (As in the script) set it within the code — **Note**: This method is **not recommended for production** or shared code.


📄 Usage

```python
import os
from transformers import AutoTokenizer

# Set Hugging Face token (for private model access)
os.environ['HF_TOKEN'] = "hf_your_token_here"

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained("google/gemma-3-1b-it")

# Tokenize input
print(tokenizer("Hey Kash"))
```


⚠️ Security Notice

Avoid hardcoding your Hugging Face token in scripts. Instead, use environment variables or a `.env` file (with tools like `python-dotenv`) for better security.

## 📚 References

* [Transformers Documentation](https://huggingface.co/docs/transformers/index)
* [google/gemma-3-1b-it Model Card](https://huggingface.co/google/gemma-3-1b-it)

---

Would you like me to include `.gitignore` or `.env` support as well for better practice?
