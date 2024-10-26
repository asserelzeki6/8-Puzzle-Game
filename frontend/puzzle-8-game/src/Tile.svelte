<script>
  export let value;
  export let empty;
  export let handleClick;
</script>

<div on:click={() => handleClick(value)} class="tile {empty ? 'empty' : ''}">
  {#if !empty}
    {value}
  {/if}
</div>

<style>
  .tile {
    width: 100px;
    height: 100px;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: lightgray;
    font-size: 24px;
    cursor: pointer;
  }
  .empty {
    background-color: white;
  }
</style>
