# MCP_SERVER
Name:- Uday Kiran
Roll no:- 261FB04028

# Building a Python MCP Server with VS Code and GitHub Copilot

A Python-based Model Context Protocol (MCP) server that exposes custom Python functions as tools and enables GitHub Copilot Agent Mode to interact with them.

This project demonstrates how to build, configure, connect, and execute multiple Python MCP tools locally using Visual Studio Code and GitHub Copilot.

## 1. Project Overview

The main objective of this project is to understand the Model Context Protocol (MCP) and how AI applications can interact with external Python functions through an MCP server.

**Project Information**

| Component | Technology |
|---|---|
| Project Name | Hello MCP |
| Programming Language | Python |
| Development Environment | Visual Studio Code |
| AI Client | GitHub Copilot |
| Interaction Mode | Agent Mode |
| MCP SDK | Python MCP SDK |
| Communication Protocol | STDIO |

### Project Architecture

GitHub Copilot Agent Mode communicates with the local Python MCP server through STDIO transport.

The MCP server exposes seven custom tools that perform different operations.

## 2. Tools Implemented

The project currently contains seven Python MCP tools.

| No. | Tool Name | Description |
|---|---|---|
| 1 | `get_greeting` | Generates a personalized greeting. |
| 2 | `add_numbers` | Adds two numbers. |
| 3 | `multiply_numbers` | Multiplies two numbers. |
| 4 | `subtract_numbers` | Subtracts the second number from the first. |
| 5 | `divide_numbers` | Divides two numbers with zero-division validation. |
| 6 | `check_prime` | Checks whether a number is prime. |
| 7 | `factorial` | Calculates the factorial of a non-negative integer. |

## 3. Software Requirements

The following software and tools are required:

- Windows 10 (64-bit)
- Python 3.12.7
- Visual Studio Code
- GitHub account with Copilot access
- GitHub Copilot Agent Mode
- Internet connection
- Python MCP SDK (`mcp[cli]`)

## 4. Step-by-Step Implementation

### Step 1: Create the Project

Created a project folder named `hello-mcp` and opened it in Visual Studio Code.

Opened the integrated terminal and created a virtual environment.

```bash
py -3.12 -m venv .venv
```

**Purpose:** The virtual environment isolates project dependencies and prevents conflicts with other Python projects.

### Step 2: Install MCP Dependencies

Installed the MCP SDK and CLI dependencies.

```powershell
.venv\Scripts\python.exe -m pip install "mcp[cli]" --default-timeout=120
```

Verified the installed package:

```powershell
.venv\Scripts\python.exe -m pip show mcp
```

### Step 3: Initialize the MCP Server

Created a Python file named `server.py`.

Imported and initialized the MCP server:

```python
from mcp.server.mcpserver import MCPServer

mcp = MCPServer("HelloMCP")
```

The `MCPServer` instance acts as the central server to which all seven tools are registered.

### Step 4: Implement the Seven MCP Tools

**Tool 1: Personalized Greeting**

`get_greeting(name: str)`

Accepts a name and returns a personalized greeting.

Example:

```text
Input: Students
Output: Hello, Students! Your first MCP tool works.
```

**Tool 2: Addition**

`add_numbers(a: int, b: int)`

Adds two integer values.

```text
Input: 10, 20
Output: 30
```

**Tool 3: Multiplication**

`multiply_numbers(a: int, b: int)`

Multiplies two integer values.

```text
Input: 10, 20
Output: 200
```

**Tool 4: Subtraction**

`subtract_numbers(a: int, b: int)`

Subtracts the second number from the first number.

```text
Input: 20, 10
Output: 10
```

**Tool 5: Division**

`divide_numbers(a: float, b: float)`

Divides the first number by the second number.

Includes input validation to prevent division by zero.

```text
Input: 20, 5
Output: 4.0
```

If the second number is zero, the function raises a `ValueError`.

**Tool 6: Prime Number Checker**

`check_prime(number: int)`

Checks whether a given integer is a prime number.

The implementation uses a square-root-based iteration to check for divisors rather than testing every number up to the input.

```text
Input: 7
Output: 7 is a prime number.
```

```text
Input: 10
Output: 10 is not a prime number.
```

**Tool 7: Factorial Calculator**

`factorial(number: int)`

Calculates the factorial of a non-negative integer using an iterative approach.

```text
Input: 5
Output: 120
```

The function raises a `ValueError` for negative inputs.

### Step 5: Start the MCP Server

Added the following execution block at the end of `server.py`:

```python
if __name__ == "__main__":
    mcp.run()
```

This starts the MCP server when the Python script is executed.

### Step 6: Configure MCP in VS Code

Created a `.vscode` directory in the project root.

Created the configuration file:

`.vscode/mcp.json`

Added the following configuration:

```json
{
    "servers": {
        "helloMcp": {
            "type": "stdio",
            "command": "${workspaceFolder}\\.venv\\Scripts\\python.exe",
            "args": ["server.py"]
        }
    }
}
```

**Configuration explanation:**

- `helloMcp`: MCP server configuration name.
- `type`: Specifies STDIO communication.
- `command`: Points to the Python interpreter inside the virtual environment.
- `args`: Specifies the Python server script.

This configuration enables VS Code to launch the local Python MCP server.

### Step 7: Start and Connect the MCP Server

After saving all project files:

1. Opened the VS Code Command Palette using `Ctrl + Shift + P`.
2. Searched for `MCP: List Servers`.
3. Selected `helloMcp`.
4. Started or restarted the MCP server.
5. Checked the MCP output panel.

The original implementation confirmed a successful connection and discovery of two tools. With the updated implementation, the expected discovery count is seven.

### Step 8: Test MCP Tools Through GitHub Copilot

Opened GitHub Copilot Chat and enabled Agent Mode.

Used natural-language prompts to invoke the registered tools.

**Example prompts:**

Greeting:

```text
Use get_greeting with the name Students.
```

Addition:

```text
Use add_numbers with a = 10 and b = 20.
```

Multiplication:

```text
Use multiply_numbers with a = 10 and b = 20.
```

Subtraction:

```text
Use subtract_numbers with a = 20 and b = 10.
```

Division:

```text
Use divide_numbers with a = 20 and b = 5.
```

Prime checking:

```text
Use check_prime to check whether 7 is a prime number.
```

Factorial:

```text
Use factorial to calculate the factorial of 5.
```

Copilot Agent Mode can identify the appropriate MCP tool, provide its arguments, execute it, and display the returned result.

## 5. Error Handling and Validation

The implementation includes validation for mathematical operations that have invalid inputs.

| Tool | Validation |
|---|---|
| `divide_numbers` | Prevents division by zero. |
| `factorial` | Rejects negative integers. |
| `check_prime` | Handles numbers less than or equal to 1 as non-prime. |

These checks help prevent invalid calculations and return meaningful errors.

## 6. Troubleshooting

| Problem | Solution |
|---|---|
| MCP module import error | Verify the installed SDK and its supported import path. |
| Python interpreter not found | Verify the `.venv` interpreter path. |
| Pip installation timeout | Use `--default-timeout=120`. |
| MCP server does not start | Check Python syntax, configuration paths, and MCP logs. |
| Copilot does not invoke tools | Check Agent Mode, server connection, tool discovery, and permissions. |
| Tool not discovered | Verify that the function has the `@mcp.tool()` decorator. |

## 7. Final Project Structure

```text
hello-mcp/
│
├── server.py
├── requirements.txt
├── .gitignore
├── .venv/
│
└── .vscode/
    └── mcp.json
```

**File descriptions:**

- `server.py`: Contains the MCP server and seven registered Python tools.
- `requirements.txt`: Stores the required Python dependencies.
- `.gitignore`: Excludes unnecessary files from Git.
- `.venv/`: Isolated Python environment.
- `.vscode/mcp.json`: MCP server configuration for VS Code.

### requirements.txt

```text
mcp[cli]
```

### .gitignore

```gitignore
.venv/
__pycache__/
*.py[cod]
.env
```

## 8. Key Learnings

Through this project, I gained practical experience in:

- Understanding the fundamentals of Model Context Protocol (MCP).
- Building a local MCP server using Python.
- Registering multiple Python functions as MCP tools.
- Understanding STDIO-based client-server communication.
- Configuring MCP servers inside Visual Studio Code.
- Integrating Python MCP tools with GitHub Copilot Agent Mode.
- Implementing mathematical operations and input validation.
- Understanding how AI agents discover and invoke external tools.

## 9. Conclusion

This project demonstrates how Python functionality can be exposed through a local Model Context Protocol server and accessed through GitHub Copilot Agent Mode.

Starting with a basic greeting and addition server, the implementation was expanded to seven custom tools covering arithmetic operations, prime-number checking, and factorial calculation.

The project provided hands-on experience with MCP server development, tool registration, STDIO communication, VS Code integration, and AI-powered tool execution.

---

**Technologies:** Python | Model Context Protocol (MCP) | VS Code | GitHub Copilot | STDIO
