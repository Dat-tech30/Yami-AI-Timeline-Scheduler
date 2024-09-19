const socket = io();
const messageInput = document.getElementById("messageInput");
const sendButton = document.getElementById("sendButton");
const
    chatMessages = document.getElementById("chatMessages");

sendButton.addEventListener("click", () => {
    const message = messageInput.value;
    if (message.trim()
        !== "") {
        socket.emit("chat", { message });
        messageInput.value = "";
    }
});

socket.on("chat response", (data) => {
    chatMessages.innerHTML += `<div class="text-right">You: ${data.message}</div>`;
    chatMessages.innerHTML += `<div class="text-left">AI: ${data.response}</div>`;
});