<script setup>

import "bootstrap/dist/css/bootstrap.min.css"
import store from "@/store";

</script>

<template>
  
<div>
    <h1>{{ store.state.message }}</h1>

  </div>
</template>

<style>
</style>