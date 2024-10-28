<script>
    import PuzzleMatrix from './ShowPuzzle.svelte';
    import { fly } from 'svelte/transition'; // Import the fly transition

    export let solutions = [];
    export let currentIndex = 0;
    let isPlaying = false;
    let interval;

    function nextStep() {
        if (currentIndex < solutions.length - 1) {
            currentIndex += 1;
        }
    }

    function previousStep() {
        if (currentIndex > 0) {
            currentIndex -= 1;
        }
    }

    function playSlow() {
        pause()
        isPlaying = true;
        if (currentIndex < solutions.length - 1) {
            interval = setInterval(() => {
                if (currentIndex < solutions.length - 1) {
                    nextStep();
                } else {
                    clearInterval(interval);
                    isPlaying = false;
                }
            }, 1000);
        }
    }

    function playFast() {
        pause()
        isPlaying = true;
        if (currentIndex < solutions.length - 1) {
            interval = setInterval(() => {
                if (currentIndex < solutions.length - 1) {
                    nextStep();
                } else {
                    clearInterval(interval);
                    isPlaying = false;
                }
            }, 500);
        }
    }

    function pause() {
        clearInterval(interval);
        isPlaying = false;
    }

    export function reset() {
        pause();
        currentIndex = 0;
    }

    function convertStringToGrid(str) {
        let flatGrid = str.split('').map(char => (char === '0' ? null : Number(char)));
        return [flatGrid.slice(0, 3), flatGrid.slice(3, 6), flatGrid.slice(6, 9)];
    }
</script>

<div class="solution-area">
    <h2>Solution Steps</h2>
    <div class="solution-display">
        {#if currentIndex > 0}
            <div class="faded-puzzle left-faded" transition:fly={{ x: -50 }}>
                <PuzzleMatrix grid={convertStringToGrid(solutions[currentIndex - 1])} size={25} />
            </div>
        {/if}

        <div class="center-puzzle" in:fly={{ x: 100 }} out:fly={{ x: -100 }}>
            {#if solutions.length > 0}
                <PuzzleMatrix grid={convertStringToGrid(solutions[currentIndex])} />
            {:else}
                <p>No solutions available</p>
            {/if}
        </div>

        {#if currentIndex < solutions.length - 1}
            <div class="faded-puzzle right-faded" transition:fly={{ x: 50 }}>
                <PuzzleMatrix grid={convertStringToGrid(solutions[currentIndex + 1])} size={25} />
            </div>
        {/if}
    </div>
    
    <div class="controls">
        <button on:click={previousStep} disabled={currentIndex === 0} class="arrow-button">&lt;</button>
        <button on:click={nextStep} disabled={currentIndex === solutions.length - 1} class="arrow-button">&gt;</button>
    </div>

    <div class="controls">
        <button on:click={playSlow}>Play Slow</button>
        <button on:click={playFast}>Play Fast</button>
        <button on:click={pause}>Pause</button>
        <button on:click={reset}>Reset</button>
    </div>
</div>
<style>
    .solution-area {
        display: flex;
        flex-direction: column;
        align-items: center;
        background-color: #001100; /* Dark green background */
        width: 100%;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 4px 10px rgba(0, 255, 0, 0.2);
        margin-top: 20px;
        color: #00ff00; /* Bright green text */
        font-family: "Courier New", Courier, monospace;
    }

    h2 {
        margin-bottom: 10px;
        color: #00ff00; /* Bright green heading */
    }

    .solution-display {
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        width: 100%;
    }

    .faded-puzzle {
        width: 80px;
        opacity: 0.5;
        margin: 0 10px;
    }

    .center-puzzle {
        display: flex;
        justify-content: center;
        width: 150px;
        z-index: 1;
    }

    .controls {
        display: flex;
        gap: 10px;
        margin-top: 10px;
    }

    .arrow-button {
        padding: 10px 15px;
        border: none;
        border-radius: 6px;
        background-color: #003300; /* Dark green button */
        color: #00ff00; /* Green text */
        cursor: pointer;
        transition: background-color 0.3s;
    }

    .arrow-button:hover {
        background-color: #006600; /* Lighter green on hover */
    }

    button {
        padding: 10px 15px;
        border: none;
        border-radius: 6px;
        background-color: #003300; /* Dark green button */
        color: #00ff00; /* Green text */
        cursor: pointer;
        transition: background-color 0.3s;
    }

    button:hover {
        background-color: #006600; /* Lighter green on hover */
    }

    button:disabled {
        background-color: #002200; /* Darker green for disabled */
        color: #555; /* Muted color for disabled text */
        cursor: not-allowed;
    }
</style>
