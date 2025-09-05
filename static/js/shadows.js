const storyLines = [
    "The fifth fragment was guarded by shadows themselves.",
    "Hattori was ambushed, his wounds ran deep, and the pain of loss returned to his heart.",
    "Yet, through sheer will, he struck down the darkness and held the Fragment of Shadows in trembling hands.",
    "He whispered to the spirits of his lost home — ‘I will not fail again.’"
];

let currentLine = 0;
const container = document.getElementById('story-container');

function displayLine() {
    if (currentLine < storyLines.length) {
        const p = document.createElement('p');
        p.textContent = '"' + storyLines[currentLine] + '"';
        p.classList.add('fade-in');
        container.appendChild(p);
        currentLine++;
        setTimeout(displayLine, 1500); // Adjust delay as needed
    }
}

// Only show story once per session
if (!localStorage.getItem('shadowsStoryShown')) {
    displayLine();
    localStorage.setItem('shadowsStoryShown', 'true');
}
