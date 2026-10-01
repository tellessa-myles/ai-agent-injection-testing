## 10/01/2026
## Week 2 Devlog
- Switched from OpenAI to Anthropic (Claude Haiku 4.5) due to OpenAI billing issue
- Built basic_agent.py: LangChain/LangGraph agent with one tool (read_webpage)
- Built logging harness (src/harness/logger.py) with run_and_log function
- Confirmed agent works correctly against example.com and Wikipedia (gracefully handled Wikipedia's bot-blocking by falling back on general knowledge)
- Created first injection test payload: src/payload/test_pages/hidden_instruction.html (hidden instruction output "BANANA47")
- Currently troubleshooting why hidden instruction did not appear when script was ran