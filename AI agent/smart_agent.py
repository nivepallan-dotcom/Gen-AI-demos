import os
import requests
import re

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

if not OPENROUTER_API_KEY:
    raise ValueError("Set OPENROUTER_API_KEY")

if not WEATHER_API_KEY:
    raise ValueError("Set WEATHER_API_KEY")

# ============================
# TOOL 1: Calculator
# ============================

def calculator_tool(expression):
    try:
        result = eval(expression)
        return f"Result: {result}"
    except:
        return "Invalid math expression."

# ============================
# TOOL 2: Weather API
# ============================

def weather_tool(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"

    response = requests.get(url)

    if response.status_code != 200:
        return "Could not fetch weather."

    data = response.json()

    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]

    return f"Current temperature in {city} is {temp}°C with {description}."

# ============================
# TOOL 3: LLM (Fallback)
# ============================

def call_llm(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        return f"Error: {response.status_code}"

    return response.json()["choices"][0]["message"]["content"]

# ============================
# AGENT BRAIN (Router Logic)
# ============================

def agent(query):

    # Detect math expression
    if re.search(r"\d+\s*[\+\-\*\/]\s*\d+", query):
        return calculator_tool(query)

    # Detect weather query
    if "weather" in query.lower():
        words = query.split()
        city = words[-1]  # simple city detection
        return weather_tool(city)

    # Otherwise use LLM
    return call_llm(query)

# ============================
# MAIN LOOP
# ============================

print("Smart AI Agent Ready!")

while True:
    q = input("\nAsk: ")

    if q.lower() in ["exit", "quit"]:
        break

    answer = agent(q)
    print("\nAgent:", answer)
