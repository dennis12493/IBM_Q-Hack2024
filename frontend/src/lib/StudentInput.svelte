<script lang="ts">
    import studentInput from "../general/stores";

    // Speichert den student input in einer globalen variable
    const handleChange = (event: Event) => {
        studentInput.set((event.target as HTMLInputElement).value);
    } 
</script>

<div>
    <input on:change={handleChange}>
</div>

<style>
    div{
        background-color: var(--background);
    }
</style>
