<script>
    export let taskText = "Do something"
    let isStrikeThrough = false

    let hideX = true
    let deleteSelf = false

</script>

<main class:hidden={deleteSelf}>
    <div id="task-n-cross" on:mouseover={() => hideX = false} on:mouseout={() => hideX = true}>
        <div id="content-in-box">
            <p class:strike={isStrikeThrough}>{taskText}</p>
            <input type="checkbox" on:click={() => isStrikeThrough = !isStrikeThrough}>
        </div>
        <button id="transparent-btn" class:hidden={hideX} on:click={() => deleteSelf = true}>
            <img id="x-img" src="./public/x-lg.svg" alt="delete task">
        </button>
    </div>
</main>


<style>
    #content-in-box {
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: var(--task-div-length);
        height: 50px;
        font-size: 40px;
        font-family: Helvetica;
        font-weight: 500;
        border-radius: 5px;
        border: 1px solid #4d4d4d;
        padding: 0.5rem;
        background-color: #242424;
        margin: 0;
        border-radius: 0;
    }

    #content-in-box:hover {
        background-color: #333333;
        transition: background-color 0.3;
    }


    input {
        min-width: 50px;
        max-width: 50px;
        height: 50px;
    }

    .strike {
        text-decoration: line-through;
    }

    #x-img {
        width: 40px;
        height: 40px;
    }

    .hidden {
        display: none;
    }


    #transparent-btn {
        background: none;
        border: none;
        margin: 0;
        padding: 0;
        position: absolute;
        right: -20px;
    }

    #transparent-btn:hover {
        filter: invert(1);
        transition: 0.3s all;
    }

    #task-n-cross {
        display: flex;
        gap: 15px;
        align-items: center;
        position: relative;
    }


</style>