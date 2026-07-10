import { createRouter, createWebHistory } from "vue-router";
import LoginView from "@/views/LoginView.vue";
import RegisterView from "@/views/RegisterView.vue";

const routes = [
    {
    path: "/login",
    name: "login" , 
    component: LoginView,
    },

    {
    path: "/signup",
    name: "signup" , 
    component: RegisterView,
    }
    
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;

