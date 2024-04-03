<script lang="ts">
    import Header from "./lib/Header.svelte";
    import Navigation from "./lib/Navigation.svelte";
    import Video from "./lib/Video.svelte";
    import Chat from "./lib/Chat.svelte";
</script>

<main>
    <Header />
    <div class="top-level">
        <div class="nav">
            <Navigation />
        </div>
        <div class="video">
            <Video />
        </div>
        <div class="chat">
            <Chat />
        </div>
    </div>
</main>

<style>
    main {
        display: flex;
        flex-direction: column;
        background-color: var(--background);
        height: 100%;
        width: 100%;
    }

    .top-level {
        background-color: var(--background);
        display: flex;
        flex-direction: row;
        gap: 1rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .nav {
        width: 20%;
    }
    .video {
        width: 60%;
    }
    .chat {
        width: 20%;
    }
</style>
