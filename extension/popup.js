// Function to anonymize content
async function cloakContent(text,anonymizationType) {

    let headersList = {
        "Content-Type": "application/json"
    }
    let bodyContent = JSON.stringify({
        "content" : text,
        "type_of_anonymization" : anonymizationType
    });

    let response = await fetch("http://localhost:8000/v1/anonymize", { 
        method: "POST",
        body: bodyContent,
        headers: headersList
    });
       
    let data = await response.json();
    return data;
}
  
// Handle cloak button click
document.getElementById("cloakButton").addEventListener("click", async () => {
    const inputText = document.getElementById("inputText").value;
    const errorMsg = document.getElementById("errorMsg");
    const outputText = document.getElementById("outputText");
    const anonymizationType = document.getElementById("anonymizationType").value;
    let errorMessageContent = "";
    
    console.log("Working on cloaking content...");
    outputText.value = "";
    errorMsg.textContent = "";
    try {
        const cloakedData = await cloakContent(inputText,anonymizationType);
        if (cloakedData === undefined || cloakedData === null) {
            errorMessageContent = "No response from server";
            errorMsg.textContent = errorMessageContent;
            return;
        }
        if('anonymized_text' in cloakedData){
            cloakedText = cloakedData['anonymized_text'];
            outputText.value = cloakedText;
        }
        else if('error' in cloakedData){            
            errorMessageContent = cloakedData['error'];
            errorMsg.textContent = errorMessageContent;
        }
        else {
            errorMessageContent = "Unexpected response format";
            errorMsg.textContent = errorMessageContent;
        }
    } catch (error) {
        errorMessageContent = "Error cloaking text - " + error;
        errorMsg.textContent = errorMessageContent;
    }
});
  
// Handle copy button click
document.getElementById("copyButton").addEventListener("click", () => {
    const outputText = document.getElementById("outputText");
    navigator.clipboard.writeText(outputText.value).then(() => {
        alert("Cloaked content copied to clipboard!");
    }).catch(err => {
        console.error("Failed to copy text: ", err);
    });
});
  