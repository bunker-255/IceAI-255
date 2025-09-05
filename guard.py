from src import BASE, tools
from datetime import datetime
import os
from pprint import pprint
import json
import subprocess

z = BASE.Zai()
os.system("clear")

# Переменная данных о системе
system_data = None


while True:
    system_data_0 = system_data
    
    # Данные о системе оборачиваем в мыслительную панель Модели
    system_data = z.mind_navbar("user", system_data)
    
    # Добавляем сообщение в историю Модели
    z.add_to_messages("user", system_data)

    # Генерируем ответ при помощи Модели на основе истории
    response = z.send_message()
    
    
    # Добавляем ответ Модели в историю сообщений
    z.add_to_messages("assistant", response)

    # Json фильтрация
    response = response.replace("```json\n", "").replace("```", "")
    
    try:
        # Формирование json кода
        response = json.loads(response)
        
        # Если тип сообщения является "python"
        if response['type'] == "python":
            func_title = response.get("title", "Выполняю код...")
            z.log(f"[ACTION] {func_title}", type="guard", filename=f"this_conver.log")
            print(f"[ACTION] {func_title}")
            code = response['content']
            
            
            system_data = z.mind_navbar("user", system_data)
            code = code.replace("```python", "").replace("```", "")
            std = subprocess.run(["python3", "-c", code], capture_output=True, text=True)
            if std.stderr:
                system_data = z.mind_navbar("system", str({
                        "code_exec_status": "error",
                        "code_exec_result": f"{std.stderr}"
                    }))
                
                
            else:
                system_data = z.mind_navbar("system", str({
                        "code_exec_status": "error",
                        "code_exec_result": f"{std.stdout}"
                    }))
        
        # Если тип сообщения является "bash"        
        elif response['type'] == "bash":
            func_title = response.get("title", "Выполняю код...")
            z.log(f"[ACTION] {func_title}", type="guard", filename=f"this_conver.log")
            print(f"[ACTION] {func_title}")
            code = response['content']
            code = code.replace("```bash", "").replace("```", "")
            std = subprocess.run(code, shell=True, capture_output=True, text=True)
            if std.stderr:
                system_data = z.mind_navbar("system", str({
                        "code_exec_status": "error",
                        "code_exec_result": f"{std.stderr}"
                    }))
                
            else:
                system_data = z.mind_navbar("system", str({
                        "code_exec_status": "error",
                        "code_exec_result": f"{std.stdout}"
                    }))

        # Если тип сообщения является "text"
        elif response['type'] == "text":
            system_data = z.mind_navbar("user", response.get("content", ""))
            
            # Логируем результаты   
            z.log(f"[SYSTEM] {system_data_0}", type="guard", filename=f"this_conver.log")
            z.log(f"[ASSISTANT] {response}", type="guard", filename=f"this_conver.log")
            print(f"[SYSTEM] {response.get('content', '')}")
            
            if response.get("done", False):

                system_data = None

    except Exception as e:
        import traceback

        response = {
            "type": "text",
            "content": f"Error parsing JSON response: {str(e)}\nOriginal response: {response}",
            "done": False
        }
        system_data = z.mind_navbar("user", response.get("content", ""))
    
    

    


