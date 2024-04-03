<script lang="ts">
    import IconUser from "./assets/User.svg";
    import IconSend from "./assets/Send.svg";
    export let sender: string, message: string;
</script>


<div class="message">
            {#if sender == "me"}
            <img src={IconUser} alt=""/>
            {/if}
            <div class="card-body">
                {message}
            </div>
            {#if sender == "other"}
            <img src={IconUser} alt=""/>
            {/if}
</div>
