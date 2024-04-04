<script lang="ts">
    import { onMount } from "svelte";
    import {selectedVideo, urls, timestamp} from "../general/stores";
    let url: string = "";
    let videoUrl: string = "";

    $: $selectedVideo, handleVideoChange();

    function handleVideoChange() {
        url = "https://www.youtube.com/embed/" + urls[$selectedVideo] ;
        videoUrl = "";
    }

    $: $timestamp, handleTimestampChange();

    function handleTimestampChange() {
        if($timestamp !== undefined && $timestamp !== null && $timestamp !== 0){
            videoUrl = url + "?start=" + $timestamp + "&autoplay=1";
            console.log(videoUrl);
        }
    }

    const setVideoSize = () => {
        const videoFrame = document.getElementById('video-frame');
        const videoContainer = document.getElementById('video-container');
        const aspectRatio = 16 / 9; // Adjust this according to your video's aspect ratio
        const containerWidth = videoContainer? videoContainer.offsetWidth : 0;
        const newHeight = containerWidth ? containerWidth / aspectRatio: 0;
        videoFrame ? videoFrame.style.height = newHeight + 'px' : '';
    }

    onMount(() => {
        setVideoSize();
        window.addEventListener('resize', setVideoSize);
    })
</script>

<div id="video-container">
    <iframe id="video-frame" title="Explanation video" src={videoUrl == "" ? url: videoUrl} class="responsive-iframe" allowfullscreen frameborder="0"></iframe>
</div>

<style>
    div {
        display: flex;
        align-items: start;
        padding-top: 1rem;
        margin-bottom: 2rem;
        height: calc(100% - 5rem);
    }
    .responsive-iframe {
        width: 100%;
        height: 100%;

        outline: none;
        border: none;
        border-radius: 5px;
    }

    #video-container{
        height: 45%;
    }
</style>
