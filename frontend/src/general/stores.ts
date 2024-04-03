import { writable } from "svelte/store";

// Create and export the store
const studentInput = writable<string>('');
export default studentInput;
