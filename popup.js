// Regex patterns for anonymization
const patterns = {
    email: /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b/g,
    phone: /\b\d{3}[-.\s]??\d{3}[-.\s]??\d{4}\b/g,
    name: /\b(John|Doe|Jane)\b/g // Example names; customize as needed
};
  
// Function to anonymize content
function cloakContent(text) {
    return text
        .replace(patterns.email, "[Email]")
        .replace(patterns.phone, "[Phone]")
        .replace(patterns.name, "[Name]");
}
  
// Handle cloak button click
document.getElementById("cloakButton").addEventListener("click", () => {
    const inputText = document.getElementById("inputText").value;
    const cloakedText = cloakContent(inputText);
    document.getElementById("outputText").value = cloakedText;
});
  
// Handle copy button click
document.getElementById("copyButton").addEventListener("click", () => {
    const outputText = document.getElementById("outputText");
    // outputText.select();
    // document.execCommand("copy");
    navigator.clipboard.writeText(outputText.value).then(() => {
        alert("Cloaked content copied to clipboard!");
    }).catch(err => {
        console.error("Failed to copy text: ", err);
    });
});
  