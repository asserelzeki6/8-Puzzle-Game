<script>
    export let grid = []; // The grid passed as a prop
    export let size = 50; // New prop for size
</script>

<div class="puzzle-matrix" style="font-size: {size / 30}rem;"> <!-- Adjust font size based on size prop -->
    {#each grid as row}
        <div class="puzzle-row">
            {#each row as cell}
                <div class="puzzle-cell" style="width: {size}px; height: {size}px;">
                    {#if cell !== null}
                        {cell}
                    {/if}
                </div>
            {/each}
        </div>
    {/each}
</div>
<style>
    .puzzle-matrix {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        background: none; 
        border: none;
        font-family: "Courier New", Courier, monospace;
    }

    .puzzle-row {
        display: flex;
    }

    .puzzle-cell {
        display: flex;
        align-items: center;
        justify-content: center;
        border: 2px solid #00ff00; /* Bright green border */
        margin: 4px;
        background-color: #001100; /* Dark green background */
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 255, 0, 0.2); /* Subtle green shadow */
        transition: background-color 0.3s, transform 0.3s;
        font-size: 1.5rem;
        color: #00ff00; /* Bright green text */
    }

    .puzzle-cell:hover {
        background-color: #003300; /* Darker green for hover effect */
        transform: scale(1.05); /* Slightly enlarges tile on hover */
        box-shadow: 0 4px 10px rgba(0, 255, 0, 0.4); /* Enhanced green shadow on hover */
    }
</style>
