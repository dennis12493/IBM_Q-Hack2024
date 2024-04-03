<script>
    import AiAnswers from "../AiAnswers.svelte"
    import  chart  from '../assets/studentchart.png';
</script>


<div class="student-view">
    <img class="chart" src={chart}>
</div>

<style>
    .student-view{
        background-color: var(--panel);
        margin: 0.8rem;
        padding: 0.5rem;
        height: calc(100% - 2.6rem);
        width: 100%;

        border-radius: 0.4rem;
    }

    .chart{
        width: 100%;
    }
</style>
