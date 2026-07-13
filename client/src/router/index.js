import { createRouter, createWebHistory } from "vue-router";
import LoginView from "@/views/LoginView.vue";
import RegisterView from "@/views/RegisterView.vue";
import AdminLayoutView from "@/views/Admin/AdminLayoutView.vue";
import LayoutView from "@/views/LayoutView.vue";
import VenueCreate from "@/views/Admin/VenueCreate.vue";
import store from "@/store";
import VenueSearch from "@/views/Admin/VenueSearch.vue";
import VenueEdit from "@/views/Admin/VenueEdit.vue";

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
        component: AdminLayoutView,
        children: [{
            path: "venue/create" , 
            name: "venue-create", 
            component: VenueCreate
        } ,
        {
            path: "venue/search" , 
            name: "venue-search", 
            component: VenueSearch
        },
        {
            path:"venue/edit/:id", 
            name: "venue-edit" , 
            component: VenueEdit
        }
                
    
    ]
    } ,
    {
        path: "/" , 
        name: "home", 
        component: LayoutView 
    },
    
    
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

router.beforeEach((to , from) => {
    
    const isLoggedIn = store.getters.getToken;
    const isAdmin = store.getters.getRoles.includes("admin");
    
    if(to.path === "/" && !isLoggedIn){
        return {name: "login"}
    }

    if (to.path == "/" && isAdmin){
        return {path : "/admin"}
        }

    if (to.path.match('/admin*' && !store.getters.getToken && !store.getters.getRoles.includes('admin'))){
        return {name : "login"}
    }
    
    if (to.path.startsWith("/admin") && (!isLoggedIn || !isAdmin)) {
        return { name: "login" };
}

            
    
})

export default router;

