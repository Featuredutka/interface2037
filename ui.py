import sys
import time
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.theme import Theme

# Custom theme for the Alien vibe
alien_theme = Theme({
    "alien_green": "bold green",
    "alien_amber": "bold yellow",
    "warning": "bold red",
    "dim": "dim",
    "boot_text": "bold green",
    "glitch": "bold red italic"
})
console = Console(theme=alien_theme)

def print_header():
    # Clear the screen
    print("\033[H\033[J", end="", flush=True) 
    header_text = Text("SYSTEM STATUS: ONLINE\nSECTOR: 7 - ISOLATION_ZONE\nUSER_IDENTITY: RECOVERY_UNIT_01", style="alien_green")
    console.print(Panel(header_text, border_style="alien_amber", title="Weyland-Yutani Corp."))

def simulate_boot():
    # Clear the screen
    print("\033[H\033[J", end="", flush=True)
    
    boot_sequence = [
        ("INITIALIZING WEYLAND-YUTANI OS...", 0.6),
        ("CONNECTING TO NEURAL INTERFACE...", 0.8),
        ("SCANNING LOCAL HARDWARE...", 0.5),
        ("CORE_TEMP: 42C [OK]", 0.3),
        ("MEMORY_BUFFER: 1024GB [READY]", 0.3),
        ("NEURAL_LINK: ESTABLISHED", 0.4),
        ("SECURITY_PROTOCOL: LEVEL_4", 0.4),
        ("LOADING AI_PERSONALITY_MATRIX...", 0.7),
        ("[GLITCH] SIGNAL_INTERFERENCE_DETECTED", 0.9),
        ("RECALIBRATING...", 0.5),
        ("DATA_FRAGMENT_RECOVERY_FAILURE", 0.6),
        ("BIO_SIGN_NULL", 0.4),
        ("SYSTEM_CORRUPTION_REPAIRED", 0.5),
        ("PROXIMITY_ALERT_NULL", 0.3),
        ("SYSTEM_READY", 0.8),
        ("...", 1.0)
    ]
    
    for line, delay in boot_sequence:
        style = "glitch" if "[GLITCH]" in line else "boot_text"
        console.print(f"[{style}]{line}[/{style}]")
        time.sleep(delay)
    
    time.sleep(1.5)
    print_header()

def print_persona_msg(message: str):
    # Father/Apollo style: Clinical, slightly eerie, technical
    console.print(f"\n[alien_amber]LOG_ENTRY:[/alien_amber] {message}\n")

def movie_print(text: str, delay: float = 0.02):
    """Prints text one character at a time with a minor delay.
    
    Supports Rich tags by rendering the style first.
    """
    # We use console.render_with_markup to preserve your alien_themes
    with console.capture() as capture:
        console.print(text, style="alien_green", end="")
    
    rendered_text = capture.get()
    
    # Print the rendered ANSI string character by character
    # Note: This handles standard text beautifully. 
    for char in rendered_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
        
    print() # Print a final newline at the end

def show_prompt(prompt_text: str):
    # Prompt text in green
    console.print(f"\n[alien_green]{prompt_text}[/alien_green]")
    
    # Get input (echoed by default)
    user_input = console.input()
    
    # Capitalize input
    capitalized_input = user_input.upper()
    
    # Print the finalized input in green and underlined
    # We use a space to separate from the prompt
    print("\033[H\033[J", end="", flush=True)
    console.print(f"[alien_green]{capitalized_input}[/alien_green]", style="underline")
    console.print()

    return capitalized_input
