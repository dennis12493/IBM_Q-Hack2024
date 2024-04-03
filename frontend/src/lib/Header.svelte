<script lang="ts">
</script>

<div class="top-level">
    <!-- Header -->
    <div />
    <div>
        <select>
            <option value="1"><h1>Biology class 4a</h1></option>
            <option value="1"><h1>English class 4a</h1></option>
            <option value="1"><h1>History class 4a</h1></option>
        </select>
    </div>
    <div class="name">
        <p>LR</p>
    </div>
</div>

<style>
    .top-level {
        background-color: var(--panel);
        display: flex;
        justify-content: space-between;
        align-items: center;
        height: 4rem;
    }

    select {
        color: var(--text);
        padding: 0.2rem 1rem;
        text-align: center;
        font-size: 1.7rem;
        margin: 0.5rem;
        border: none;
        background-color: transparent;
    }

    .name {
        background-color: var(--background);
        color: var(--text);
        height: 3rem;
        width: 3rem;
        text-align: center;
        font-size: 1.5rem;
        border-radius: 100%;

        display: flex;
        justify-content: center;
        align-items: center;
    }
</style>
