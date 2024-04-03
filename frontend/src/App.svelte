<!-- App.svelte -->
<script lang="ts">
  import { Route, Router } from 'svelte-routing';
  import StudentPage from './pages/StudentPage.svelte';
  import TeacherPage from './pages/TeacherPage.svelte';
</script>

<Router>
    <Route path="/" component={StudentPage} />
    <Route path="/teacher" component={TeacherPage} />
</Router>
