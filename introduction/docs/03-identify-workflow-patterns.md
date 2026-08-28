# 3. Identify workflow patterns

> Part of the [Introduction to Agent-Driven Workflows](../README.md) module.
> **Previous:** [What are workflows?](02-what-are-workflows.md) · **Next:** [Create workflows in Microsoft Foundry](04-create-workflows.md)

---

When building agent-driven solutions, the **structure** of your workflow matters as much as the agents themselves. Different problems require different orchestration approaches, depending on how decisions are made, how data flows, and whether human input is required. Foundry provides several predefined workflow patterns.

| Pattern | How it works | Best for | Trade-off |
| --- | --- | --- | --- |
| **Sequential** | A fixed, step-by-step path. Each node executes in order and passes its output to the next step. | Pipelines and multi-stage processes — validate input, enrich data, generate a final response. A good starting point while learning. | Predictable and easy to reason about, but not adaptive. |
| **Human-in-the-loop** | Introduces pauses where user input or approval is required before the workflow continues. The workflow asks a question, waits for a response, then resumes based on that input. | Approvals, confirmations, or situations where missing context must be supplied by a person. | Adds oversight at the cost of latency / a required human. |
| **Group chat** | Dynamic orchestration across multiple agents. Control shifts between agents based on context, rules, or intermediate results rather than following a fixed path. | Scenarios where specialized agents collaborate on complex requests — customer support, multi-domain question answering. | Flexible and powerful, but harder to predict and debug. |

Each pattern provides a foundation for structuring agent interactions, managing control flow, and incorporating human input as needed. Recognize these patterns and choose an orchestration approach that fits your scenario **before** you begin designing.

---

**Previous:** [What are workflows?](02-what-are-workflows.md) · **Next:** [Create workflows in Microsoft Foundry](04-create-workflows.md)
