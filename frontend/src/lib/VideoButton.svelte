<script lang="ts">
    import { selectedVideo, selectedVideoButtonId } from "../general/stores";
    export let title: string, value: number;


    const handleSelect = (event: MouseEvent) => {

        selectedVideo.set(value);
        selectedVideoButtonId.set(value);
    }
</script>

<button on:click={handleSelect} class={$selectedVideoButtonId == value ? "selected" : ""}>{title}</button>

<style>
    button {
        background-color: var(--background);
        border: none;
        outline: none;
        padding: 0.3rem 1rem;

        width: 80%;
        height: 3rem;
        border-radius: 5px;
    }

    .selected{
        background-color: var(--accent);
    }
</style>
