<script lang="ts">
    import { Link } from "svelte-routing";
</script>

<div class="teacher-header">
    <select>
        <option>Biology 4a</option>
        <option>Biology 3b</option>
        <option>Biology 3a</option>
        <option>English 1a</option>
        <option>English 2c</option>
    </select>

    <div class="role-wrapper">
        <Link to="/">Teacher</Link>
        <div class="profile">
            <p>JT</p>
        </div>
    </div>
</div>


<style>
    .teacher-header{
        height: 4rem;
        width: calc(100% - 6rem);
        background-color: var(--panel);

        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0rem 3rem;
    }

    .role-wrapper{
        display: flex;
        gap: 2rem;
        align-items: center;
    }

    .role{
        color: var(--border);
    }

    select {
        color: var(--text);
        padding: 0.2rem 1rem;
        text-align: center;
        font-size: 1.7rem;
        border: none;
        background-color: transparent;
    }

    .profile {
        background-color: var(--background);
        width: 3rem;
        height: 3rem;
        border-radius: 100%;
        text-align: center;
        display: flex;
        justify-content: center;
        align-items: center;
    }
</style>
