"""Invoke the saved 'triage-workflow' in Microsoft Foundry and stream its events.

Prereqs:
    pip install azure-ai-projects azure-identity openai
    export AZURE_AI_PROJECT_ENDPOINT="https://<project>.services.ai.azure.com/api/projects/<project>"
    export WORKFLOW_NAME="triage-workflow"   # optional; this is the default
    az login                                  # DefaultAzureCredential

Usage:
    python run_workflow.py "Users can't reset their password from the mobile app."
    python run_workflow.py                    # uses a built-in sample ticket

See ../../docs/08-use-workflows-in-code.md for the concepts.
"""

from __future__ import annotations

import os
import sys

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

DEFAULT_INPUT = "I was charged twice and my API isn't working — can you help?"


def main() -> None:
    endpoint = os.environ.get("AZURE_AI_PROJECT_ENDPOINT")
    if not endpoint:
        sys.exit("Set AZURE_AI_PROJECT_ENDPOINT to your Foundry project endpoint.")

    workflow_name = os.environ.get("WORKFLOW_NAME", "triage-workflow")
    user_input = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_INPUT

    project = AIProjectClient(endpoint=endpoint, credential=DefaultAzureCredential())

    # OpenAI-compatible client for conversations + responses.
    openai_client = project.get_openai_client()

    # A conversation gives the workflow a context to run in (and to resume, for
    # human-in-the-loop pauses).
    conversation = openai_client.conversations.create()

    print(f"Workflow : {workflow_name}")
    print(f"Input    : {user_input}\n")

    stream = openai_client.responses.create(
        conversation=conversation.id,
        extra_body={"agent": {"name": workflow_name, "type": "agent_reference"}},
        input=user_input,
        stream=True,
    )

    for event in stream:
        etype = getattr(event, "type", "")

        if etype == "response.completed":
            print("\n--- workflow completed ---")
            for message in event.response.output:
                for content_item in getattr(message, "content", None) or []:
                    if getattr(content_item, "type", "") == "output_text":
                        print(content_item.text)

        elif etype == "response.output_item.done":
            item = getattr(event, "item", None)
            item_type = getattr(item, "type", "")
            # ItemType.WORKFLOW_ACTION == "workflow_action"
            if item_type == "workflow_action":
                print(f"[action] {item.action_id}: {item.status}")


if __name__ == "__main__":
    main()
