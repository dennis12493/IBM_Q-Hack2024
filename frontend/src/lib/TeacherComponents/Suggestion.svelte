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
        animation: fade 0.7s ease-in;
        margin-bottom: 0.5rem;
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
