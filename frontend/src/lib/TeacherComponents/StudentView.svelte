<script>
    import AiAnswers from "../AiAnswers.svelte"
    import  chart  from '../assets/studentchart.png';
    import Curriculum from "./Curriculum.svelte";
    import VerticalBarChart from './VerticalBarChart.svelte';
</script>


<div class="student-view">
    <img class="chart" src={chart} alt="">
    <div class="horizontal-wrapper">
        <Curriculum></Curriculum>
        <VerticalBarChart></VerticalBarChart>
    </div>
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
        user-select: none;
    }

    .horizontal-wrapper{
        display: flex;
        justify-content: center;
        gap: 1rem;
        padding: 0rem 1rem;
    }
</style>
