
# Interface 2037

A small on-evening project that was inspired by "Alien". A termial interface imitating Weyland-Utani "Mother" ship AI (or Sevastopol's "Apollo" - whichever you prefer better). Provides a stylized way to interact with local LLMs.

## Prerequisites

- **Python 3.10+**
- **LM Studio**: For running local models - connection is now possible with LM Studio interface only
- **Ollama**: (Optional) For alternative local LLM backends.

## 📥 Installation

1. **Clone the repository** (or navigate to the project folder):
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🖥️ Usage

### Step 1: Prepare your Local Model
1. Open **LM Studio**.
2. Download and load your preferred model (e.g., Llama 3, Mistral - tested with Gemma4-E4B-8bit and DeepDeek-R1-0528-Qwen3-8B).
3. Go to the **Local Server** tab and click **Start Server**.
4. Ensure the server is running on the default port (usually `http://localhost:1234`).

### Step 2: Launch the Interface
Run the main script:
```bash
python3 main.py
```

### Interaction
- The system will perform a "boot sequence" before entering the main loop.
- Interface automatically selects the first available models (#TODO).
- Type `EXIT` or `QUIT` to safely disconnect from the terminal.