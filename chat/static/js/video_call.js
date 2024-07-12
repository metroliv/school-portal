function copyInviteLink() {
    const inviteLink = document.getElementById("invite-link");
    inviteLink.select();
    document.execCommand("copy");
    alert("Invite link copied to clipboard!");
}

function mute(userId) {
    // Logic to mute user
}

function unmute(userId) {
    // Logic to unmute user
}

function remove(userId) {
    // Logic to remove user from call
}
