<script lang="ts">
    import IconUser from "./assets/User.svg";
    import IconSend from "./assets/Send.svg";
    export let sender: string, message: string;
</script>

<div class="message-container">
    <div class="message">
        {#if sender == "me"}
        <img src={IconUser} alt=""/>
        {/if}

        <div class="message-text">
            {message}
        </div>

        {#if sender == "other"}
        <img src={IconUser} alt=""/>
        {/if}
    </div>
    <div class="line"></div>
</div>

<style>
    .message-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 0.4rem;

        width: 100%;
    }

    .message {
        display: flex;
        align-items: center;
        justify-content: space-between;
        width: 80%;
        gap: 1rem;
    }

    .message-text{
        font-size: 1.2rem;
        width: 100%;
    }

    .line {
        background-color: var(--background);
        width: 95%;
        height: 3px;
        margin-bottom: 0.5rem;
    }

    img {
        width: 1.7rem;
        height: 1.7rem;

        background-color: var(--border);
        filter: invert(0.9);
        padding: 0.6rem;
        border-radius: 100%;
    }
</style>
