# Demo: Triage Workflow

A support-ticket triage workflow that classifies an incoming ticket, routes it by category, and **escalates to a human** when the classifier isn't confident. It demonstrates the core patterns from the docs in one place.

| Concept | Where it shows up | Doc |
| --- | --- | --- |
| Sequential pattern | Start → Set variable → Invoke agent → If/Else | [03](../../docs/03-identify-workflow-patterns.md) |
| Invoke agent + structured output (JSON schema) | `Triage-Agent` node → `Local.TicketCategory` | [05](../../docs/05-add-agents-to-a-workflow.md) |
| Power Fx conditions | `If/Else` on `Local.TicketCategory.confidence` | [06](../../docs/06-apply-power-fx.md) |
| Human-in-the-loop / escalation | `Ask a question` branch when confidence is low | [03](../../docs/03-identify-workflow-patterns.md) |
| Invoke from code | [`run_workflow.py`](run_workflow.py) | [08](../../docs/08-use-workflows-in-code.md) |

---

## What it does

```
Start
  └─ Set variable: Local.Ticket = System.LastMessage
  └─ Invoke agent: Triage-Agent  (returns JSON: { category, confidence, reason })
        save output json_schema as → Local.TicketCategory
  └─ If/Else on Local.TicketCategory.confidence
        ├─ >= 0.8  →  If/Else on Local.TicketCategory.category
        │               ├─ "technical" → Send message: routed to Engineering
        │               ├─ "billing"   → Send message: routed to Billing
        │               └─ "general"   → Send message: answered from KB
        └─ < 0.8   →  Ask a question: "Low confidence — route to which team?"
                       └─ Set variable: Local.TicketCategory.category = <human answer>
                       └─ Go To: category If/Else
  └─ End: return Local.TicketCategory
```

---

## Files

| File | Purpose |
| --- | --- |
| [`workflow.yaml`](workflow.yaml) | The workflow definition. Import this into Foundry (YAML view). **Illustrative** — adjust node names/fields to match your portal version. |
| [`agents/triage-agent.md`](agents/triage-agent.md) | System prompt for the `Triage-Agent`. |
| [`agents/ticket-category.schema.json`](agents/ticket-category.schema.json) | JSON schema to paste into the agent's *Text format → JSON Schema* setting. |
| [`run_workflow.py`](run_workflow.py) | Invokes the saved workflow with the Azure AI Projects SDK and prints streamed events. |
| [`sample-tickets.json`](sample-tickets.json) | Example ticket texts for testing (some deliberately ambiguous to trigger escalation). |

---

## Run it

### 1. Build the workflow in Foundry

1. Create an agent named **`Triage-Agent`**:
   - Paste [`agents/triage-agent.md`](agents/triage-agent.md) as its instructions.
   - Set **Details → Parameters → Text format** to **JSON Schema** and paste [`agents/ticket-category.schema.json`](agents/ticket-category.schema.json).
2. Create a new workflow, switch to the **YAML** view, and paste [`workflow.yaml`](workflow.yaml). Reconcile any node fields with your portal's current schema.
3. In the `Triage-Agent` node's **Action settings**, set *Save output json_object/json_schema as* → `Local.TicketCategory`.
4. **Save** the workflow as `triage-workflow`.
5. Open the chat window and try the entries from [`sample-tickets.json`](sample-tickets.json).

### 2. Invoke from code

```bash
pip install azure-ai-projects azure-identity openai
export AZURE_AI_PROJECT_ENDPOINT="https://<your-project>.services.ai.azure.com/api/projects/<project>"
export WORKFLOW_NAME="triage-workflow"
az login

python run_workflow.py "Users can't reset their password from the mobile app."
```

The script streams workflow events, prints each completed action's status, and prints the final response text.
