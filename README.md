## 📄 Autonomous Web Agent for Research & PDF Generation

This project uses `browser_use.Agent` with Gemini 2.0 to automate web browsing and summarization.

### 🚀 Features:
- 🧠 AI agent that accepts any user prompt and searches the web accordingly.
- 🌐 Uses a headless/non-headless browser to interact with real sites (e.g., Arxiv, Uber).
- 📝 Summarizes data from online sources using Gemini LLM (`temperature=0.1`).
- 📄 Outputs final summary and supports future PDF generation.

### 🧪 Example Task
```python
task="Analyse the recent Arxiv AI papers and summarize the key findings"
