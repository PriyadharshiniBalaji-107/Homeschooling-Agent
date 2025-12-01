{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "11d551ff-cd1a-4ed4-adce-fdd3f7e41f19",
   "metadata": {},
   "outputs": [],
   "source": [
    "# src/curriculumagent.py\n",
    "import os\n",
    "import google.genai as genai\n",
    "from google.cloud import aiplatform\n",
    "\n",
    "PROMPT_TEMPLATE = open(\"prompts/curriculum_prompt.txt\").read()\n",
    "\n",
    "# Configure GenAI (API key or rely on ADC)\n",
    "API_KEY = os.environ.get(\"GOOGLE_API_KEY\")\n",
    "if API_KEY:\n",
    "    genai.configure(api_key=API_KEY)\n",
    "\n",
    "# Initialize Vertex AI (optional but good for some environments)\n",
    "PROJECT_ID = os.environ.get(\"GOOGLE_CLOUD_PROJECT\")\n",
    "LOCATION = os.environ.get(\"AI_LOCATION\", \"us-central1\")\n",
    "if PROJECT_ID:\n",
    "    aiplatform.init(project=PROJECT_ID, location=LOCATION)\n",
    "\n",
    "MODEL = os.environ.get(\"GENIE_MODEL\", \"gemini-1.5-pro\")\n",
    "\n",
    "def build_prompt(user_text, retrieval_text):\n",
    "    return PROMPT_TEMPLATE.format(user_text=user_text, retrieval_text=retrieval_text)\n",
    "\n",
    "def call_gemini(prompt, model=MODEL, max_tokens=256, temperature=0.2):\n",
    "    # Uses google-genai create_chat API\n",
    "    response = genai.create_chat(\n",
    "        model=model,\n",
    "        messages=[{\"role\": \"user\", \"content\": prompt}],\n",
    "        temperature=temperature,\n",
    "        max_output_tokens=max_tokens,\n",
    "    )\n",
    "    if hasattr(response, \"candidates\") and response.candidates:\n",
    "        return response.candidates[0].content\n",
    "    # Fallbacks:\n",
    "    if hasattr(response, \"text\"):\n",
    "        return response.text\n",
    "    return str(response)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
