import { DefaultAzureCredential } from "@azure/identity";
import { AIProjectClient } from "@azure/ai-projects";

const endpoint = "<Your Endpoint URL>";
const agentName = "<Your workflow name>"; // Replace with your workflow name

// Create AI Project client
const projectClient = new AIProjectClient(endpoint, new DefaultAzureCredential());

async function main() {
  
   // Retrieve Workflow by name (latest version)
  const retrievedworkflow = await projectClient.agents.get(agentName);
  console.log("Retrieved latest workflow - name:", retrievedworkflow.versions.latest.name, " id:", retrievedworkflow.id);

  // Use the retrieved agent to create a conversation and generate a response
  const openAIClient = projectClient.getOpenAIClient();
  
  // Create conversation with initial user message
  console.log("\nCreating conversation with initial user message...");
  const conversation = await openAIClient.conversations.create({
    items: [{ type: "message", role: "user", content: "Hello" }],
    });
  console.log("\nCreated conversation id: ");
  console.log(conversation.id);
  
  // Generate response using the agent
  console.log("\nGenerating response...");
  const response = await openAIClient.responses.create(
      {
          conversation: conversation.id,
      },
      {
          body: { agent: { name: retrievedworkflow.name, type: "agent_reference" } },
      },
  );
  console.log("\nResponse output: ");
  console.log(response.output_text);
}

main();