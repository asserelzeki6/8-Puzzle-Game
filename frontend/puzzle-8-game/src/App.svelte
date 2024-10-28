<script>
  import { onMount, onDestroy } from 'svelte';
  import PuzzleMatrix from './PuzzleMatrix.svelte';
  import ControlArea from './ControlArea.svelte';
  import SolutionArea from './SolutionArea.svelte';
  import { slide } from 'svelte/transition';

  let inputString = '125670834';
  let goalString="012345678"
  let grid = convertStringToGrid(inputString);
  let selectedMethod = "bfs";
  let solutions = [];
  let currentIndex = 0;
  let showAnalysis = false;
  let analysisData = [];
  let solutionAreaRef;


  function handleInputChange(newInputString) {
    inputString = newInputString;
    if (isValidInput(newInputString)) {
      grid = convertStringToGrid(inputString);
      currentIndex = 0; 
    }
  }

  function handleGoalChange(newGoalString){
    goalString=newGoalString
  }

  function updateInput(newString) {
    inputString = newString;
  }

  function handleShuffle() {
    let shuffledArray;
    do {
      shuffledArray = shuffleArray(inputString.split(''));
    } while (!isSolvable(shuffledArray.join('')));
    
    inputString = shuffledArray.join('');
    grid = convertStringToGrid(inputString);
  }


  // Helper function to shuffle an array
  function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
  }

  // Check if the shuffled string is solvable
  function isSolvable(puzzleString) {
    const puzzleArray = puzzleString.split('').map(Number);
    let inversions = 0;
      
    for (let i = 0; i < puzzleArray.length - 1; i++) {
      for (let j = i + 1; j < puzzleArray.length; j++) {
        if (puzzleArray[i] !== 0 && puzzleArray[j] !== 0 && puzzleArray[i] > puzzleArray[j]) {
          inversions++;
        }
      }
    }

    // For a 3x3 grid, a puzzle is solvable if the number of inversions is even
    return inversions % 2 === 0;
  }

  async function handleSolveClick() {
    // Prepare data to send to the Flask server
    if(!isValidInput(inputString))
    {
      alert('Invalid input! Please enter a valid puzzle order.');
      return
    }
    if(!isValidInput(goalString))
    {
      alert('Invalid Goal! Please enter a valid puzzle order.');
      return
    }
    // if (!isSolvable(inputString))
    // {
    //   alert('Puzzle is unsolvable');
    //   return
    // }
    const data = {
      inputString: inputString,
      goalString: goalString,
      algorithmName: selectedMethod
    };

    const response = await fetch('http://127.0.0.1:5000/start', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });

    if (response.ok) {
      const result = await response.json();
      if(result.status=="success"){
        solutionAreaRef.reset()
        solutions = result.path;
        analysisData = result.info;
      }
      else{
        alert('Failed to find solution.');
      }
    } else {
      console.error('Failed to start algorithm');
    }
  }

  function handleMethodChange(newMethod) {
    selectedMethod = newMethod;
  }

  function isValidInput(str) {
    const requiredSet = new Set('012345678');
    const inputSet = new Set(str.split(''));
    return str.length === 9 && [...inputSet].sort().join('') === [...requiredSet].sort().join('');
  }

  function convertStringToGrid(str) {
    let flatGrid = str.split('').map(char => (char === '0' ? null : Number(char)));
    return [flatGrid.slice(0, 3), flatGrid.slice(3, 6), flatGrid.slice(6, 9)];
  }

  function showAnalysisSection() {
    if (solutions.length > 0) {
      showAnalysis = true;
    }
  }

  function hideAnalysisSection() {
    showAnalysis = false;
  }
</script>

<div class="app-container">
  <h1>8-Puzzle Solver</h1>

  {#if !showAnalysis}
  <div class="content-container1" transition:slide={{ duration: 700 }}>
    <div class="content-container2">
      <ControlArea
        {inputString}
        onInputChange={handleInputChange}
        onSolveClick={handleSolveClick}
        onGoalChange={handleGoalChange}
        {selectedMethod}
        onMethodChange={handleMethodChange}
        onShuffleClick={handleShuffle}
      />
      <div>
        <PuzzleMatrix {grid} {updateInput} />
        <button 
          on:click={showAnalysisSection} 
          class="toggle-button {solutions.length === 0 ? 'disabled' : ''}" 
          disabled={solutions.length === 0}
        >
          Show Analysis
        </button>
      </div>
    </div>

    <SolutionArea bind:this={solutionAreaRef} {solutions} {currentIndex} />
  </div>

  {:else}
    <div class="analysis-area" transition:slide={{ duration: 300 }}>
      <div class="analysis-cards">
        {#each analysisData as card}
          <div class="card" transition:slide={{ duration: 1500 }}>
            <h3>{card.title}</h3>
            <p>{card.value}</p>
          </div>
        {/each}
      </div>
      <button on:click={hideAnalysisSection} class="back-button">
        Back to Puzzle
      </button>
    </div>
  {/if}
</div>

<style>
  /* Main Page Container */
  .app-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    font-family: "Courier New", Courier, monospace;
    background-color: #000; /* Black background */
    color: #00ff00; /* Bright green text */
  }

  h1 {
    color: #00ff00; /* Green heading */
    font-size: 2rem;
    margin-bottom: 20px;
  }

  .content-container1 {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 20px;
    width: 100%;
  }

  .content-container2 {
    display: flex;
    align-items: flex-start;
    gap: 20px;
    margin-top: 20px;
  }

  /* Styles for Analysis Area */
  .analysis-area {
    margin-top: 20px;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .analysis-cards {
    display: flex;
    gap: 20px;
    justify-content: center;
    flex-wrap: wrap;
  }

  .card {
    background-color: #002200; /* Dark green card background */
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 255, 0, 0.2);
    width: 150px;
    text-align: center;
    color: #00ff00;
  }

  .toggle-button,
  .back-button {
    margin-top: 20px;
    padding: 10px 20px;
    border: none;
    border-radius: 6px;
    background-color: #004d00; /* Dark green button */
    color: #00ff00; /* Bright green text */
    cursor: pointer;
    transition: background-color 0.3s;
  }

  .toggle-button:hover,
  .back-button:hover {
    background-color: #009900; /* Lighter green on hover */
  }

  .toggle-button.disabled {
    background-color: #003300; /* Even darker green */
    color: #006600; /* Dark green text */
    cursor: not-allowed;
  }
</style>
