<script lang="ts">
    export let text: string;
</script>


<div class="message">
    <p>{text}</p>
</div>

<style>
    .message{
        border-bottom: 2px solid var(--border);
        padding: 0.3rem 1rem;
        margin-bottom: 0.5rem;
        opacity: 0;
        animation: fade 0.7s 0.5s ease-in forwards;
    }

    p{
        color: var(--text);
        font-size: 1.2rem;
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
