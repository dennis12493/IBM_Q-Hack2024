import { writable } from "svelte/store";

// Create and export the store
export const selectedVideo = writable<number>(0);
export const selectedVideoButtonId = writable<number>(0);

export const urls: string[] = [
    "v6tUWk7vC6g",
    "uipjCTg_PqQ",
    "NiKtZgImdlY",
];

export const timestamp = writable<number>(0);
