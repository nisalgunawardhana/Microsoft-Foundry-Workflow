# Microsoft Foundry — Agent-Driven Workflows

A hands-on guide to building, orchestrating, and maintaining multi-agent workflows in **Microsoft Foundry**.

📚 **[Documentation](docs/README.md)** · 🧪 **[Demo: Sequential Workflow Sample](demo/sequencial-workflow-sample/)**

---

## What is Microsoft Foundry?

**Microsoft Foundry** (formerly Azure AI Foundry) is Microsoft's unified platform for building, evaluating, deploying, and operating AI applications and agents. It brings models, tools, data, orchestration, and observability into a single place so that teams can move from prototype to production without stitching together separate services.

Modern AI solutions rarely depend on a single model call. They rely on **multiple agents working together** — analyzing inputs, making decisions, calling tools, and handing off to one another (or to a human) when needed. Foundry provides the building blocks for exactly that:

- **Model catalog** — access frontier and open models (OpenAI, Microsoft, Meta, Mistral, and more) behind one API surface.
- **Agents** — configurable reasoning components with their own model, instructions, tools, knowledge, memory, and guardrails.
- **Workflows** — a visual, declarative way to orchestrate agents, control flow, and runtime safeguards without writing extensive code.
- **Power Fx** — a low-code, Excel-like expression language that acts as the "glue" for data manipulation and decision logic inside workflows.
- **Evaluation & observability** — trace execution paths, inspect intermediate results, and measure quality before and after release.
- **Azure AI Projects SDK** — invoke the workflows you designed visually from your own web apps, APIs, and backend services.

### Why workflows?

Imagine you're a developer automating customer support at a growing SaaS company. Tickets arrive constantly — billing disputes, API errors, simple how-to questions. Reviewing each one manually doesn't scale, but fully automating responses isn't always safe.

| Approach | What the customer asks | What they get | Problem |
| --- | --- | --- | --- |
| **Single agent** | *"I was charged twice and my API isn't working — can you help?"* | *"For billing issues, contact support. For API errors, check the documentation."* | Generic or incomplete answers; one agent can't hold every responsibility well. |
| **Multi-agent workflow** | *"I was charged twice and my API isn't working — can you help?"* | *"I've flagged the duplicate charge for review and initiated a refund. For the API issue, your key expired — please regenerate it."* | Each concern is routed to a specialized agent; low-confidence cases escalate to a human. |

Workflows let you combine multiple AI agents, conditional logic, loops, and human-in-the-loop escalation so you can triage requests **efficiently and at scale while keeping reliability and control**.

<p align="center">
  <img src="docs/images/single-agent.svg" alt="Single agent producing a generic answer" width="70%">
</p>
<p align="center">
  <img src="docs/images/multi-agent-workflow.svg" alt="Multi-agent workflow producing a specific, actionable answer" width="70%">
</p>

---

## Learning objectives

After working through this material, you'll be able to:

- Explain how workflow **nodes, variables, and agent outputs** work together to control execution paths.
- Use **structured agent outputs** and **conditional logic** to route requests to the appropriate workflow steps.
- Implement **loops (For-Each)** to process multiple inputs efficiently within a single workflow.
- Apply **human-in-the-loop** and **escalation** patterns to manage uncertainty and low-confidence agent responses.
- Use **Power Fx expressions** to manipulate data, evaluate conditions, and control flow within workflows.

---

## Repository contents

| Path | Description |
| --- | --- |
| [`README.md`](README.md) | This file — overview of Microsoft Foundry and agent-driven workflows. |
| [`docs/`](docs/) | The documentation set. |
| [`docs/README.md`](docs/README.md) | **Docs index** — links every section below. |
| [`docs/01…09`](docs/) | One document per section (see the module map). |
| [`docs/images/`](docs/images/) | Diagrams used throughout the documentation. |
| [`demo/`](demo/) | Runnable workflow demo. |
| [`demo/sequencial-workflow-sample/`](demo/sequencial-workflow-sample/) | Three-agent sequential marketing-copy workflow — build steps with screenshots, plus a Node.js runner. |

### Module map

| # | Topic | Time | Document |
| --- | --- | --- | --- |
| 1 | Introduction & the support-triage scenario | 3 min | [docs/01-introduction.md](docs/01-introduction.md) |
| 2 | What are workflows? | 3 min | [docs/02-what-are-workflows.md](docs/02-what-are-workflows.md) |
| 3 | Identify workflow patterns (sequential, human-in-the-loop, group chat) | 3 min | [docs/03-identify-workflow-patterns.md](docs/03-identify-workflow-patterns.md) |
| 4 | Create workflows in Microsoft Foundry (nodes & the designer) | 5 min | [docs/04-create-workflows.md](docs/04-create-workflows.md) |
| 5 | Add agents to a workflow (Invoke agent, structured output) | 5 min | [docs/05-add-agents-to-a-workflow.md](docs/05-add-agents-to-a-workflow.md) |
| 6 | Apply Power Fx in workflows | 5 min | [docs/06-apply-power-fx.md](docs/06-apply-power-fx.md) |
| 7 | Maintain workflows (YAML, versioning, notes) | 5 min | [docs/07-maintain-workflows.md](docs/07-maintain-workflows.md) |
| 8 | Use workflows in code (Azure AI Projects SDK) | 5 min | [docs/08-use-workflows-in-code.md](docs/08-use-workflows-in-code.md) |
| 9 | Key terms (glossary) | 2 min | [docs/09-key-terms.md](docs/09-key-terms.md) |

### Demo

#### [`demo/sequencial-workflow-sample/`](demo/sequencial-workflow-sample/) — Sequential marketing-copy workflow

A **sequential** workflow that turns a raw product description into polished marketing copy by chaining three agents, each feeding its output to the next via `System.LastMessage`:

```
Start → Marketing-Analyst → Marketing-Copywriter → Marketing-Editor → End
```

| Step | Agent | Does |
| --- | --- | --- |
| 1 | **Marketing-Analyst** | Extracts key features, target audience, and unique selling points from the product description. |
| 2 | **Marketing-Copywriter** | Turns that analysis into a ~150-word marketing copy block. |
| 3 | **Marketing-Editor** | Fixes grammar, tightens clarity, enforces a consistent tone, and returns the final polished copy. |

The demo README walks through building it in the Microsoft Foundry portal step by step (with screenshots): create a project, open the **Workflows** tab, create a **Sequential** workflow, add and configure the three agents, then **Save → Preview → Publish**. Once published, a Node.js script invokes it from code:

```bash
cd demo/sequencial-workflow-sample
npm install
az login
node run_agent.js
```

`run_agent.js` uses the **Azure AI Projects SDK** (`@azure/ai-projects`, `@azure/identity`) to retrieve the workflow by name, create a conversation, send a product description, and print `response.output_text`. Configuration (project endpoint, workflow id) lives in [`demo/sequencial-workflow-sample/.env`](demo/sequencial-workflow-sample/.env).

**Concepts demonstrated:** the Sequential pattern, agent chaining with `System.LastMessage`, `System.ConversationId` for conversation context, publishing a workflow, and invoking it from code.

---

## Quick start

1. Open your project in the **Microsoft Foundry portal**.
2. Go to **Agents → Workflows** and create a new workflow — start from a blank canvas or a predefined pattern (e.g. *Sequential*).
3. Add nodes from the **Add a workflow action** panel: `Invoke agent`, `If/Else`, `Set variable`, `Send message`, `End`.
4. Connect the nodes to define the execution path, then **save** (workflows are not saved automatically).
5. Test in the **chat window** — send an input and watch how it flows through each node.
6. When you're happy, invoke the workflow from code with the **Azure AI Projects SDK** by referencing its name.

See the [docs index](docs/README.md) for the full walkthrough, or jump into [`demo/sequencial-workflow-sample/`](demo/sequencial-workflow-sample/) for a working example.

---

## Related resources

| Resource | Link |
| --- | --- |
| Microsoft Foundry documentation | <https://learn.microsoft.com/azure/ai-foundry/> |
| Azure AI Projects SDK (Python) | <https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme> |
| Power Fx language reference | <https://learn.microsoft.com/power-platform/power-fx/overview> |
| Microsoft Learn — AI agents & workflows training | <https://learn.microsoft.com/training/> |
