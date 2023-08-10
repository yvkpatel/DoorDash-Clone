"use strict";


// This file is responsible for chat component 
const form = document.getElementById('chat-form');
const chatMsg = document.querySelector('.chat-messages');


const socket = io();

socket.on('message', (msg) => {
    console.log(msg);
    displayText(msg);
    chatMsg.scrollTop = chatMsg.scrollHeight;

});

form.addEventListener('submit', (e) => {
    // This is to prevent the page from reloading.
    e.preventDefault();

    // This is to grab the text out of the text box.
    const text = e.target.elements.msg.value;
    
    socket.emit('chat', text);

    e.target.elements.msg.value = '';
    e.target.elements.msg.value.focus();
});

let displayText = (text) => {
    const div = document.createElement('div');
    div.classList.add('message');
    div.innerHTML = `<p class="meta"></p>
    <p class="text">
        ${text}
    </p>`; 
    document.querySelector('.chat-messages').appendChild(div);
};