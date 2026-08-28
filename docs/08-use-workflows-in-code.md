# 8. Use workflows in code

> Part of the [Microsoft Foundry Workflows docs](README.md).
> **Previous:** [Maintain workflows in Microsoft Foundry](07-maintain-workflows.md) · **Next:** [Key terms](09-key-terms.md)

---

After designing and testing a workflow in the visual designer, you can integrate it into your applications using the **Azure AI Projects SDK** — embedding workflow-driven automation into web apps, APIs, backend services, and other software.

Workflows are created in the Foundry portal, which generates the underlying **YAML definition**. Once saved in your project, you can invoke a workflow programmatically by referencing its **name**, or download its YAML and include it in your codebase.

## Invoke a workflow

Before running a workflow, establish a connection to your Foundry project using `AIProjectClient`. This client handles authentication and provides access to the OpenAI-compatible API for executing conversations and invoking workflows.

```python
# Reference a workflow created in the Foundry portal
workflow_name = "support-triage-workflow"

# Create a conversation context for the workflow
conversation = openai_client.conversations.create()

# Execute the workflow, passing input to drive the workflow logic
stream = openai_client.responses.create(
    conversation=conversation.id,
    extra_body={"agent": {"name": workflow_name, "type": "agent_reference"}},
    input="Users can't reset their password from the mobile app.",
    stream=True,
)
```

The `input` parameter passes a prompt or message to the workflow, which uses it to drive its logic. Depending on your design, this input might be:

- a **user question** that agents analyze and respond to,
- a **support ticket description** for classification and routing,
- a **data payload** that triggers processing logic,
- an **empty string** that simply starts the workflow without specific input.

## Process workflow events

When streaming is enabled, your application receives events as the workflow executes — for real-time progress, capturing agent outputs, and responding to workflow actions.

```python
for event in stream:
    if event.type == "response.completed":
        print("Workflow completed:")
        for message in event.response.output:
            if message.content:
                for content_item in message.content:
                    if content_item.type == 'output_text':
                        print(content_item.text)
    if (event.type == "response.output_item.done") and event.item.type == ItemType.WORKFLOW_ACTION:
        print(f"Action '{event.item.action_id}' completed with status: {event.item.status}")
```

| Event type | Description |
| --- | --- |
| `response.completed` | The workflow finished executing and returned a final response. |
| `response.output_item.done` | An individual output item (such as a workflow action) completed. |

By monitoring these events you can see the workflow progress in real time, or trigger external actions based on workflow state. Alternatively, wait for the entire workflow to complete and process the final response **without** streaming.

For workflows that include **human-in-the-loop** patterns, your application may need to handle pauses where the workflow waits for user input. Send additional messages to the conversation to provide the requested input and **resume** execution.

## Benefits of code integration

| Scenario | Benefit |
| --- | --- |
| **Web applications** | Embed AI-driven workflows directly in user-facing apps. |
| **APIs and microservices** | Expose workflow capabilities through REST endpoints. |
| **Batch processing** | Invoke workflows programmatically for bulk operations. |
| **Testing and validation** | Automate workflow testing as part of CI/CD pipelines. |
| **Custom interfaces** | Build specialized UIs tailored to specific workflow use cases. |

By combining the visual design experience of the Foundry portal with the flexibility of code integration, you can create powerful AI-driven solutions that fit seamlessly into your existing software architecture.

---

**Previous:** [Maintain workflows in Microsoft Foundry](07-maintain-workflows.md) · **Next:** [Key terms](09-key-terms.md)
