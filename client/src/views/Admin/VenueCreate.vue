<script setup>
    import InputError from '@/components/InputError.vue';
    import store from '@/store';
</script>

<template>
   
        <div class="card venue-create">
                <div class="card-body">

                <div class="alert alert-success alert-dismissible fade show" role="alert" v-if="success">
                    Venue created successfully!!
                <button
                    type="button"
                    @click="success = false"
                    class="btn-close"
                    data-bs-dismiss="alert"
                    aria-label="Close"
                ></button>
            </div>
                    <form @submit="create">
                    <div class="mb-3">
                        <label for="VenuenameInput" class="form-label">Venue name</label>
                        <input type="text" class="form-control" id="VenuenameInput" v-model = "name" 
                            placeholder="Enter venue name">
                        <InputError :value="error['name']" />

                            
                        </div>
                        <div class="mb-3">
                            <label for="VenuePlace" class="form-label">Venue Place</label>
                            <input type="text" class="form-control" id="VenuePlace" v-model = "place"
                                placeholder="Enter Venue Place ">
                            <InputError :value="error['place']"/>
                    </div>
                        <div class="mb-3" style="display: flex; justify-content: center;">
                            <input type="submit" class="btn btn-primary" style="width: 25%;">
                        </div>    
                        </form>
                </div>

            </div>
   
</template>

<script>
    export default{
        data(){
            return {
                name: null , 
                place: null , 
                success : false,
                error: {
                    name: null , 
                    place : null 
            }

            }
            
            } , 

            methods:{
                validate(){
                    let error = false 
                    this.error = {
                        name: null , 
                        place: null
                    }

                    if(!this.name){
                        error = true; 
                        this.error["name"] = "Invalid name"

                    }

                    if(!this.place){
                        error = true; 
                        this.error["place"] = "Invalid place"
                    }

                    return error ; 
                } , 
                create(event){
                    event.preventDefault();
                    if(!this.validate()){
                        let statuscode ; 
                        fetch(store.getters.BASEURL + "/venue/create", {
                            method: "POST",
                            headers: {
                                "Content-Type": "application/json",
                                "Authentication-token": store.getters.getToken
                            },
                            body: JSON.stringify({
                                name: this.name,
                                place: this.place,
                            })
                            
                            }).then(response => {
                                statuscode = response.status; 
                                if (statuscode == 201){
                                    this.success = true,
                                    this.name = null , 
                                    this.place = null
                                }
                                
                    })
                    }
                    
                }
            }
        }
    
</script>

<style scoped>
    .venue-create{
        margin: 20px;
    }
</style>