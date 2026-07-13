<script setup>
import { RouterView, RouterLink } from "vue-router";

</script>
<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <router-link class="navbar-brand" to="/admin">
                Tickets
            </router-link>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item dropdown">
                    <router-link class="nav-link dropdown-toggle" to="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                      Venue
                    </router-link>
                    <ul class="dropdown-menu">
                      <li><router-link class="dropdown-item" to="/admin/venue/create">Create</router-link></li>
                      <li><router-link class="dropdown-item" to="/admin/venue/search">Search</router-link></li>
                    </ul>
                  </li>          
            </ul>
            </div>
        </div>
    </nav>
    <RouterView/>
</template>