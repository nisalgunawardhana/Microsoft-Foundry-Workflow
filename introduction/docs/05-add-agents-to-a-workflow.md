# 5. Add agents to a workflow

> Part of the [Introduction to Agent-Driven Workflows](../README.md) module.
> **Previous:** [Create workflows in Microsoft Foundry](04-create-workflows.md) · **Next:** [Apply Power Fx in workflows](06-apply-power-fx.md)

---

Agents are the **core reasoning components** within a Foundry workflow. Adding agents enables AI-driven decision-making, classification, and response generation as part of a larger orchestration. Each agent can be configured with a specific purpose, model, prompt, and set of tools.

## Adding an agent

You add agents by inserting an **Invoke agent** node. This node can:

- reference an **existing agent** from your Foundry project, or
- **create a new agent** directly within the workflow designer.

The Invoke agent editor lets you configure **tools, knowledge bases, memory, and guardrails** for the agent, tailoring its behavior to the workflow's needs. When you invoke an agent, the workflow passes context — user input or previously set variables — to the agent and receives a response that can be used in later steps.

## Reuse and modular design

Agents can be **reused across multiple workflows**, which encourages modular design. For example:

- a single **categorization agent** might be invoked in many workflows to classify incoming requests,
- while different **resolution agents** handle follow-up actions.

This separation of concerns makes workflows easier to maintain and evolve over time.

## Structured output

In addition to natural-language responses, agents can be configured to return **structured output**. By defining a response format such as a **JSON schema**, you ensure agent output follows a predictable shape. Structured outputs are especially useful when agent responses drive control flow — routing logic or variable assignment in later nodes.

- Define an agent's output schema in the **parameters of the Details tab** of the Invoke agent editor (set *Text format* to **JSON Object** or **JSON Schema**).
- Store agent output in a **variable** via the **Action settings** of the Invoke agent node (e.g. *Save agent output message as* `Local.TextOutput`, *Save output json_object/json_schema as* `Local.JsonOutput`).

<p align="center">
  <img src="../images/invoke-agent-settings.svg" alt="Invoke agent node: Action settings for saving output to variables, and Details parameters for choosing a JSON Schema response format" width="85%">
</p>

Once an agent is added, its output can be stored in a variable and referenced throughout the workflow — influencing decisions, triggering conditional branches, or providing input to other agents. By thoughtfully adding and configuring agents, you transform a simple sequence of actions into an **intelligent, adaptive workflow**.

---

**Previous:** [Create workflows in Microsoft Foundry](04-create-workflows.md) · **Next:** [Apply Power Fx in workflows](06-apply-power-fx.md)
