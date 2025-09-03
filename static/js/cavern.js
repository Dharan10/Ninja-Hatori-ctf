const storyLines = [
    "Hattori's journey began not with a clash of steel, but with a test of perception.",
    "The first fragment lay hidden in the Cavern of Echoes.",
    "Here, the past screamed at him — the cries of friends who perished in flames.",
    "The echoes cut deeper than steel, but Hattori walked on, steady and unbroken.",
    "Each step was a promise.",
    "Each breath, a vow.",
    "When he claimed the Fragment of Echoes, the cavern fell silent, as if honoring his resolve."
];

let currentLine = 0;
const container = document.getElementById('story-container');

function displayLine() {
    if (currentLine < storyLines.length) {
        const p = document.createElement('p');
        p.textContent = storyLines[currentLine];
        p.classList.add('fade-in');
        container.appendChild(p);
        currentLine++;
        setTimeout(displayLine, 4000); // Adjust delay as needed
    }
}

displayLine();
