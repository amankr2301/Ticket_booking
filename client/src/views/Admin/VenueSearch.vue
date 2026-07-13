<script setup>
    import InputError from '@/components/InputError.vue';
    import store from '@/store';
</script>

<template>
     <form @submit="SearchVenue">
    <div class="row venue-search" >
       
            <div class="col" style="min-width: 60%;">
                <input type="text" class="form-control" placeholder="First name" aria-label="First name" v-model = "search">
                <InputError :value="error['search']" />
            </div>
                <div class="col" style="min-width: 20%;">
                    <select class="form-select" aria-label="Filter" v-model="option">
                        <option>Place</option>
                        <option>Name</option>
                    </select>
                </div>
                <div class="col">
                    <input style="width: 100%;" type="submit" class="btn btn-success" value="Search">
                </div>
                </div>
        </form>

            

    <div class="card-body p-0">
        <table class="table table-hover mb-0">
            <thead>
                <tr>
                    <th class="ps-4">Name</th>
                    <th class="pe-4">Place</th>
                    <th class="text-center" style="width: 520px;">Actions</th>
                </tr>
                
            </thead>
            
            <tbody>
                <tr v-for="venue in venues" :key="venue.id">
                    <td class="ps-4">{{ venue.name }}</td>

                    <td class="pe-4">
                        {{ venue.place }}
                    </td>

                    <td class="text-center">
                        <router-link
                            class="btn btn-sm me-5"
                            :to= "{name : 'venue-edit' , params : {id : venue.id} , query: {name: venue.name , place: venue.place}}">
                            ✏️ Edit
                        </router-link>

                        <button
                            class="btn btn-sm me-5"
                            :to="{name : 'venue-edit'}">
                            🗑️ Delete
                        </button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>

</template>


<script>
    export default{
        data(){
            return {
            search: null ,
            option: 'Place' , 
            venues: [] , 
            error:{
                search: null , 
            }
        }
        } , 
        methods:{
            validate(){
            let error = false 
            this.error= {
                search: null 
            }

            if(!this.search){
                error = true 
                this.error["search"] = "Invalid Input"
                return true
            }
        },
        SearchVenue(event){
            
            event.preventDefault()
            this.validate()
            fetch(store.getters.BASEURL + "/venue/search", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authentication-token": store.getters.getToken
                            },
                    body: JSON.stringify({
                        search: this.search,
                        option: this.option,
                            })
                            }).then(response =>{
                                if (response.status == 200){
                                    return response.json()
                                }
                                return [] ; 
                                                            
                            }).then(data =>{
                                this.venues = data ; 
                                console.log(data)
                            })
                    
            }
        
        

    }
}
</script>
<style scoped>
    .venue-search{
        margin: 20px;
    }

    .table th,
    .table td {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }

    
</style>