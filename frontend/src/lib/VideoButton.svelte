<script lang="ts">
    import { selectedVideo, selectedVideoButtonId } from "../general/stores";
    export let title: string, value: number, date: string;


    const handleSelect = (event: MouseEvent) => {

        selectedVideo.set(value);
        selectedVideoButtonId.set(value);
    }
</script>

<button on:click={handleSelect} class={$selectedVideoButtonId == value ? "selected" : ""}>
    <p class="title">{title}</p>
    <p class="date">{date}</p>
</button>

<style>
    button {
        opacity: 0;
        background-color: var(--background);
        border: none;
        outline: none;
        padding: 0.3rem 1rem;

        width: 95%;
        height: 3rem;
        border-radius: 5px;

        display: flex;
        justify-content: space-between;
        align-items: center;

        animation: fade 0.7s ease-in forwards;
    }

    .selected{
        background-color: var(--accent);

        color: var(--background);
    }

    .selected p {
        color: var(--background);
    }

    .title{
        font-size: 1.3rem;
        font-weight: 500;
    }

    .date{
        color: var(--border);
    }

    @keyframes fade {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }
</style>
