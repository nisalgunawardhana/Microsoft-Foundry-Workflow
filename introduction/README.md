# Introduction to Agent-Driven Workflows in Microsoft Foundry

This module is the conceptual foundation for building, extending, and reasoning about agent-driven systems in Microsoft Foundry. It's split into short, focused documents — read them in order or jump to what you need.

> **New here?** Start with the [main README](../README.md) for a one-page overview of Microsoft Foundry, then read the [short intro](intro.md).

---

## Documents

| # | Document | Time | What it covers |
| --- | --- | --- | --- |
| — | [intro.md](intro.md) | 1 min | A short standalone intro to the module and the support-triage scenario. |
| 1 | [Introduction](docs/01-introduction.md) | 3 min | Why multi-agent workflows, the running scenario, learning objectives. |
| 2 | [What are workflows?](docs/02-what-are-workflows.md) | 3 min | Nodes, execution paths, and why workflows matter. |
| 3 | [Identify workflow patterns](docs/03-identify-workflow-patterns.md) | 3 min | Sequential, human-in-the-loop, and group-chat patterns. |
| 4 | [Create workflows in Microsoft Foundry](docs/04-create-workflows.md) | 5 min | The visual designer and every node type. |
| 5 | [Add agents to a workflow](docs/05-add-agents-to-a-workflow.md) | 5 min | The Invoke agent node, reuse, and structured output. |
| 6 | [Apply Power Fx in workflows](docs/06-apply-power-fx.md) | 5 min | Variables, conditions, loops, and a formula reference table. |
| 7 | [Maintain workflows in Microsoft Foundry](docs/07-maintain-workflows.md) | 5 min | YAML, versioning, notes, and refinement best practices. |
| 8 | [Use workflows in code](docs/08-use-workflows-in-code.md) | 5 min | Invoking workflows with the Azure AI Projects SDK. |
| 9 | [Key terms](docs/09-key-terms.md) | 2 min | Glossary of workflow terminology. |

---

## Learning objectives

After working through these documents, you'll be able to:

- Explain how workflow **nodes, variables, and agent outputs** work together to control execution paths.
- Use **structured agent outputs** and **conditional logic** to route requests to the appropriate workflow steps.
- Implement **loops (For-Each)** to process multiple inputs efficiently within a single workflow.
- Apply **human-in-the-loop** and **escalation** patterns to manage uncertainty and low-confidence agent responses.
- Use **Power Fx expressions** to manipulate data, evaluate conditions, and control flow within workflows.

---

## Folder layout

```
introduction/
├── README.md          ← this index
├── intro.md           ← short standalone intro
├── docs/              ← one document per section
│   ├── 01-introduction.md
│   ├── 02-what-are-workflows.md
│   ├── 03-identify-workflow-patterns.md
│   ├── 04-create-workflows.md
│   ├── 05-add-agents-to-a-workflow.md
│   ├── 06-apply-power-fx.md
│   ├── 07-maintain-workflows.md
│   ├── 08-use-workflows-in-code.md
│   └── 09-key-terms.md
└── images/            ← diagrams referenced by the docs
```

---

**Next unit:** *Exercise — Create an Agent-driven Workflow.*
