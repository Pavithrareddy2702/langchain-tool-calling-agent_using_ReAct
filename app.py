
import streamlit as st

from agent import build_agent

# ---------------------------------------------------------------------------
# Page Config
# ---------------------------------------------------------------------------

st.set_page_config(
    page_title="ReAct Agent Chat",
    page_icon="🤖",
    layout="centered"
)


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------

AVAILABLE_MODELS = {
    "llama-3.3-70b-versatile":
        "Llama 3.3 70B — strong reasoning, good default for agents",

    "llama-3.1-8b-instant":
        "Llama 3.1 8B — fastest/cheapest option",

    "qwen/qwen3-32b":
        "Qwen3 32B — strong general-purpose model",

    "qwen/qwen3.6-27b":
        "Qwen3.6 27B — newer Qwen release",

    "allam-2-7b":
        "Arabic-focused model",
}

DEFAULT_MODEL = "llama-3.3-70b-versatile"

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------

# st.title("🤖 ReAct Agent")

# st.subheader(
#     "Ask anything related to the latest news, current events, weather, and general knowledge."
# )

# st.caption(
#     "Powered by Groq · Tavily Search · WeatherStack"
# )

st.title("🤖 ReAct Langchain Agent")

st.markdown(
    """
### Stay informed with real-time information

Ask anything about:

- 📰 Latest News
- 🌍 Current Events
- 🌦️ Weather Updates
- 🔎 General Knowledge
"""
)

st.caption(
    "Powered by Groq · Tavily Search · WeatherStack"
)
# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------

with st.sidebar:

    st.header("Settings")

    selected_model = st.selectbox(
        "Model",
        options=list(AVAILABLE_MODELS.keys()),
        index=list(AVAILABLE_MODELS.keys()).index(DEFAULT_MODEL),
    )

    st.caption(
        AVAILABLE_MODELS[selected_model]
    )

    show_steps = st.toggle(
        "Show Agent Reasoning",
        value=False
    )

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.markdown(
        """
### Available Tools

- 🔎 Tavily Search
- 🌤️ WeatherStack
"""
    )

    st.markdown(
        """
### Try Asking

- Find the capital of France and its current weather
- What's the weather in Tokyo?
- Latest AI news
- Who is the Prime Minister of India?
"""
    )

# ---------------------------------------------------------------------------
# Session State
# ---------------------------------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------------------------------------------------------
# Display Chat History
# ---------------------------------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------------------------------------------------------------------
# Chat Input
# ---------------------------------------------------------------------------

user_input = st.chat_input(
    "Ask me anything..."
)

if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):

        try:

            agent_executor = build_agent(
                selected_model
            )

            with st.spinner("Thinking..."):

                result = agent_executor.invoke(
                    {
                        "input": user_input
                    }
                )

            answer = result["output"]

            st.markdown(answer)

            # --------------------------------------------------
            # Agent Reasoning
            # --------------------------------------------------

            if show_steps:

                trace_lines = []

                for step in result["intermediate_steps"]:

                    action, observation = step

                    trace_lines.append(
                        f"🔧 Tool: {action.tool}"
                    )

                    trace_lines.append(
                        f"📤 Input: {action.tool_input}"
                    )

                    trace_lines.append(
                        f"📥 Output: {observation}"
                    )

                    trace_lines.append(
                        "------------------------------------"
                    )

                if trace_lines:

                    with st.expander(
                        "🧠 Agent Reasoning Trace"
                    ):
                        st.text(
                            "\n".join(trace_lines)
                        )

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

        except Exception as e:

            error_msg = (
                f"⚠️ Something went wrong:\n\n{str(e)}"
            )

            st.error(error_msg)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": error_msg
                }
            )

