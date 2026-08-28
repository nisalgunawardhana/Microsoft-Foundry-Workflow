# 7. Maintain workflows in Microsoft Foundry

> Part of the [Introduction to Agent-Driven Workflows](../README.md) module.
> **Previous:** [Apply Power Fx in workflows](06-apply-power-fx.md) · **Next:** [Use workflows in code](08-use-workflows-in-code.md)

---

Building a workflow is just the first step — real-world automation **evolves over time**. Maintaining and refining workflows keeps them reliable, understandable, and adaptable as business needs or AI models change.

## YAML and visual representations

Foundry workflows can be represented in **two synced views**:

| View | Strengths |
| --- | --- |
| **Visual canvas** | Conceptual understanding, tracing execution paths, collaborating with others. |
| **YAML** | Textual representation for advanced configuration, version tracking, and integration with source control. |

Changes in either view are reflected in the other, giving you flexibility while keeping workflows consistent.

## Versioning

Every time a workflow is saved, Foundry automatically creates a **new, immutable version**. Versioning provides a safety net:

- review prior versions,
- compare changes,
- roll back to an earlier workflow if a modification introduces errors.

It also supports collaboration, making it easier to track who changed what and why.

## Adding notes for maintainers

The workflow visualizer lets you attach **notes** to nodes or sections of the workflow. Notes provide context, explain design decisions, or clarify variable usage — helping future maintainers understand the workflow's purpose and logic, reducing errors and accelerating updates.

<p align="center">
  <img src="../images/workflow-note.svg" alt="A note attached to a Triage-Agent node, describing what it categorizes and where its output is stored" width="75%">
</p>

## Best practices for refinement

- Regularly review workflows for **unused or redundant nodes**.
- Ensure **structured agent outputs** are consistently handled.
- **Document** decisions and logic with notes.
- Leverage **version history** to track changes and validate updates.

By combining YAML editing, version control, and thoughtful documentation, you keep workflows robust, maintainable, and ready for enterprise use — letting teams scale automation with confidence.

---

**Previous:** [Apply Power Fx in workflows](06-apply-power-fx.md) · **Next:** [Use workflows in code](08-use-workflows-in-code.md)
