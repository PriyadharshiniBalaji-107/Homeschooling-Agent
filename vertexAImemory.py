{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "69de7823-66ef-4a3f-8bee-e419fa5fe0af",
   "metadata": {},
   "outputs": [],
   "source": [
    "from vertexai.preview.generative_models import GenerativeModel, MCPTool\n",
    "\n",
    "mcp_server = MCPTool.from_uri(\"http://localhost:8000\")\n",
    "\n",
    "model = GenerativeModel(\n",
    "    \"gemini-1.5-pro\",\n",
    "    tools=[mcp_server]\n",
    ")\n",
    "\n",
    "prompt = \"\"\"\n",
    "You are a homeschooling curriculum agent.\n",
    "\n",
    "You have access to memory via these tools:\n",
    "- save_memory\n",
    "- load_memory\n",
    "- list_memory\n",
    "\n",
    "Whenever the mother provides student info, interests, difficulties, or curriculum decisions,\n",
    "STORE THEM IN MEMORY.\n",
    "\n",
    "Before generating curriculum:\n",
    "1. Call list_memory.\n",
    "2. Load any relevant memory.\n",
    "3. Use that memory to personalize the curriculum.\n",
    "\n",
    "Student ID: kid1\n",
    "Goal: Build a 12-week plan.\n",
    "\"\"\"\n",
    "\n",
    "response = model.generate_content(prompt)\n",
    "\n",
    "print(response.text)\n"
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
