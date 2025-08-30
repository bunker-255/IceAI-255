from src import BASE, tools
from datetime import datetime
import os
from pprint import pprint
import json
import subprocess

z = BASE.Zai()
os.system("clear")


conversation_id = str(datetime.now()).split(".")[0]
if conversation_id not in os.listdir("conversation"):
    tools.pick(f"conversation/{conversation_id}", {"messages": z.messages, 'title': z.title})

z.init_messages(f"conversation/{conversation_id}")


user_input = None
while True:
    if not user_input:
        user_input = input("[USER] ")

        if user_input.lower() in ["exit", "quit", "выход", "выйти"]:
            break
    user_input = z.mind_navbar("user", user_input)
    z.add_to_messages("user", user_input)
    z.save_messages()


    response = z.send_message()
    z.add_to_messages("assistant", response)
    z.save_messages()


    response = response.replace("```json\n", "").replace("```", "")
    try:
        response = json.loads(response)
        if response['type'] == "python":
            func_title = response.get("title", "Выполняю код...")
            print(f"[ACTION] {func_title}")
            code = response['content']
            user_input = z.mind_navbar("user", user_input)
            code = code.replace("```python", "").replace("```", "")
            std = subprocess.run(["python3", "-c", code], capture_output=True, text=True)
            if std.stderr:
                user_input = z.mind_navbar("system", str({
                        "code_exec_status": "error",
                        "code_exec_result": f"{std.stderr}"
                    }))
                
            else:
                user_input = z.mind_navbar("system", str({
                        "code_exec_status": "error",
                        "code_exec_result": f"{std.stdout}"
                    }))
                
        elif response['type'] == "bash":
            func_title = response.get("title", "Выполняю код...")
            print(f"[ACTION] {func_title}")
            code = response['content']
            code = code.replace("```bash", "").replace("```", "")
            std = subprocess.run(code, shell=True, capture_output=True, text=True)
            if std.stderr:
                user_input = z.mind_navbar("system", str({
                        "code_exec_status": "error",
                        "code_exec_result": f"{std.stderr}"
                    }))
                
            else:
                user_input = z.mind_navbar("system", str({
                        "code_exec_status": "error",
                        "code_exec_result": f"{std.stdout}"
                    }))

        elif response['type'] == "text":
            user_input = z.mind_navbar("user", response.get("content", ""))
            print(f"[ASSISTANT] {response.get('content', '')}")
            
            if response.get("done", False):

                user_input = None

    except Exception as e:
        import traceback

        response = {
            "type": "text",
            "content": f"Error parsing JSON response: {str(e)}\nOriginal response: {response}",
            "done": False
        }
        user_input = z.mind_navbar("user", response.get("content", ""))
    

    


