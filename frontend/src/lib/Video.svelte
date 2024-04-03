<script lang="ts">
    import {selectedVideo, urls, timestamp} from "../general/stores";
    let url: string = "";
    $: $selectedVideo, handleVideoChange();

    function handleVideoChange() {
        url = "https://www.youtube.com/embed/" + urls[$selectedVideo];
    }

    $: $timestamp, handleTimestampChange();
    let videoUrl: string = "";
    function handleTimestampChange() {
        if($timestamp !== undefined && $timestamp !== null && $timestamp !== 0){
            videoUrl = url + "?start=" + $timestamp;
        }
    }
</script>

<div>
    <iframe title="Explanation video" src={videoUrl} class="responsive-iframe"></iframe>
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
