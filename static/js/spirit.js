const storyLines = [
    "The fourth trial tested his soul.",
    "He faced illusions of his fallen family, voices of despair telling him to give up.",
    "His tears fell, but his blade did not waver.",
    "With courage, he shattered the illusions, holding the Fragment of Spirit close as if it were the hands of his loved ones."
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
        setTimeout(displayLine, 3000);
    }
}

if (container && !sessionStorage.getItem('spiritStoryShown')) {
    displayLine();
    sessionStorage.setItem('spiritStoryShown', 'true');
} else {
    console.error('Story container not found or story already shown');
}
