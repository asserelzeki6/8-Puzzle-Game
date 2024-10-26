<script>
    export let inputString;
    export let goalString;
    export let onInputChange;
    export let onGoalChange;
    export let onSolveClick;
    export let onShuffleClick;
    export let selectedMethod = "bfs";
    export let onMethodChange;
  
    function handleInputChange(event) {
      onInputChange(event.target.value);
    }

    function handleGoalChange(event) {
      onGoalChange(event.target.value);
    }    
  
    function handleMethodChange(event) {
      onMethodChange(event.target.value);
    }

  </script>
  
  <div class="control-card">
    <h2>Puzzle Control Panel</h2>
  
    <div class="input-group">
      <label for="inputString">Enter puzzle order (0 for empty tile):</label>
      <input
        type="text"
        bind:value={inputString}
        on:input={handleInputChange}
        maxlength="9"
        id="inputString"
        placeholder="e.g., 125670834"
      />
    </div>

    <div class="input-group">
      <label for="inputString">Enter goal order (0 for empty tile):</label>
      <input
        type="text"
        bind:value={goalString}
        on:input={handleGoalChange}
        maxlength="9"
        id="inputString"
        placeholder="e.g., 125670834"
      />
    </div>
  <div class="rowed">
    <button class="solve-button" on:click={onSolveClick}>Solve Puzzle</button>
    <button class="solve-button" on:click={onShuffleClick}>Suffle Puzzle</button>
  </div>
  
    <div class="method-select">
      <!-- svelte-ignore a11y-label-has-associated-control -->
      <label>Select Solve Method:</label>
      <div class="radio-options">
        <label><input type="radio" value="bfs" bind:group={selectedMethod} on:change={handleMethodChange}/> BFS</label>
        <label><input type="radio" value="dfs" bind:group={selectedMethod} on:change={handleMethodChange}/> DFS</label>
        <label><input type="radio" value="dls" bind:group={selectedMethod} on:change={handleMethodChange}/> DLS</label>
        <label><input type="radio" value="a-starm" bind:group={selectedMethod} on:change={handleMethodChange}/> A* M</label>
        <label><input type="radio" value="a-stare" bind:group={selectedMethod} on:change={handleMethodChange}/> A* E</label>
      </div>
    </div>
  </div>
  <style>
    /* Main Card */
    .control-card {
      display: flex;
      flex-direction: column;
      padding: 20px;
      border-radius: 12px;
      background-color: #001100; /* Dark green background */
      box-shadow: 0px 4px 10px rgba(0, 255, 0, 0.2);
      width: 300px;
      font-family: "Courier New", Courier, monospace;
      color: #00ff00; /* Bright green text */
    }
  
    h2 {
      margin-bottom: 16px;
      color: #00ff00; /* Green heading */
      font-weight: 600;
      font-size: 1.25rem;
    }
  
    /* Input Group */
    .input-group {
      display: flex;
      flex-direction: column;
      margin-bottom: 16px;
    }
  
    label {
      color: #00ff00; /* Green label */
      font-size: 0.9rem;
      margin-bottom: 4px;
    }
  
    input[type="text"] {
      padding: 8px;
      border: 1px solid #005500; /* Dark green border */
      border-radius: 6px;
      font-size: 1rem;
      background-color: #002200; /* Darker green input background */
      color: #00ff00; /* Green text */
    }
  
    input[type="text"]:focus {
      border-color: #00ff00; /* Bright green focus border */
      outline: none;
      box-shadow: 0 0 0 2px rgba(0, 255, 0, 0.2);
    }
  
    /* Solve Button */
    .solve-button {
      padding: 5px 10px;
      border: none;
      border-radius: 6px;
      background-color: #004d00; /* Dark green button */
      color: #00ff00; /* Bright green text */
      font-size: 1rem;
      font-weight: 600;
      cursor: pointer;
      transition: background-color 0.3s;
    }
  
    .solve-button:hover {
      background-color: #009900; /* Lighter green on hover */
    }
  
    /* Method Select */
    .method-select {
      margin-top: 16px;
    }
  
    .radio-options {
      display: flex;
      flex-direction: row;
      gap: 6px;
    }
    .rowed {
      display: flex;
      flex-direction: row;
      gap: 6px;
    }
  
    .radio-options label {
      display: flex;
      align-items: center;
      font-size: 0.95rem;
      color: #00ff00; /* Green label text */
    }
    .radio-options input[type="radio"] {
      margin-right: 8px;
      accent-color: #00ff00; /* Green radio button */
    }
  </style>
  