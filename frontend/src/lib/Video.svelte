<script lang="ts">
    import selectedVideo from "../general/stores";
    let url: string = "";
    let urls: string[] = [
        "https://www.youtube.com/embed/v6tUWk7vC6g",
        "https://www.youtube.com/embed/uipjCTg_PqQ",
        "https://www.youtube.com/embed/kV1ru-Inzl4",
    ];
    $: $selectedVideo, handleVideoChange();

    function handleVideoChange() {
        url = urls[$selectedVideo];
    }
</script>

<div>
    <iframe
        src={url}
        height="600"
        width="1000"
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
