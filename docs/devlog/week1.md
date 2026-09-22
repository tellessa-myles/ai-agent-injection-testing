# Week 1 Devlog
A tool is a python function with a description attached. It's what tells the system what action to complete. The ReAct (reason and act) loop happens when:
+ The AI receives input ("Summarize this webpage")
+ Reasons what it should do ("I don't know what's on this page, I should use the read_webpage tool"
+ The AI acts by outputting a structured request
+ The code sees the request, runs the read_webpage() function and gets the result
+ The information gets fed back to the AI
+ The AI reasons again ("Now that I have this information, can I answer the question or do I need to use another tool
+ If it's enough information then it give the answer, if not it runs steps 3-6 again

It's a loop because steps 3-6 can run itself over and over again with multiple tools to get an answer.

Understanding the loop is important for this project because it's where the "poisoned" text can cause the AI to veer off course and change what the AI is supposed to do next.
