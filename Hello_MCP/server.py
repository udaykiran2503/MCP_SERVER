
from mcp.server.mcpserver import MCPServer

mcp = MCPServer("HelloMCP")


@mcp.tool()
def get_greeting(name: str) -> str:
    """Return a greeting for a student."""
    return f"Hello, {name}! Your first MCP tool works."


@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@mcp.tool()
def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


@mcp.tool()
def subtract_numbers(a: int, b: int) -> int:
    """Subtract the second number from the first number."""
    return a - b


@mcp.tool()
def divide_numbers(a: float, b: float) -> float:
    """Divide the first number by the second number."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


@mcp.tool()
def check_prime(number: int) -> str:
    """Check whether a number is prime or not."""
    if number <= 1:
        return f"{number} is not a prime number."

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return f"{number} is not a prime number."

    return f"{number} is a prime number."


@mcp.tool()
def factorial(number: int) -> int:
    """Calculate the factorial of a number."""
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    result = 1

    for i in range(1, number + 1):
        result *= i

    return result


if __name__ == "__main__":
    mcp.run()
