<template>
    <div class="invalid-feedback"
    :style="{display: (value)? 'block': 'none'}">
        {{ value }}
    </div>
</template>

<script>
    export default{
        props: ["value"]
    }
</script>