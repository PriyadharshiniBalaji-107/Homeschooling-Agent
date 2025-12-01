# Homeschooling-Agent
Code to build an agent to support homeschooling parents to decide their curriculum

Our homeschooling AI agent uses a hybrid architecture consisting of Vertex AI’s Gemini models and the Model Context Protocol (MCP). Vertex AI performs all reasoning, planning, and curriculum generation, while MCP gives the model structured access to external tools such as student profiles, curriculum repositories, state standards, and long-term memory storage. This design allows the agent to generate accurate, personalized learning plans that evolve with each student over time. By combining the intelligence of Vertex AI with the tool-access capabilities of MCP, the system delivers a reliable, extensible, and context-aware homeschooling assistant
An AI assistant that helps homeschooling parents choose and plan day-to-day curriculum.  
Built with Python, Google GenAI (Gemini), and a CSV-backed retrieval tool. Includes a Streamlit demo UI

Vertex AI (Gemini) handles reasoning, curriculum design, and tool invocation.
MCP (Model Context Protocol) exposes backend tools for profiles, standards, curriculum data, and persistent memory.
Using both allows the agent to create highly personalized and continuously improving homeschool curriculum plans.
