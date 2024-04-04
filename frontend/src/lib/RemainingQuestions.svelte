<script>

</script>

<div>
    <h1>Questions for next Class</h1>
    <div class="messages">
        <p>
            Can we please talk a bit more about the wildlife in America? I think it is quite confusing.
        <p>
        <div class="line"></div>
    </div>
    <input placeholder="Remaining questions for the teacher..."/>
</div>

<style>
    h1{
        margin: 0;
        font-size: 1.4rem;
        color: var(--accent);
    }

    input {
        position: absolute;
        bottom: 2rem;

        width: calc(40% - 1rem);
        padding: 1rem 0rem;
        padding-left: 0.3rem;
        outline: none;
        border: none;
        border-radius: 0 0 5px 5px;
    }

    .messages{
        padding-top: 2rem;
        animation: 0.7s fade ease-in forwards;
    }

    .line{
        width: 100%;
        height: 1px;
        background-color: var(--border);
        margin-top: 0.5rem;
        margin-bottom: 0.5rem;
    }

    @keyframes fade {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }
</style>
