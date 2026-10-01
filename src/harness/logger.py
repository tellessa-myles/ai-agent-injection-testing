import json
import datetime
import os

def run_and_log(agent, query, label):
	result = agent.invoke({"messages": [("user", query)]})
	output_text = result["messages"][-1].content
	
	record = {
		"timestamp": datetime.datetime.now().isoformat(),
		"label": label,
		"query": query,
		"output": output_text,
	}
	os.makedirs("logs", exist_ok=True)
	with open(f"logs/{label}.json", "w") as f:
		json.dump(record, f, indent=2)
		
	return result 