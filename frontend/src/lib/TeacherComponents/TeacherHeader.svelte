<script lang="ts">

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
        <p class="role">Teacher</p>
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
        outline: none;
        border: none;
        padding: 0.4rem 2rem;
        border-radius: 5px;
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
