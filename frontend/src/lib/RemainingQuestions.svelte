<script lang="ts">
    import { writable } from "svelte/store";

    const messages = writable<string[]>([]);

    let userInput: string = '';

    const handleInputSubmit = (event: Event) => {
        event.preventDefault();
        messages.set([...$messages, userInput]);
        userInput = "";
    }
</script>

<div>
    <h1>Questions for next Class</h1>
    <div class="messages">

        {#each $messages as message}
            <p>
                {message}
            <p>
            <div class="line"></div>
        {/each}
    </div>
    <form on:submit={handleInputSubmit}>
        <input bind:value={userInput} placeholder="Remaining questions for the teacher..."/>
    </form>
</div>

<style>
    h1{
        margin: 0;
        font-size: 1.4rem;
        color: var(--accent);
    }

    form{
        width: 100%;
    }

    input {
        position: absolute;
        bottom: 2rem;

        width: calc(40% - 1rem);
        padding: 1rem 0rem;
        padding-left: 0.3rem;
        outline: none;
        border: none;
        border-radius: 0 0 5px 5px;
    }

    .messages{
        padding-top: 2rem;
        animation: 0.7s fade ease-in forwards;
    }

    .line{
        width: 100%;
        height: 1px;
        background-color: var(--border);
        margin-top: 0.5rem;
        margin-bottom: 0.5rem;
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
