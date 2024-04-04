<script lang="ts">
    import VideoButton from "./VideoButton.svelte";

</script>

<div class="wrapper">
    <h1>Lectures</h1>
    <div class="lectures">
        <VideoButton date="21.03.2024" value={0} title={'Bees'}></VideoButton>
        <VideoButton date="24.03.2024" value={1} title={'Trees'}></VideoButton>
        <VideoButton date="01.04.2024" value={2} title={'Wölfe'}></VideoButton>
    </div>
</div>

<style>
    .wrapper {
        background-color: var(--panel);
        width: 100%;
        height: 100%;

        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .lectures{
        padding-top: 1rem;
        width: 100%;

        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 0.5rem;
    }
    h1 {
        margin: 0rem 1rem;
        width: 100%;
        text-align: center;
        background-color: var(--background);
        color: var(--text);
        font-size: 1.7rem;
        padding: 1.5rem 0;
        color: var(--accent);
    }
</style>
