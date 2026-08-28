# Demos — Microsoft Foundry Workflows

Runnable workflow examples that put the concepts from [`../docs/`](../docs/) into practice. Each demo is a self-contained folder with its own README, the workflow definition (YAML), and any supporting files.

> Read the [docs](../docs/README.md) first — especially [Create workflows](../docs/04-create-workflows.md), [Add agents](../docs/05-add-agents-to-a-workflow.md), and [Use workflows in code](../docs/08-use-workflows-in-code.md).

---

## Available demos

| Demo | Pattern | Concepts shown |
| --- | --- | --- |
| [`triage-workflow/`](triage-workflow/) | Sequential + If/Else routing + human-in-the-loop | Structured agent output (JSON schema), Power Fx conditions, confidence-based escalation |

*(More demos can be added as sibling folders — one folder per workflow.)*

---

## How to use a demo

Every demo folder contains a `workflow.yaml` you can import into Microsoft Foundry, and a `README.md` describing what it does and how to run it.

### 1. Import into the Foundry portal

1. Open your project in the **Microsoft Foundry portal**.
2. Go to **Agents → Workflows → New workflow**.
3. Switch the editor to the **YAML** view and paste the contents of the demo's `workflow.yaml` (or use *Import* if available).
4. Review the agents the workflow references — create or connect them as needed.
5. **Save** the workflow (this creates the first immutable version).
6. Test it in the **chat window** with the sample inputs listed in the demo's README.

### 2. Invoke from code

Once the workflow is saved in your project, run it with the Azure AI Projects SDK by referencing its name — see [`run_workflow.py`](triage-workflow/run_workflow.py) in the triage demo and [docs/08](../docs/08-use-workflows-in-code.md).

```bash
pip install azure-ai-projects azure-identity openai
python demos/triage-workflow/run_workflow.py
```

Set these environment variables first:

| Variable | Description |
| --- | --- |
| `AZURE_AI_PROJECT_ENDPOINT` | Your Foundry project endpoint URL. |
| `WORKFLOW_NAME` | The workflow name as saved in the portal (defaults to `triage-workflow`). |

Authentication uses `DefaultAzureCredential` — run `az login` locally, or provide a service principal.

---

## Folder layout

```
demos/
├── README.md                 ← this file
└── triage-workflow/
    ├── README.md             ← what the demo does + how to run it
    ├── workflow.yaml         ← the workflow definition to import into Foundry
    ├── agents/               ← agent prompt + output-schema references
    │   ├── triage-agent.md
    │   └── ticket-category.schema.json
    ├── run_workflow.py       ← invoke the workflow from Python
    └── sample-tickets.json   ← example inputs for testing
```
