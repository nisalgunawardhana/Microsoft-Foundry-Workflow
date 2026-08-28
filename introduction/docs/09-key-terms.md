# 9. Key terms

> Part of the [Introduction to Agent-Driven Workflows](../README.md) module.
> **Previous:** [Use workflows in code](08-use-workflows-in-code.md)

---

| Term | Meaning |
| --- | --- |
| **Workflow** | A visual, declarative orchestration of connected nodes that defines what happens and when. |
| **Node** | A single step in a workflow — invoke an agent, branch on a condition, set a variable, send a message, or end. |
| **Agent** | A configurable AI reasoning component with its own model, prompt, tools, knowledge, memory, and guardrails. |
| **Invoke agent node** | The node that calls an agent, passing workflow context in and receiving a response out. |
| **Structured output** | Agent output constrained to a predictable shape (JSON object or JSON schema) so later nodes can rely on it. |
| **Variable** | Shared state across nodes. `System.*` variables carry conversation/workflow context; `Local.*` variables hold data created during execution. |
| **Control flow** | Nodes that shape the execution path: If/Else, Go To, For Each. |
| **Power Fx** | The low-code, Excel-like expression language used for data manipulation, conditions, and loops. |
| **Human-in-the-loop** | A pattern where the workflow pauses for user input or approval before continuing. |
| **Escalation** | Routing a low-confidence or ambiguous case to a human or a more capable path. |
| **Group chat workflow** | A dynamic pattern where control shifts between multiple agents based on context. |
| **Versioning** | Foundry's automatic creation of an immutable workflow version on every save. |
| **Azure AI Projects SDK** | The SDK used to invoke Foundry workflows from application code. |

---

**Previous:** [Use workflows in code](08-use-workflows-in-code.md)

**Next unit:** *Exercise — Create an Agent-driven Workflow.*
