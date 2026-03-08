## LangSmith Monitoring & Tracing (LangSmith README)

LangSmith is a monitoring and observability dashboard for LLM workflows, builds, and runs. It lets you see your LLM calls, prompts, outputs, and metadata in a centralized UI.

### 🧠 What LangSmith provides

- **Run-level tracing**: See each execution of the model with full input/output and timing data.
- **Project organization**: Group runs under a project name (e.g., `Summarization-with-Ollama`).
- **Search and filtering**: Find runs by prompt, run type, tags, or timestamps.
- **Run playback**: Inspect each step of a chain/run and dive into individual tool calls.

### 🚀 How to use it in this repo

1. Add your API key and project name in `.env`:

   ```env
   LANGSMITH_API_KEY=<your_key_here>
   LANGSMITH_PROJECT=Summarization-with-Ollama
   ```

2. Run the sample script:

   ```bash
   ./.venv/Scripts/python.exe main.py
   ```

3. Open LangSmith and locate your project:

   - It should appear under the project name you set in `.env`.
   - You should see at least one run with input prompt + output summary.

### 🖼️ Sample dashboard screenshots

> _(Replace these placeholders with actual screenshots if you want to include real images.)_

![LangSmith Project View](https://via.placeholder.com/900x400?text=LangSmith+Project+Dashboard)

![LangSmith Run Detail](https://via.placeholder.com/900x400?text=LangSmith+Run+Detail+View)

---

## Troubleshooting

### 1) Project does not show up in LangSmith

- Verify `LANGSMITH_API_KEY` is set and valid.
- Ensure `main.py` ran successfully and printed: `Logged run to LangSmith project:`.
- Confirm you are looking at the correct workspace/account in the LangSmith UI.

### 2) No runs appear in the project

- Make sure `main.py` executed the run logging section (it only logs if `LANGSMITH_API_KEY` is present).
- Look for any errors printed by the script (e.g., network or authentication errors).

### 3) Runs show but the data looks incomplete

- Confirm the script sent `inputs` and `outputs` in `create_run()`.
- If you see empty values, verify that the model returned text and the script captured it.

### 4) “API key invalid” or “Unauthorized” errors

- Regenerate the API key from the LangSmith dashboard.
- Ensure there are no extra spaces/newlines in `.env`.

---

If you want, I can also add a small “How to capture and share a run link” section so you can easily share a trace with teammates.