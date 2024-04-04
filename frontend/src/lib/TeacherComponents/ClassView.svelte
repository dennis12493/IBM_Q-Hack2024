<script>
    import BarChart from "./BarChart.svelte";
    import Suggestion from "./Suggestion.svelte";

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
            <Suggestion text={"You could incorporate more experiments or group projects to deepen students' understanding of biological concepts while fostering collaboration in the next lesson."}></Suggestion>
            <Suggestion text={"Consider devoting a segment to exploring different ecosystems and the creatures that inhabit them to captivate students' interest and make learning more memorable next time."}></Suggestion>
            <Suggestion text={"Next lesson, try breaking down challenging topics into bite-sized, digestible pieces. Using visual aids or analogies might help students grasp these concepts more easily."}></Suggestion>
            <Suggestion text={"Integrate examples from everyday life or nature documentaries in the next lesson to make abstract concepts more relatable and enhance comprehension."}></Suggestion>
            <Suggestion text={"During the next lesson, consider providing additional one-on-one support or personalized explanations to john for topics they find challenging. This individual attention can help them feel more confident and engaged in the lesson material."}></Suggestion>
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
        margin: 0;
        margin-bottom: 1rem;
    }

    h2 {
        font-size: 1.5rem;
        margin: 0;
        margin-bottom: 1rem;
    }

    .suggestions-wrapper{
        height: calc(50% - 3.8rem);
    }

    .suggestions {
        overflow-y: scroll;
        background-color: var(--background);
        border-radius: 5px;
        height: 100%;
    }


</style>
