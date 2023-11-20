import { config } from "dotenv"
config()

import { Configuration, OpenAIApi } from "openai"
import readline from "readline"

const openAi = new OpenAIApi(
  new Configuration({
    apiKey: process.env.OPEN_AI_API_KEY,
  })
)

const userInterface = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

userInterface.prompt()
userInterface.on("line", async input => {
  const response = await openAi.createChatCompletion({
    model: "gpt-3.5-turbo",
    messages: [{ role: "user", content: input }],
  })
  console.log(response.data.choices[0].message.content)
  userInterface.prompt()
})

document.getElementById('send-btn').addEventListener('click', async function() {
    const messageInput = document.getElementById('shared-input');
    const userInput = messageInput.value;
    const chatBox = document.getElementById('chat-box');

    if (userInput.trim() !== '') {
        // Add the user message to the chat interface
        addMessageToChat('You', userInput, chatBox);

        // Clear the input field
        messageInput.value = '';

        // Send the message to the server and receive a response
        try {
            const response = await fetch('/message', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ prompt: userInput })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();

            // Add the AI's reply to the chat interface
            addMessageToChat('Nutribot', data.message, chatBox);
        } catch (error) {
            console.error('Error fetching response:', error);
        }
    }
});

function addMessageToChat(sender, message, chatBox) {
    const newMessage = document.createElement('div');
    newMessage.innerHTML = `<strong>${sender}:</strong> ${message}`;
    chatBox.appendChild(newMessage);
    chatBox.scrollTop = chatBox.scrollHeight;
}
