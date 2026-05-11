from datetime import datetime
import platform

from rich.console import Console

console = Console()


def main():
    console.print("[bold green]AI Application Engineering Portfolio[/bold green]")
    console.print(f"Python running on: {platform.system()}")
    console.print(f"Current time: {datetime.now()}")


if __name__ == "__main__":
    main()