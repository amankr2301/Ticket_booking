<script setup>
import { RouterLink , RouterView } from "vue-router";
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap/dist/js/bootstrap.min.js"

import store from "@/store";

</script>

<template>

  <RouterView/>
<div>
  </div>
</template>

<script>
  export default{
    created(){
      let user = JSON.parse(sessionStorage.getItem("user"))
      if (!user){
        user = {roles: [] , token: null}
      }
      store.commit("setToken" , user);

    }

  }
</script>