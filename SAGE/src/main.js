const input = document.getElementById("commandInput");
const button = document.getElementById("sendButton");

button.addEventListener("click", sendMessage);

input.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
        sendMessage();
    }
});

function sendMessage() {

    const message = input.value.trim();

    if (message === "") {
        return;
    }

    console.log("User said:", message);

    input.value = "";
}