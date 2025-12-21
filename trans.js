function convertToHtml() {
    const inputText = document.getElementById('inputText').value;
    // Simple conversion: split by newlines and wrap each paragraph in <p> tags
    const htmlOutput = inputText
        .split('\n\n') // Split by double newlines for paragraphs
        .map(para => `<p>${para.trim()}</p>`)
        .join('\n');
    
    document.getElementById('outputCode').value = htmlOutput;
}

function copyToClipboard() {
    const outputCode = document.getElementById('outputCode');
    outputCode.select();
    outputCode.setSelectionRange(0, 99999); /* For mobile devices */
    navigator.clipboard.writeText(outputCode.value).then(() => {
        alert('HTML code copied to clipboard!');
    }).catch(err => {
        console.error('Could not copy text: ', err);
    });
}
