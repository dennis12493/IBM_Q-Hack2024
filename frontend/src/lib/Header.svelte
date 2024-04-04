<script lang="ts">
    import { Link } from "svelte-routing";

</script>

<div class="top-level">
    <!-- Header -->
    <div />
    <div class="select-wrapper">
        <select>
            <option value="1"><h1>Biology</h1></option>
            <option value="1"><h1>English</h1></option>
            <option value="1"><h1>History</h1></option>
        </select>
    </div>
    <div class="name-wrapper">
        <Link to="/teacher">Student</Link>
        <div class="name">
            <p class="initials">LR</p>
        </div>
    </div>
</div>

<style>
    .top-level {
        background-color: var(--panel);
        display: flex;
        justify-content: space-around;
        align-items: center;
        height: 4rem;
        width: 100%;
    }

    .select-wrapper{
        width: 45%;
        padding-left: 2rem;
    }

    select {
        color: var(--text);
        padding: 0.2rem 1rem;
        text-align: center;
        font-size: 1.7rem;
        border: none;
        background-color: transparent;
    }

    .name-wrapper{
        width: 54%;
        display: flex;
        justify-content: end;
        align-items: center;
        gap: 2rem;
        padding-right: 3rem;
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

    .initials{
        font-size: 1rem;
    }
</style>
