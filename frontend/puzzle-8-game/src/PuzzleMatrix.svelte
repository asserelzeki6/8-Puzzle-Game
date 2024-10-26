<script>
    export let grid;
    export let updateInput;
  
    function handleTileClick(value) {
      if (value === null) return;
      const emptyPos = findEmpty();
      const tilePos = findTile(value);
  
      if (canMove(tilePos, emptyPos)) {
        moveTile(tilePos, emptyPos);
        updateInputFromGrid();
      }
    }
  
    function findEmpty() {
      for (let row = 0; row < grid.length; row++) {
        for (let col = 0; col < grid[row].length; col++) {
          if (grid[row][col] === null) {
            return { row, col };
          }
        }
      }
    }
  
    function findTile(value) {
      for (let row = 0; row < grid.length; row++) {
        for (let col = 0; col < grid[row].length; col++) {
          if (grid[row][col] === value) {
            return { row, col };
          }
        }
      }
    }
  
    function canMove(tilePos, emptyPos) {
      const rowDiff = Math.abs(tilePos.row - emptyPos.row);
      const colDiff = Math.abs(tilePos.col - emptyPos.col);
      return (rowDiff === 1 && colDiff === 0) || (rowDiff === 0 && colDiff === 1);
    }
  
    function moveTile(tilePos, emptyPos) {
      [grid[emptyPos.row][emptyPos.col], grid[tilePos.row][tilePos.col]] = 
      [grid[tilePos.row][tilePos.col], grid[emptyPos.row][emptyPos.col]];
    }
  
    function updateInputFromGrid() {
      let flatGrid = grid.flat().map(tile => (tile === null ? '0' : tile)).join('');
      updateInput(flatGrid);
    }
  </script>
  
  <div class="grid">
    {#each grid as row}
      {#each row as tile}
        <div 
          on:click={() => handleTileClick(tile)} 
          class="tile {tile === null ? 'empty' : ''}"
        >
          {#if tile !== null}
            {tile}
          {/if}
        </div>
      {/each}
    {/each}
  </div>
  <style>
    .grid {
        display: grid;
        grid-template-columns: repeat(3, 80px);
        gap: 8px;
        padding: 15px;
        border-radius: 12px;
        background-color: #001100; /* Dark green background */
        box-shadow: 0px 4px 10px rgba(0, 255, 0, 0.2);
        font-family: "Courier New", Courier, monospace;
    }

    .tile {
        width: 80px;
        height: 80px;
        display: flex;
        align-items: center;
        justify-content: center;
        background-color: #002200; /* Darker green tile background */
        font-size: 24px;
        font-weight: bold;
        color: #00ff00; /* Bright green text */
        border-radius: 6px;
        box-shadow: 0px 2px 5px rgba(0, 255, 0, 0.3);
        cursor: pointer;
        transition: background-color 0.3s;
    }

    .tile:hover:not(.empty) {
        background-color: #006600; /* Lighter green on hover */
        color: #00ff00;
    }

    .empty {
        background-color: #001100; /* Dark green for empty tile */
        cursor: default;
    }
</style>
