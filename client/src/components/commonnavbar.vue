<script setup>
import { RouterLink } from "vue-router";
</script>

<template>
    <nav class="navbar navbar-expand-lg navbar-dark custom-navbar">
        <div class="container">

            <RouterLink class="navbar-brand" to="/">
                🚀 Tickets
            </RouterLink>

            <button
                class="navbar-toggler"
                type="button"
                data-bs-toggle="collapse"
                data-bs-target="#navbarSupportedContent"
                aria-controls="navbarSupportedContent"
                aria-expanded="false"
                aria-label="Toggle navigation"
            >
                <span class="navbar-toggler-icon"></span>
            </button>

            <div
                class="collapse navbar-collapse"
                id="navbarSupportedContent"
            >
                <ul class="navbar-nav ms-auto">

                    <li class="nav-item">
                        <RouterLink class="nav-link glass-link" to="/login">
                            Login
                        </RouterLink>
                    </li>

                    <li class="nav-item">
                        <RouterLink class="glass-button" to="/signup">
                            Register
                        </RouterLink>
                    </li>

                </ul>
            </div>

        </div>
    </nav>
</template>

<style scoped>

.custom-navbar{

    background:linear-gradient(
        135deg,
        #111827,
        #1e293b,
        #0f172a
    );

    backdrop-filter:blur(18px);

    -webkit-backdrop-filter:blur(18px);

    border-bottom:1px solid rgba(255,255,255,.08);

    box-shadow:0 10px 30px rgba(0,0,0,.25);

    padding:14px 0;

}


.navbar-brand{

    color:white !important;

    font-size:24px;

    font-weight:700;

    letter-spacing:.6px;

    transition:.3s;

}


.navbar-brand:hover{

    color:#60a5fa !important;

}


.navbar-nav{

    gap:14px;

    align-items:center;

}


.glass-link{

    position:relative;

    overflow:hidden;

    padding:10px 18px !important;

    border-radius:12px;

    color:#d1d5db !important;

    transition:all .35s ease;

}


.glass-link:hover{

    background:rgba(255,255,255,.08);

    backdrop-filter:blur(14px);

    color:white !important;

    transform:translateY(-2px);

}


.glass-link::before{

    content:"";

    position:absolute;

    top:0;

    left:-100%;

    width:100%;

    height:100%;

    background:linear-gradient(
        90deg,
        transparent,
        rgba(255,255,255,.18),
        transparent
    );

    transition:.6s;

}


.glass-link:hover::before{

    left:100%;

}


.glass-button{

    text-decoration:none;

    color:white;

    padding:10px 22px;

    border-radius:12px;

    background:rgba(59,130,246,.25);

    border:1px solid rgba(96,165,250,.45);

    backdrop-filter:blur(12px);

    transition:all .35s;

    font-weight:600;

}


.glass-button:hover{

    background:#2563eb;

    color:white;

    transform:translateY(-2px);

    box-shadow:0 10px 25px rgba(37,99,235,.4);

}


.navbar-toggler{

    border:none;

}


.navbar-toggler:focus{

    box-shadow:none;

}


@media(max-width:991px){

    .navbar-nav{

        margin-top:18px;

        gap:10px;

    }

    .glass-button{

        display:block;

        text-align:center;

    }

}

</style>