// client/static/script.js
const socket = io();

socket.on('message', (msg) => {
    const chatBox = document.getElementById('chat-box');
    const messageElement = document.createElement('div');
    messageElement.textContent = msg;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
});

function sendMessage() {
    const input = document.getElementById('message-input');
    const message = input.value;
    if (message) {
        socket.send(message);
        input.value = '';
    }
}
