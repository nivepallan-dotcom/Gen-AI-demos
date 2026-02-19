# Gen-AI-demos - Tool using router agent

User Input
     ↓
Agent Brain (Router Logic)
     ├── Calculator Tool
     ├── Weather Tool (API Call)
     └── LLM (Fallback)
     ↓
Return Result

# Load API keys
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# Calculator tool
def calculator_tool(expression):
    try:
        result = eval(expression)   # risky in prod
        return f"Result: {result}"

-> Input: 25 * 8   , Output : 200

# Weather tool
def weather_tool(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"


# Agent brain (router)
def agent(query): -->  decides what to do - call weather API or calculator tool

# LLM fallback
return call_llm(query)  --> in case query is " What is AI? , Tell a joke" 

It is rule based routing and not LLM driven (agentic)




















