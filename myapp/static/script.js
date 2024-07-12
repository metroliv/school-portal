document.addEventListener('DOMContentLoaded', function() {
    const sections = {
        dashboard: document.getElementById('dashboard'),
        messages: document.getElementById('messages'),
        assignments: document.getElementById('assignments'),
        profile: document.getElementById('profile')
    };

    const links = {
        dashboard: document.getElementById('dashboard-link'),
        messages: document.getElementById('messages-link'),
        assignments: document.getElementById('assignments-link'),
        profile: document.getElementById('profile-link')
    };

    function showSection(section) {
        Object.values(sections).forEach(s => s.classList.remove('active'));
        section.classList.add('active');
    }

    links.dashboard.addEventListener('click', function(event) {
        event.preventDefault();
        showSection(sections.dashboard);
    });

    links.messages.addEventListener('click', function(event) {
        event.preventDefault();
        showSection(sections.messages);
    });

    links.assignments.addEventListener('click', function(event) {
        event.preventDefault();
        showSection(sections.assignments);
    });

    links.profile.addEventListener('click', function(event) {
        event.preventDefault();
        showSection(sections.profile);
    });

    const sendMessageButton = document.getElementById('send-message');
    const newMessageInput = document.getElementById('new-message');
    const messageList = document.getElementById('message-list');

    sendMessageButton.addEventListener('click', function() {
        const message = newMessageInput.value.trim();
        if (message !== '') {
            const messageElement = document.createElement('div');
            messageElement.textContent = message;
            messageList.appendChild(messageElement);
            newMessageInput.value = '';
            messageList.scrollTop = messageList.scrollHeight;
        }
    });
});
