<script>
    import BarChart from "./BarChart.svelte";

</script>

<div class="class-view">
    <div class="class-stats">
        <div class="bar-chart-wrapper">
            <h1>Class Overview</h1>
            <BarChart />
        </div>
        <div class="pie-chart-wrapper">
            <p class="margin-top">Questions per Student</p>
            <div class="pie-chart"></div>
        </div>
    </div>
    <div class="suggestions-wrapper">
        <h2>Suggestions for Improvement</h2>
        <div class="suggestions">
            Text
        </div>
    </div>
</div>

<style>
    .class-view{
        width: 100%;
        background-color: var(--panel);
        height: calc(100% - 2.6rem);
        margin: 0.8rem;
        padding: 0.5rem;

        border-radius: 0.4rem;
    }

    .class-stats{
        height: 50%;
        display: flex;

    }

    .margin-top{
        margin-top: 2rem;
    }

    .bar-chart-wrapper{
        display: flex;
        flex-direction: column;
        width: 100%;
    }

    .pie-chart-wrapper{
        display: flex;
        flex-direction: column;
        gap: 1rem;
        justify-content: start;
        align-items: center;
        width: 100%;
    }

    .pie-chart{
        border-radius: 100%;
        width: 15rem;
        height: 15rem;
        background-color: var(--accent);
    }

    h1{
        color: var(--accent);
    }

    h2 {
        font-size: 1.2rem;
    }

    .suggestions-wrapper{
        height: calc(50% - 3.8rem);
    }

    .suggestions {
        background-color: var(--background);
        border-radius: 5px;
        height: 100%;
    }


</style>
