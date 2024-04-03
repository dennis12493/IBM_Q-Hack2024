<script lang="ts">
    import Header from '../lib/Header.svelte';
    import Navigation from '../lib/Navigation.svelte';
    import Video from '../lib/Video.svelte';
    import Chat from '../lib/Chat.svelte';
</script>

<div class="main">
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
</div>

<style>
    .main {
        display: flex;
        flex-direction: column;
        height: 100%;
        width: 100%;
    }

    .top-level {
        background-color: var(--background);
        display: flex;
        flex-direction: row;
        gap: 1rem;
        height: 100%;
    }

    .nav {
        width: 20%;
    }
    .video {
        width: 40%;
    }
    .chat {
        width: 40%;
    }
</style>
