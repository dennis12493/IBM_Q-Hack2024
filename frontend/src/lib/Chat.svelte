<script lang="ts">
    import {selectedVideo, urls, timestamp} from "../general/stores";
    import { onMount } from "svelte";
    import { askAboutVideo } from '../services/video-helper';
    import IconUser from "./assets/User.svg";
    import IconSend from "./assets/Send.svg";

    let url: string = "";
    $: $selectedVideo, handleVideoChange();

    function handleVideoChange() {
        url = urls[$selectedVideo];
    }

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

        if (message && message.message !== "") {
            messages = [...messages, message];
            input.value = "";
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
        <div class="card">
            {#if message.sender == "me"}
            <img src={IconUser} alt=""/>
            {/if}
            <div class="card-body">
                {message.message}
            </div>
            {#if message.sender == "other"}
            <img src={IconUser} alt=""/>
            {/if}
        </div>
        {/each}
    </div>
    <div class="input-container">
        <textarea
            class="form-control"
            id="message-input"
            data-bs-toggle="autosize"
            placeholder="Type something…"
        ></textarea>
        <button on:click={sendMessage}><img src={IconSend} alt=""/></button>
    </div>
</div>

<style>
    .card {
        display: flex;
        flex-direction: row;
        width: 100%;
        justify-content: center;
        align-items: center;
    }

    .messages{
        padding-top: 2rem;
        height: calc(100% - 8rem);
        max-height: calc(100% - 12rem);
        overflow-y: scroll;
    }

    .chat-container {
        margin: 0;
        border-radius: 5px;
        height: calc(100%);
        background-color: var(--panel);
    }

    .card-body {
        margin: 10px;
        padding: 10px;
        border-radius: 10px;
        background-color: --var(--highlight);
        border: 2px solid #ccc;
        color: --var(--text);
    }

    .input-container {
        position: absolute;
        bottom: 0;
        display: flex;
        align-items: center;
        justify-content: center;

        width: 38%;
        margin-bottom: 2rem;
    }

    textarea {
        width: 80%;
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
