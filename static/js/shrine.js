const storyLines = [
    "Hattori’s third trial was not of blades, but of wisdom.",
    "In the ruins of an abandoned shrine, he uncovered secrets buried beneath deception.",
    "His patience and sharp mind earned him the Dragon Fragment of Light.",
    "A faint glimmer of hope returned to his heart."
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
        setTimeout(displayLine, 3000); // Adjust delay as needed
    }
}

if (container && !sessionStorage.getItem('shrineStoryShown')) {
    displayLine();
    sessionStorage.setItem('shrineStoryShown', 'true');
} else {
    console.error('Story container not found or story already shown');
}
