<script>
  export let size = 200;
  export let percent = 0;

  $: viewBox = `0 0 ${size} ${size}`;

  $: radius = size / 2;
  $: halfCircumference = Math.PI * radius;
  $: pieSize = halfCircumference * (percent / 100);
  $: dashArray = `0 ${halfCircumference - pieSize} ${pieSize}`;
</script>

<div>
    <svg width={size} height={size} {viewBox}>
        <circle r={radius} cx={radius} cy={radius} fill={'var(--accent)'} />
        <circle
        r={radius / 2}
        cx={radius}
        cy={radius}
        fill={'var(--accent)'}
        stroke={'rgb(123, 175, 232)'}
        stroke-width={radius}
        stroke-dasharray={dashArray}
        />
    </svg>
    <p id="john">John</p>
    <p id="anna">Anna</p>
</div>

<style>
    p{
        color: rgb(123, 175, 232);
    }

    #john{
        position: relative;
        color: var(--background);
        bottom: 5rem;
        left: 4rem;
        width: 2rem;
    }

    #anna{
        position: relative;
        color: var(--background);
        bottom: 12rem;
        left: 6.3rem;
        width: 2rem;
    }
</style>
