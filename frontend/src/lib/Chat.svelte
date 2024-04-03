<script lang="ts">
    import { onMount } from 'svelte';
    import { IconSend2, IconUser } from '@tabler/icons-svelte';

    type Message = {
        sender: string;
        message: string;
    };

    let messages: string[] = [];

    onMount(() => {
        messages = ['Do you have some questions about the video?'];
    });

    function sendMessage() {
        const input = document.getElementById('message-input') as HTMLInputElement;
        const message = input.value.trim();

        if (message) {
            messages = [...messages, message];
            input.value = '';
        }
    }
</script>

<div class="chat-container">
    {#each messages as message}
        <div class="message"><IconUser/> {message}</div>
    {/each}

    <div class="input-container">
        <input id="message-input" type="text" placeholder="Type your message..." />
        <button on:click={sendMessage}><IconSend2/></button>
    </div>
</div>

<style>
    .chat-container {
        max-width: 500px;
        margin: 0 auto;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 4px;
    }

    .message {
        margin: 5px;
        border: 1px;
        border-radius: 6px;
    }

    .input-container {
        display: flex;
        margin-top: 10px;
    }

    .input-container input {
        flex: 1;
        padding: 8px;
        border: 1px solid #ccc;
        border-radius: 4px;
    }

    .input-container button {
        margin-left: 10px;
        padding: 8px 12px;
        background-color: #007bff;
        color: #fff;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }
</style>
