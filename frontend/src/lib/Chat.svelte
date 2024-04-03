<script lang="ts">
    import { onMount } from "svelte";
    import { askAboutVideo } from '../services/video-helper';
    import IconUser from "./assets/User.svg";
    import IconSend from "./assets/Send.svg";

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
            askAboutVideo("v6tUWk7vC6g", message.message).then((answer ) => { //TODO: get VideoId
                let answerMessage: Message =  {
                    sender: "other",
                    message: answer ? answer : "Sorry, currently I can't help you."
                }
                messages = [ ...messages, answerMessage ]
            })
        }
    }
</script>

<div class="chat-container">
    {#each messages as message}
        <div class="card">
            <div class="card-body">
                {#if message.sender == "me"}
                    <img src={IconUser} alt=""/>
                {/if}
                {message.message}
                {#if message.sender == "other"}
                    <img src={IconUser} alt=""/>
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
        <button on:click={sendMessage} class="btn btn-primary d-flex"><img src={IconSend} alt=""/></button>
    </div>
</div>

<style>
    .chat-container {
        margin: 0;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 4px;
        overflow-y: scroll;
        height: calc(100% - 20px - 5rem);
    }

    .card {
        margin: 10px;
        padding: 10px;
        border-radius: 10px;
        background-color: --var(--highlight);
        border: 2px solid #ccc;
        color: --var(--text);
    }

    .input-container {
        display: flex;
        margin: 10px;
        padding: 10px;
    }

    textarea {
        margin: 10px;
        padding: 10px;
        border-radius: 10px;
        background-color: --var(--highlight);
        border: 2px solid #ccc;
        color: --var(--text);
    }

    img {
        width: 20px;
        height: 20px;
    }
</style>
