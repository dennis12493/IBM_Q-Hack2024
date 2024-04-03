<script lang="ts">
    import VideoButton from "./VideoButton.svelte";

</script>

<div class="wrapper">
    <h1>Lectures</h1>
    <div class="lectures">
        <VideoButton value={0} title={'Bees'}></VideoButton>
        <VideoButton value={1} title={'Trees'}></VideoButton>
        <VideoButton value={2} title={'the danger of Silence'}></VideoButton>
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
        width: calc(100% - 2rem);
        text-align: center;
        background-color: var(--background);
        color: var(--text);
        font-size: 1.7rem;
        padding: 0.5rem 0;
        margin: 0;

        border-radius: 5px;
    }
</style>
