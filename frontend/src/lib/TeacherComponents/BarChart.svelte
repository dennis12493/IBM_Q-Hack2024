
<div class="bar-chart">
    <div class="bar"><p>Digestion</p></div>
    <div class="bar"><p>Unicellular organism</p></div>
    <div class="bar"><p>Wildlife</p></div>
    <div class="bar"><p>Genes</p></div>
</div>


<style>
    p{
        margin-left: 0.8rem;
    }

    .bar-chart{
        width: 100%;
        padding: 1rem 0;

        display: flex;
        flex-direction: column;
        gap: 1rem;

        background-color: rgba(0, 0, 0, 0.23);
        border-radius: 10px;


    }

    .bar {
        width: 0%;
        height: 2rem;
        background-color: var(--contrast);
        color: var(--background);
        display: flex;
        align-items: center;
        margin-left: 1rem;
        white-space: nowrap;

        animation: growBar 0.7s ease-in forwards;
    }

    .bar:nth-child(2) {
        animation: growBar2 0.7s 0.1s ease-in forwards;
    }

    .bar:nth-child(3) {
        animation: growBar3 0.7s 0.2s ease-in forwards;
    }

    .bar:nth-child(4) {
        animation: growBar4 0.7s 0.3s ease-in forwards;
    }

    @keyframes growBar {
        from {
            width: 0%;
        }
        to {
            width: 93%;
        }
    }

    @keyframes growBar2 {
        from {
            width: 0%;
        }
        to {
            width: 80%;
        }
    }

    @keyframes growBar3 {
        from {
            width: 0%;
        }
        to {
            width: 66%;
        }
    }

    @keyframes growBar4 {
        from {
            width: 0%;
        }
        to {
            width: 20%;
        }
    }


</style>
