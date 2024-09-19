const messageInput = document.getElementById('messageInput');
const sendButton = document.getElementById('sendButton');
const chatMessages = document.getElementById('chatMessages');

sendButton.addEventListener('click', () => {
    const message = messageInput.value;
    if (message.trim() !== '') {
        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: message })
        })
            .then(response => response.json())
            .then(data => {
                chatMessages.innerHTML += `<div class="text-right">You: ${message}</div>`;
                chatMessages.innerHTML += `<div class="text-left">AI: ${data.response}</div>`;
                messageInput.value = '';
            })
            .catch(error => console.error(error));
    }
});