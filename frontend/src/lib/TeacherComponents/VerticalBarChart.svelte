<script></script>

<div class="bar-chart">
    <p>Relative Performance</p>
    <div class="chart-wrapper">
        <div class="bar"></div>
        <div class="bar"></div>
    </div>
</div>


<style>
    .bar-chart{
        width: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 1rem;

    }

    p{
        font-size: 1.2rem;
        font-weight: 500;
    }

    .bar{
        width: 5rem;
    }

    .chart-wrapper{
        display: flex;
        gap: 0.1rem;
        justify-content: center;
        align-items: end;
        height: 80%;
        width: 100%;
    }

    .bar:nth-child(1){
        height: 0%;
        background-color: var(--contrast);
        animation: growBar 0.75s ease-in forwards;
    }
    .bar:nth-child(2){
        height: 0%;
        background-color: var(--accent);
        animation: growBar1 0.75s 0.2s ease-in forwards;
    }

        @keyframes growBar {
        from {
            height: 0%;
        }
        to {
            height: 60%;
        }
    }

    @keyframes growBar1 {
        from {
            height: 0%;
        }
        to {
            height: 95%;
        }
    }
</style>
