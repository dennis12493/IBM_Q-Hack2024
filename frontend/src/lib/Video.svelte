<script lang="ts">
    import selectedVideo from "../general/stores";
    let url: string = "";
    let urls: string[] = [
        "https://www.youtube.com/embed/v6tUWk7vC6g",
        "https://www.youtube.com/embed/uipjCTg_PqQ",
        "https://www.youtube.com/embed/NiKtZgImdlY",
    ];
    $: $selectedVideo, handleVideoChange();

    function handleVideoChange() {
        url = urls[$selectedVideo];
    }
</script>

<div>
    <iframe title="Explanation video" src={url} class="responsive-iframe"></iframe>
</div>

<style>
    div {
        background-color: var(--background);
        position: relative;
        overflow: hidden;
        width: 100%;
        padding-top: 56.25%;
    }
    .responsive-iframe {
        position: absolute;
        top: 0;
        left: 0;
        bottom: 0;
        right: 0;
        width: 100%;
        height: 100%;
    }
</style>
