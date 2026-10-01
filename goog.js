const input = document.getElementById('search-input');
const suggestionsBox = document.getElementById('suggestions');

// Inline SVG icon prevents character encoding issues
const searchIcon = `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#9aa0a6" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>`;

window.handleSuggestions = (data) => {
    const suggestions = data[1] || [];
    
    suggestionsBox.innerHTML = suggestions.map(entry => {
        const text = Array.isArray(entry) ? entry[0] : entry;
        const safeText = text.replace(/'/g, "\\'").replace(/"/g, '&quot;');
        
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