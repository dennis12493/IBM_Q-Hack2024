<script lang="">
    import ClassView from "../lib/TeacherComponents/ClassView.svelte";
import StudentView from "../lib/TeacherComponents/StudentView.svelte";
import TeacherHeader from "../lib/TeacherComponents/TeacherHeader.svelte";


</script>

<div class="teacher-wrapper">
    <TeacherHeader></TeacherHeader>
    <div class="teacher-body">
        <StudentView></StudentView>
        <ClassView></ClassView>
    </div>
</div>

<style>
    .teacher-wrapper{
        background-color: var(--background);
        height: 100%;
    }

    .teacher-body{
        display: flex;
        height: calc(100% - 4rem);
    }
</style>
