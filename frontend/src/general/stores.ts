import { writable } from "svelte/store";

// Create and export the store
const selectedVideo = writable<number>(0);
export default selectedVideo;
