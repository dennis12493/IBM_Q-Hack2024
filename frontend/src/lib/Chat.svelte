<script lang="ts">
    import { onMount } from "svelte";
    import { IconSend2, IconUser } from "@tabler/icons-svelte";
    // import '../services/video-chat';

    type Message = {
        sender: "me" | "other";
        message: string;
    };

    let messages: Message[] = [];

    onMount(() => {
        messages = [
            {
                sender: "other",
                message: "Do you have some questions about the video?",
            },
        ];
    });

    function sendMessage() {
        const input = document.getElementById("message-input") as HTMLInputElement;
        const message: Message = {
            sender: "me",
            message: input.value.trim(),
        };

        if (message) {
            messages = [...messages, message];
            input.value = "";
        }
    }
</script>

<div class="chat-container">
    {#each messages as message}
        <div class="card">
            <div class="card-body">
                {#if message.sender == "me"}
                    <IconUser />
                {/if}
                {message.message}
                {#if message.sender == "other"}
                    <IconUser />
                {/if}
            </div>
        </div>
    {/each}

    <div class="input-container">
        <textarea
            class="form-control"
            id="message-input"
            data-bs-toggle="autosize"
            placeholder="Type something…"
        ></textarea>
        <button on:click={sendMessage} class="btn btn-primary d-flex"><IconSend2 /></button>
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

    .input-container {
        display: flex;
        margin-top: 10px;
    }
</style>
