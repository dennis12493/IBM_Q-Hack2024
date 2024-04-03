<script lang="ts">
    let url: string = "";
    function changeIframe(event: Event) {
        url = (event.target as HTMLInputElement).value;
    }
</script>

<div>
    <div>
        <input on:change={changeIframe} />
        <iframe
            width="560"
            height="315"
            src={url}
            title="YouTube video player"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            allowfullscreen
        ></iframe>
    </div>
</div>

<style>
    div {
        background-color: var(--background);
    }
</style>
