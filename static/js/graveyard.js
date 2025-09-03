const storyLines = [
    "The second fragment awaited in the Dragon Graveyard — the resting place of ancient warriors.",
    "Spirits rose to challenge him, testing his worth.",
    "Their blades clashed with his, their voices demanded justice.",
    "With unyielding determination, Hattori fought not for himself, but for all who were gone.",
    "As he stood victorious, the spirits bowed.",
    "The Fragment of Eternity rested in his hand, glowing like the dawn of a new era."
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
        setTimeout(displayLine, 4000); // Adjust delay as needed
    }
}

displayLine();
