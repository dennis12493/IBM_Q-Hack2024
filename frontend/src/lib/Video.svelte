<script lang="ts">
    let url: string = "";
</script>

<div>
    <iframe
        src={url}
        height="400rem"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen
    ></iframe>
</div>

<style>
    div {
        background-color: var(--background);
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
</style>
