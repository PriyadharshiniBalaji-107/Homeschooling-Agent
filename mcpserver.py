{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "60639a97-ec3c-4393-a7ef-99b229d3fe9d",
   "metadata": {},
   "outputs": [],
   "source": [
    "from mcp.server import Server\n",
    "from src.curriculum import Curriculumsearch\n",
    "from src.curriculumagent import curriculumagent\n",
    "from src.app_streamlit import app_streamlit\n",
    "\n",
    "server = Server(\"homeschool-curriculum-mcp\")\n",
    "\n",
    "# Register tools\n",
    "server.add_tool(CurriculumTool())\n",
    "server.add_tool(StudentProfileTool())\n",
    "server.add_tool(StandardsTool())\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    server.run()\n"
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
