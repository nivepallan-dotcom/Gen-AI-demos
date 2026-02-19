import os
import requests
import json

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

if not OPENROUTER_API_KEY:
    raise ValueError("Set OPENROUTER_API_KEY")

# -------------------------
# LLM CALL
# -------------------------

def call_llm(messages):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": messages,
        "temperature": 0.2
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        print("LLM API Error:", response.text)
        return None

    return response.json()["choices"][0]["message"]["content"]

# -------------------------
# TOOLS
# -------------------------

def calculator_tool(expression):
    try:
        return str(eval(expression))
    except:
        return "Calculation error."

def weather_tool(city):
    if not WEATHER_API_KEY:
        return "Weather API key missing."

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        return f"Weather lookup failed: {response.text}"

    data = response.json()
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]

    return f"{temp}°C with {desc}"

# -------------------------
# JSON CLEANER
# -------------------------

def parse_json_response(response):

    cleaned = response.strip()

    # Remove markdown code fences if present
    if cleaned.startswith("```"):
        cleaned = cleaned.replace("```json", "")
        cleaned = cleaned.replace("```", "")
        cleaned = cleaned.strip()

    return json.loads(cleaned)

# -------------------------
# TRUE AGENT LOOP
# -------------------------

def agent_loop(user_goal):

    print("\nGoal:", user_goal)

    messages = [
        {
            "role": "system",
            "content": """
You are an autonomous AI agent.

You have access to these tools:
1. calculator(expression)
2. weather(city)

Respond ONLY in valid JSON format like this:

{
  "action": "calculator | weather | DONE",
  "input": "tool input or final answer"
}

Do not include markdown. Do not include explanation.
"""
        },
        {"role": "user", "content": user_goal}
    ]

    max_iterations = 5
    iteration = 0

    while iteration < max_iterations:

        iteration += 1
        print(f"\n--- Iteration {iteration} ---")

        response = call_llm(messages)

        if not response:
            print("LLM error.")
            break

        print("LLM Raw Response:", response)

        try:
            action_json = parse_json_response(response)
        except Exception as e:
            print("JSON parsing error:", e)
            print("Raw response was:", response)
            break

        action = action_json.get("action")
        action_input = action_json.get("input")

        if action == "DONE":
            print("\nFinal Answer:", action_input)
            break

        elif action == "calculator":
            tool_result = calculator_tool(action_input)

        elif action == "weather":
            tool_result = weather_tool(action_input)

        else:
            print("Unknown tool:", action)
            break

        print("Tool Result:", tool_result)

        # Feed result back to LLM
        messages.append({"role": "assistant", "content": response})
        messages.append({"role": "user", "content": f"Tool result: {tool_result}. What next?"})

    else:
        print("\nStopped due to max iteration limit.")

# -------------------------
# RUN
# -------------------------

print("True Agentic AI Demo Ready!")

while True:
    user_input = input("\nEnter Goal (or exit): ")

    if user_input.lower() == "exit":
        break

    agent_loop(user_input)

