function convertToHtml() {
    const inputText = document.getElementById('inputText').value;
    // Simple conversion: split by newlines and wrap each paragraph in <p> tags
    htmlOutput = "."+inputText.replace(/ /i, ".");
    htmlOutput = htmlOutput.replace(/([aeiqouyh])([aeiqouyh])/g, "$11$2");
    htmlOutput = htmlOutput.replace(/(\.[aeiqouyh])/g, "$11");
    htmlOutput = htmlOutput.replace(/([rtsfjkzxcv][aeiqouyh])/g, "$12");
    htmlOutput = htmlOutput.replace(/21/g, "1");
    htmloutput = htmlOutput = htmlOutput.replace(/^./, "");
  
    document.getElementById('outputCode').value = htmlOutput;
}
