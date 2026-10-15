const input = document.getElementById('search-input');
const suggestionsBox = document.getElementById('suggestions');
// const suggestions_back = document.getElementById('suggestions_back');


const searchIcon = `<img src="searchicon.png" width="20" height="20" alt="icon">`;
// const searchIcon = `<span><span>`;
// suggestions_back.style.visibility = 'hidden';      // Hide


window.handleSuggestions = (data) => {
    const suggestions = data[1] || [];
    
    suggestionsBox.innerHTML = suggestions.map(entry => {
        const text = Array.isArray(entry) ? entry[0] : entry;
        const safeText = text.replace(/'/g, "\\'").replace(/"/g, '&quot;');
        
        // suggestions_back.style.visibility = 'visible';     // Show
        
        return `
            <div class="suggestion-item" onclick="selectSuggestion('${safeText}')">
                ${searchIcon}
                <span>${text}</span>
            </div>
        `;
    }).join('');
};

function selectSuggestion(text) {
    input.value = text;
    suggestionsBox.innerHTML = '';
    document.querySelector('.google-search').submit();
}

input.addEventListener('input', () => {
    const query = input.value.trim();
    if ((input.value.length) < 1) {
            suggestions_back.style.visibility = 'hidden';      // Hide
        }
    if (!query) {
        suggestionsBox.innerHTML = '';
        return;
    }

    const oldScript = document.getElementById('jsonp-script');
    if (oldScript) oldScript.remove();

    const script = document.createElement('script');
    script.id = 'jsonp-script';
    script.src = `https://suggestqueries.google.com/complete/search?client=chrome&q=${encodeURIComponent(query)}&callback=handleSuggestions`;
    document.body.appendChild(script);
});