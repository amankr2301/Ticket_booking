import { createRouter, createWebHistory } from "vue-router";
import LoginView from "@/views/LoginView.vue";
import RegisterView from "@/views/RegisterView.vue";
import AdminLayoutView from "@/views/Admin/AdminLayoutView.vue";

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
    },

    {
        path: "/admin", 
        name: "admin" , 
        component: AdminLayoutView
    }
    
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;

