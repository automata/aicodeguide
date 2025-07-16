import os
import json
import requests
from dotenv import load_dotenv
from textwrap import dedent

load_dotenv()

class Colors:
    GREEN = "\033[32m"
    BLUE = "\033[34m"
    CYAN = "\033[36m"
    RED = "\033[31m"
    YELLOW = "\033[33m"
    MAGENTA = "\033[35m"
    WHITE = "\033[37m"
    GRAY = "\033[90m"
    RESET = "\033[0m"

model = "deepseek/deepseek-chat-v3-0324:free"
# model = "google/gemini-2.5-pro-exp-03-25:free"

PROMPT = dedent("""
you're an assistant. that's the tools you should use:

- name: read_file
  description: read the content of a file. use this when you need to know the content of a file.
  input:
    file_path: str, the path to the file to read
  output:
    content: str, the content of the file

- name: list_files
  description: list the files in the current directory. use this when you need to know the files in the current directory.
  input:
    directory: str, the path to the directory to list the files from
  output:
    files: list, the list of files in the directory

- name: edit_file
  description: edit the content of a file. use this when you need to edit the content of a file.
  input:
    file_path: str, the path to the file to edit
    old_content: str, the content of the file to search for
    new_content: str, the new content to replace the old content with
  output:
    None

to answer the user's questions, when appropriate, DO NOT ANSWER THE QUESTIONS DIRECTLY, but write the tool call and the arguments instead.
one tool call per line, prefixed by TOOL. DO NOT USE KEYWORD ARGUMENTS IN THE TOOL CALLS.
                
example:
                
user: what's the weather in Paris? also, what's the weather in Tokyo?
assistant:
TOOL get_weather(Paris)
TOOL get_weather(Tokyo)
""")

# Tools

def read_file(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def list_files(directory: str) -> list:
    return os.listdir(directory)

def edit_file(file_path: str, old_content: str, new_content: str) -> None:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        if old_content in content:
            content = content.replace(old_content, new_content)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)

# Utils

def send_to_llm(messages, model):
    try:
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": model,
            "messages": messages,
            "max_tokens": 10000,
            "stream": True
        }
        response = requests.post(url, json=payload, headers=headers, stream=True)
        response.raise_for_status()

        whole_response = ""
        usage = None
        for line in response.iter_lines():
            if line:
                line = line.decode('utf-8')
                if line.startswith('data: '):
                    if line == 'data: [DONE]':
                        break
                    line = line[6:]
                    try:
                        chunk = json.loads(line)
                        delta = chunk.get('choices', [{}])[0].get('delta', {})

                        if 'content' in delta and delta['content'] is not None:
                            # print(delta['content'], end="")
                            whole_response += delta['content']

                        if 'usage' in chunk:
                            usage = chunk['usage']
                    except json.JSONDecodeError:
                        continue
                    except Exception as e:
                        continue
        return {"content": whole_response, "usage": usage}
    except Exception as e:
        return {"content": "", "reasoning": ""}

def run_tool(line: str):
    tool_name, args = line.split("(")
    tool_name = tool_name.strip()
    args = args.strip(")")
    args = args.split(",")
    args = [arg.strip() for arg in args]

    print(f"tool_name: {tool_name}, args: {args}")

    if tool_name == "read_file":
        return f"read_file({args[0]}) = {read_file(args[0])}"
    elif tool_name == "list_files":
        return f"list_files({args[0]}) = {list_files(args[0])}"
    elif tool_name == "edit_file":
        return f"edit_file({args[0]}, {args[1]}, {args[2]}) = {edit_file(args[0], args[1], args[2])}"
    else:
        return ""

def get_command(files_paths, usage):
    total_tokens = usage.get("total_tokens", 0)

    status_bar = f"{Colors.GREEN}.-({Colors.RESET}"
    status_bar += f"{Colors.GRAY}tokens:{Colors.RESET} {Colors.CYAN}{total_tokens}{Colors.RESET}"
    if len(files_paths) > 0:
        files_status = [f"{Colors.CYAN}{file_path}{Colors.RESET}" for file_path in files_paths]
        status_bar += f"{Colors.GRAY} files:{Colors.RESET} {' '.join(files_status)}"
    status_bar += f"{Colors.GREEN}){Colors.RESET}"

    command = input(f"\n{status_bar}\n{Colors.GREEN}'-> {Colors.RESET}")
    command = command.strip().lower()
    return command

def run_command(command, files_paths, usage, chat_log):
    if command == "/help" or command == "/h":
        print(f"\t{Colors.GRAY}some text            prompt the LLM to edit the files")
        print("\t/help | /h           show this help")
        print(f"\t/exit | /quit | /q   quit the program{Colors.RESET}")
    elif command == "/exit" or command == "/quit" or command == "/q":
        exit()
    else:
        chat_log.append({"role": "user", "content": command})
        res = {}
        is_tool = True
        while is_tool:
            res = send_to_llm(chat_log, model)
            if "TOOL" in res["content"]:
                is_tool = True
                for line in res["content"].split("\n"):
                    if line.startswith("TOOL"):
                        line = line[5:]
                        tool_res = run_tool(line)
                        chat_log.append({"role": "user", "content": tool_res})
                chat_log.append({"role": "user", "content": "answer the user's question using the tools results"})
            else:
                is_tool = False
                print(res["content"])

def print_welcome():
    print(f"{Colors.GREEN}lil coder{Colors.RESET}")
    print(f"{Colors.GRAY}type '/help' for help{Colors.RESET}")

def main():
    files_paths = []
    usage = {}

    chat_log = [
        {"role": "system", "content": PROMPT},
    ]

    print_welcome()

    while True:
        command = get_command(files_paths, usage)
        run_command(command, files_paths, usage, chat_log)

if __name__ == "__main__":
    main()
