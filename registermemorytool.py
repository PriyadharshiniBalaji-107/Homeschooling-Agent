{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "56dd9c81-7868-4a4b-9755-e1ac03eeb108",
   "metadata": {},
   "outputs": [],
   "source": [
    "from mcp.server import Server\n",
    "from tools.curriculum import CurriculumTool\n",
    "from tools.student_profile import StudentProfileTool\n",
    "from tools.standards import StandardsTool\n",
    "from tools.memory import SaveMemoryTool, LoadMemoryTool, ListMemoryTool\n",
    "\n",
    "server = Server(\"homeschool-curriculum-mcp\")\n",
    "\n",
    "server.add_tool(CurriculumTool())\n",
    "server.add_tool(StudentProfileTool())\n",
    "server.add_tool(StandardsTool())\n",
    "server.add_tool(SaveMemoryTool())\n",
    "server.add_tool(LoadMemoryTool())\n",
    "server.add_tool(ListMemoryTool())\n",
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
