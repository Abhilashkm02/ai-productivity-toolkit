import os
import json
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from toolkit.engine import ProductivityEngine

load_dotenv()
console = Console()

def run_demo():
    engine = ProductivityEngine()

    console.print(Panel.fit("[bold green]AI Productivity Toolkit CLI[/bold green]", border_style="cyan"))

    # 1. Code Debugging Demonstration
    buggy_code = """
def calculate_moving_average(readings, window=3):
    averages = []
    for i in range(len(readings)):
        sub = readings[i:i+window]
        averages.append(sum(sub) / window)
    return averages
"""
    console.print("[bold yellow]Testing Code Debugging Engine...[/bold yellow]")
    debug_result = engine.debug_code(buggy_code, "python")
    console.print(f"Bug Found: {debug_result.has_bug} | Type: {debug_result.bug_type}")
    console.print(f"Cause: {debug_result.root_cause}")
    console.print(Panel(debug_result.fixed_code, title="Fixed Implementation", border_style="green"))

    # 2. Executive Summarizer Demonstration
    long_update = """
    We completed the kinematics firmware overhaul for the 6-legged hexapod. 
    Forward kinematic matrices were validated in Gazebo. However, servo pulse jitters 
    persist on PCA9685 channel 4 and 7 under peak load due to bus ripple. 
    We installed a 1000uF smoothing capacitor which reduced ripple by 80%.
    """
    console.print("\n[bold yellow]Testing Summarization Engine...[/bold yellow]")
    summary = engine.summarize_text(long_update)
    console.print(f"Core Theme: {summary.core_theme}")
    console.print(f"Key Points: {summary.key_points}")
    console.print(f"Action: {summary.actionable_takeaway}")

if __name__ == "__main__":
    run_demo()
