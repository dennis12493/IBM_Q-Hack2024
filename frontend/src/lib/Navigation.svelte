<script lang="ts">
    import selectedVideo from "../general/stores";
</script>

<div>
    <h1>Lectures</h1>
    <button on:click={e => {selectedVideo.set(0)}}>All About Bees</button>
    <button on:click={e => {selectedVideo.set(1)}}>Trees for kids</button>
    <button on:click={e => {selectedVideo.set(2)}}>Stanford EE364A Convex Optimization</button>
</div>

<style>
    div {
        background-color: var(--background);
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    button {
        background-color: var(--background);
        color: var(--text);
        padding: 1rem;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 1rem;
        margin: 0.5rem;
        cursor: pointer;
        /* border: */
        border-radius: 1rem;
        border: 1px solid black;
    }
</style>
