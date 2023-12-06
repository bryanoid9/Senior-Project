document.addEventListener('DOMContentLoaded', function() {
    // Adding event listener only after DOM has fully loaded
    document.getElementById('send-btn').addEventListener('click', function() {
        let userInput = document.getElementById('user-input').value;
        sendToChatGPT(userInput);
    });
});

function sendToChatGPT(question) {
    const url = '/ask'; // Endpoint of your Flask server

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ question: question })
    })
    .then(response => response.json())
    .then(data => {
        appendMessage(`You: ${question}`);
        appendMessage(`GPT: ${data}`);
    })
    .catch(error => console.error('Error:', error));
}

function appendMessage(message) {
    let chatOutput = document.getElementById('chat-output');
    let newMessage = document.createElement('div');
    newMessage.textContent = message;
    chatOutput.appendChild(newMessage);
}
