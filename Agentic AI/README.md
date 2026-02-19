# LLM decides which tool to use and how to respond 

User Goal
    ↓
LLM decides next action
    ↓
Agent executes tool
    ↓
Send result back to LLM
    ↓
LLM decides next action
    ↓
Repeat until DONE

# Environment variables
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# LLM call
def call_llm(messages):

# Tools section
Calculator vs Weather 

# Agentic loop - runs till either LLM says done or max iterations reached
while iteration < max_iterations:

# Agent executes tool 
if action == "calculator":
    tool_result = calculator_tool(action_input)
    
# Termination - when LLM says done
{
  "action": "DONE",
  "input": "Final answer..."
}

# Reasoning chain
LLM decides next action  → weather tool
Agent executes tool 
Tool result is feedback -> returns "30°C"
LLM decides next action → calculator tool
Tool returns "60"
Repeat until LLM → DONE


# Mental Note
The LLM is the brain
Python is the body
Tools are the hands
The loop is consciousness

-----------------------------
# Input
What is the weather in Mumbai and multiply temperature by 2?

# Output

True Agentic AI Demo Ready!

Enter Goal (or exit): 
Goal: What is the weather in Mumbai and multiply temperature by 2?

--- Iteration 1 ---
LLM Raw Response: ```json
{
  "action": "weather",
  "input": "Mumbai"
}
```
Tool Result: 25.99°C with haze

--- Iteration 2 ---
LLM Raw Response: ```json
{
  "action": "calculator",
  "input": "25.99 * 2"
}
```
Tool Result: 51.98

--- Iteration 3 ---
LLM Raw Response: ```json
{
  "action": "DONE",
  "input": {
    "city": "Mumbai",
    "weather": "25.99°C with haze",
    "calculated_temperature": "51.98°C"
  }
}
```

Final Answer: {'city': 'Mumbai', 'weather': '25.99°C with haze', 'calculated_temperature': '51.98°C'}

Enter Goal (or exit):
----------------------------------------------------------------

# Demo resembles:
-> AWS Bedrock Agents
-> LangGraph
-> AutoGPT-style loops
-> CrewAI agent patterns

# Terms to note
-> LangChain - framework for building LLM-powered applications - connect LLM to tools, build RAG pipelines, manage prompts, chain multiple LLM calls, build simple agents
-> LangGraph - built on LangChain - treats agent execution like a graph/state machine - multi-step workflows, conditional branching, retry logic, long-running agents, human-in-the-loop, production durability
-> AutoGPT - one of the first "autonomous agent" projects - break a goal into tasks, use tools, browse the web, store memory, continue until completion
-> CrewAI - multi agent collaboration

-------------------------------------------------------------------
LangChain ----> 	LLM pipelines	----> RAG, chatbots
LangGraph	----> Stateful agents ---->	Production agents
AutoGPT	----> Autonomous loops ---->	Experimental autonomy
CrewAI	----> Multi-agent systems	----> Role-based collaboration

























