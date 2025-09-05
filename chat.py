from src import BASE, tools
from datetime import datetime
import os
from pprint import pprint
import json
import subprocess

# Переменная данных о системе
z = BASE.Zai()
z.sended_from = "Linux Terminal (CLI)"

# Очистка экрана
os.system("clear")

# Инициализация или загрузка истории сообщений
conversation_id = str(datetime.now()).split(".")[0]
if conversation_id not in os.listdir("conversation"):
    tools.pick(f"conversation/{conversation_id}", {"messages": z.messages, 'title': z.title})

z.init_messages(f"conversation/{conversation_id}")


user_input = None
while True:
    if not user_input:
        user_input = input("[USER] ")
        z.log(f"[USER] {user_input}", type="chat", filename=f"this_conver.log")

        if user_input.lower() in ["exit", "quit", "выход", "выйти"]:
            break
    
    user_input_0 = user_input

    user_input = z.mind_navbar("user", user_input)
    z.add_to_messages("user", user_input)
    z.save_messages()

    response = None
    while not response:
        try:
            response = z.send_message()
        except Exception as e:
            import time

            print(f"Error: {str(e)}. Retrying...")
            time.sleep(2)
            
    
    z.add_to_messages("assistant", response)
    
    

    response = response.replace("```json\n", "").replace("```", "")
    try:
        response = json.loads(response)
        if response['type'] == "python":
            func_title = response.get("title", "Выполняю код...")
            print(f"[ACTION] {func_title}")
            z.log(f"[ACTION] {func_title}", type="chat", filename=f"this_conver.log")

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
            z.log(f"[ACTION] {func_title}", type="chat", filename=f"this_conver.log")
            code = response['content']
            code = code.replace("```bash", "").replace("```", "")
            std = subprocess.run(code, shell=True, capture_output=True, text=True)
            if std.stderr:
                user_input = str({
                        "code_exec_status": "error",
                        "code_exec_result": f"{std.stderr}"
                    })
                
            else:
                user_input = str({
                        "code_exec_status": "success",
                        "code_exec_result": f"{std.stdout}"
                    })

        elif response['type'] == "text":
            user_input_0 = response.get("content", "")
            user_input = z.mind_navbar("user", user_input_0)

            z.log(f"[ASSISTANT] {response.get('content', '')}", type="chat", filename=f"this_conver.log")
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
        user_input = response.get("content", "")
    

    


