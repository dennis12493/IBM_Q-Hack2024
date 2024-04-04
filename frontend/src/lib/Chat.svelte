<script lang="ts">
    import {selectedVideo, urls, timestamp} from "../general/stores";
    import { onMount } from "svelte";
    import { askAboutVideo } from '../services/video-helper';
    import Message from "./Message.svelte";

    let url: string = "";
    let userInput: string = "";
    $: $selectedVideo, handleVideoChange();

    function handleVideoChange() {
        url = urls[$selectedVideo];
        resetMessages();
    }

    type Message = {
        sender: "me" | "other";
        message: string;
    };

    let messages: Message[] = [];

    onMount(() => resetMessages);

    function resetMessages() {
        messages = [
            {
                sender: "other",
                message: "I'm happy to assist you. Feel free to ask any Question you want!",
            },
        ];
    }

    function sendMessage(event: Event){
        event.preventDefault();
        const message: Message = {
            sender: "me",
            message: userInput.trim(),
        };

        if (message && message.message !== "") {
            messages = [...messages, message];
            console.log(message.message);
            userInput = "";
            console.log(message.message);
            askAboutVideo(url, message.message).then((value ) => {
                timestamp.set(value.timestamp);
                let answerMessage: Message =  {
                    sender: "other",
                    message: value.answer
                }
                messages = [ ...messages, answerMessage ]
            })
        }
    }
</script>

<div class="chat-container">
    <div class="messages">
        {#each messages as message}
            <Message sender={message.sender} message={message.message} />
        {/each}
    </div>
    <div class="input-container">
        <form on:submit={sendMessage}>
            <input
                bind:value={userInput}
                class="form-control"
                id="message-input"
                placeholder="Ask me anything..."
                type="text"
            >
        </form>
    </div>
</div>
<!-- <button on:click={sendMessage}><img src={IconSend} alt=""/></button> -->

<style>
    .messages{
        padding-top: 2rem;
        height: 100%;
        max-height: 100%;
        overflow-y: scroll;
        background-color: var(--panel);

        border-radius: 5px 5px 0 0;
    }

    .chat-container {
        margin: 1rem 0.5rem;
        border-radius: 5px;
        height: 85%;
    }

    .input-container {
        position: absolute;
        bottom: 0;
        display: flex;
        align-items: center;
        justify-content: center;

        width: 38%;
        margin-bottom: 3rem;
    }

    form{
        width: 100%;
    }

    input {
        width: 100%;
        max-width: calc(100% - 0.6rem);
        padding: 1rem 0.3rem;

        outline: none;
        border: none;
        border-radius: 0 0 5px 5px;
    }

    img {
        width: 20px;
        height: 20px;
    }
</style>
