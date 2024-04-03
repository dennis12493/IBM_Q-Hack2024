<script lang="ts">
    import Header from "./lib/Header.svelte";
    import Navigation from "./lib/Navigation.svelte";
    import Video from "./lib/Video.svelte";
    import Chat from "./lib/Chat.svelte";
</script>

<main>
    <Header />
    <div>
        <Navigation />
        <Video />
        <Chat />
    </div>
</main>

<style>
    main {
        display: flex;
        flex-direction: column;
        background-color: var(--background);
    }

    div {
        background-color: var(--background);
        display: flex;
        flex-direction: row;
    }
</style>
