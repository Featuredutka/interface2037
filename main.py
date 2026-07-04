import sys
from lm_studio import LMStudioProvider
from ui import simulate_boot, print_persona_msg, show_prompt, console, movie_print
from rich.markdown import Markdown

def main():
    simulate_boot()
    print_persona_msg("INTERFACE 2037 READY FOR INQUIRY")
    
    # Defaulting to LM Studio as requested
    provider = LMStudioProvider()
    models = provider.get_models()
    
    selected_model = models[0]
    
    if selected_model not in models and models:
        print_persona_msg(f"Error: Model '{selected_model}' not found in local registry.")
        sys.exit(1)

    while True:
        user_input = show_prompt("\n[alien_amber][/alien_amber]")
        
        if user_input.lower() in ["exit", "quit"]:
            print_persona_msg("DISCONNECT")
            break
        
        if not user_input.strip():
            continue

        response = provider.generate_response(user_input, model=selected_model).upper()
        
        # Displaying response with markdown support for a nicer look
        md = Markdown(response)
        # This forces the alien_green theme style onto the Markdown rendering
        movie_print(md)

        

if __name__ == "__main__":
    main()
