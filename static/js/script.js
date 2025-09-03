const storyLines = [
    "The world once trembled beneath the shadow of a ruthless conqueror... Ryukazen, the Warlord of Shadows. His ambition knew no bounds. He swept through nations like a storm, leaving behind only ashes, silence, and despair.",
    "In his conquest, he destroyed everything Hattori held dear. His village burned to dust. His comrades cut down. His bloodline erased. Hattori was left with nothing but pain... nothing but the fire of vengeance burning in his heart.",
    "Desperate to protect what little remained of the world, Hattori sought a power that could rival the darkness of Ryukazen. It was then he learned of the Secret Scroll of Sogen — a scroll said to hold the knowledge of ultimate strength, hidden away within the Dragon Temple.",
    "But the temple cannot be entered by mortal will alone. The gates are sealed by the Dragon Seal Key — an artifact forged long ago by the ancient master craftsman, Koen. And only when the Six Dragon Fragments are gathered can Koen restore the seal and craft the key anew.",
    "And so, Hattori begins his journey. Each fragment hidden in places filled with danger, sacrifice, and trials of spirit. To fail would mean eternal darkness. To succeed would mean a chance to save the world... and honor the memory of all he lost."
];

let currentLine = 0;
const container = document.getElementById('story-container');
const button = document.getElementById('begin-button');

function displayLine() {
    if (currentLine < storyLines.length) {
        const p = document.createElement('p');
        p.textContent = storyLines[currentLine];
        p.classList.add('fade-in');
        container.appendChild(p);
        currentLine++;
        setTimeout(displayLine, 3000); // Reduced to 3s per line for faster pacing
    } else {
        button.style.display = 'block';
    }
}

if (container && button) {
    button.style.display = 'none'; // Ensure hidden initially
    displayLine();
    button.addEventListener('click', () => {
        window.location.href = '/map';
    });
} else {
    console.error('Story container or button not found');
}
