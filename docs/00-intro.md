# 0. Intro

> Part of the [Microsoft Foundry Workflows docs](README.md).
> **Next:** [1. Introduction](01-introduction.md)

---

Modern AI solutions often rely on multiple agents working together to analyze inputs, make decisions, and take action. In **Microsoft Foundry**, agent workflows orchestrate these interactions using a combination of agents, control flow, and runtime safeguards — designed and tested in a visual builder without writing extensive code.

These docs use one running scenario: a developer automating **customer support** at a growing SaaS company, where tickets range from billing disputes to API errors to simple how-to questions. Manual review doesn't scale; full automation isn't always safe. Workflows bridge the gap by combining multiple AI agents, conditional logic, loops, and human-in-the-loop escalation so requests are triaged efficiently and at scale — while keeping reliability and control.

By the end you'll be able to explain how nodes, variables, and agent outputs control execution paths; route requests with structured outputs and conditional logic; process many inputs with For-Each loops; apply human-in-the-loop and escalation patterns; and use Power Fx expressions to manipulate data and control flow.

A companion demo lives in [`../demos/`](../demos/) — a runnable triage workflow you can import into Foundry and invoke from code.

---

**Next:** [1. Introduction](01-introduction.md)
