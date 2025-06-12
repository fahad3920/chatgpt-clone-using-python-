// Get references to DOM elements
const input = document.querySelector('.input-bar input');
const responseContainer = document.getElementById('response-container');
const toolsIcon = document.querySelector('.tool-icon');
const micIcon = document.querySelector('.mic');
const waveIcon = document.querySelector('.wave');

// Function to append messages to the response container
function appendMessage(message, isUser = false) {
  const msgDiv = document.createElement('div');
  msgDiv.textContent = (isUser ? 'You: ' : 'Bot: ') + message;
  msgDiv.style.marginBottom = '10px';
  msgDiv.style.color = isUser ? '#4f46e5' : '#ccc';
  responseContainer.appendChild(msgDiv);
  responseContainer.scrollTop = responseContainer.scrollHeight;
}

// Handle Enter key press in input field
input.addEventListener('keydown', function(event) {
  if (event.key === 'Enter') {
    const userInput = input.value.trim();
    if (userInput === '') return;
    appendMessage(userInput, true);
    input.value = '';
    // Simulate bot response
    setTimeout(() => {
      appendMessage("Sorry, I'm a static UI clone and cannot respond.");
    }, 500);
  }
});

// Add click handlers for icons
toolsIcon.addEventListener('click', () => {
  alert('Tools functionality is not implemented in this static clone.');
});

micIcon.addEventListener('click', () => {
  alert('Mic functionality is not implemented in this static clone.');
});

waveIcon.addEventListener('click', () => {
  alert('Wave functionality is not implemented in this static clone.');
});
