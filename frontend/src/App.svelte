<script lang="ts">
    import Navigation from "./lib/Navigation.svelte";
    import Video from "./lib/Video.svelte";
    import Chat from "./lib/Chat.svelte"
</script>

<main>
    <Navigation/>
    <Video/>
    <Chat/>
</main>

<style>
    main {
        display: flex;
        flex-direction: row;
        height: 100vh;
        background-color: var(--background);
    }
</style>
