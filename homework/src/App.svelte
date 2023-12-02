
<script>
  import Task from './Task.svelte'

  let newTaskName = ''
  let tasks = []


  function addNewTask() {
    if (!newTaskName.trim())
      return
    tasks = [...tasks, newTaskName]
    newTaskName = ''
  }


</script>

<main>
  <h1>Simple TODO App in Svelte</h1>

  <form id="input-line" on:submit|preventDefault={() => {}}>
    <input maxlength="30" class="task-input" placeholder="Enter your task here..." bind:value={newTaskName}/>
    <button id="add-task-btn" on:click={addNewTask} hidden>Add</button>
  </form>

  <ul id="tasks">
    {#each tasks as task}
      <Task taskText={task}/>
    {/each}
  </ul>
</main>

<style>
  #input-line {
    display: flex;
    gap: 10px
  }

  .task-input {
    display: inline-block;
    width: var(--task-div-length);
    height: 50px;
    font-size: 40px;
    font-family: Helvetica;
    font-weight: 500;
    border: 1px solid #4d4d4d;
    padding: 0.5rem;
    background-color: #242424;
  }

  #add-task-btn {
    display: inline-block;
    height: 65px;
    width: 100px;
    border-radius: 3px;
    display: none;
  }

  #tasks {
    gap:0;
    margin:0;
    padding:0;
  }



</style>
