# 🤖 LangChain Tool Calling Agent using ReAct

An intelligent AI assistant built using the **ReAct (Reasoning + Acting)** framework with **LangChain**, **Groq LLMs**, **Tavily Search**, and **WeatherStack APIs**.

The agent can reason through user queries, decide when to use external tools, retrieve real-time information from the web, fetch live weather data, and generate accurate responses through a modern Streamlit interface.

---

## 🚀 Live Demo

🔗 **Deployed Application:**
https://langchain-tool-calling-agent-using-react-ob3y.onrender.com


---


## 📸 Screenshots


<img width="1915" height="942" alt="image" src="https://github.com/user-attachments/assets/c075f440-9f20-46ae-80d9-32e11b183a61" />



---


## 📌 Features

### 🧠 ReAct Agent Architecture

* Uses LangChain's ReAct framework
* Performs reasoning before taking actions
* Dynamically selects tools based on user queries

### 🔎 Real-Time Web Search

* Powered by Tavily Search API
* Retrieves latest news and current information
* Provides up-to-date responses

### 🌦️ Live Weather Information by creating Custom tool

* Integrated with WeatherStack API Custom tool
* Fetches current weather conditions
* Supports humidity, temperature, and weather descriptions

### ⚡ Groq LLM Integration

Supports multiple Groq-hosted models:

* Llama 3.3 70B Versatile
* Llama 3.1 8B Instant
* Qwen 3 32B
* Qwen 3.6 27B
* Allam 2 7B


## 🏗️ System Architecture

User Query
↓
ReAct Agent (LangChain)
↓
Reasoning
↓
Tool Selection
↓
├── Tavily Search Tool
└── WeatherStack Tool
↓
Groq LLM
↓
Final Response

---

## 🛠️ Tech Stack

### AI & Agent Framework

* LangChain
* ReAct Agent Pattern

### LLM Provider

* Groq

### External Tools

* Tavily Search API
### Custom tool 

* get_weather_data

### Frontend

* Streamlit

### Backend

* Python

---

## 📂 Project Structure

```bash
langchain-tool-calling-agent_using_ReAct/
│
├── app.py
├── agent.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Pavithrareddy2702/langchain-tool-calling-agent_using_ReAct.git

cd langchain-tool-calling-agent_using_ReAct
```

### Create Virtual Environment

```bash
conda create -n langagent python=3.11

conda activate langagent
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key

TAVILY_API_KEY=your_tavily_api_key

WEATHERSTACK_API_KEY=your_weatherstack_api_key
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---


## 🧠 Agent Workflow

1. User submits a query.
2. ReAct agent analyzes the request.
3. Determines whether a tool is needed.
4. Calls:

   * Tavily Search for current information
   * WeatherStack for weather data
5. Receives tool outputs.
6. Generates a final response using Groq LLM.

---

## 🎯 Learning Outcomes

Through this project I learned:

* LangChain Agent Architecture
* ReAct Reasoning Framework
* Tool Calling Agents
* Prompt Engineering
* Groq LLM Integration
* Streamlit Application Development
* External API Integration
* Real-Time Information Retrieval

---

## 🔮 Future Improvements

* Memory-enabled conversations
* Multi-agent architecture
* PDF document Q&A
* Voice assistant integration
* RAG-based knowledge retrieval
* Streaming token responses
* Authentication and user management

---

## 👨‍💻 Author

**Pavithra Reddy**

GitHub: https://github.com/Pavithrareddy2702

---

