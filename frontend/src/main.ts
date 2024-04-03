import './app.css'
import App from './App.svelte'
import "@tabler/core/dist/css/tabler.min.css"

const app = new App({
  target: document.getElementById('app')!,
})

export default app
