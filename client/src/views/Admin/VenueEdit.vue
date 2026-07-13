<script setup>
    import InputError from '@/components/InputError.vue';
    import store from '@/store';
    import router from '@/router';
</script>

<template>
   
        <div class="card venue-Edit">
                <div class="card-body">

                <div class="alert alert-success alert-dismissible fade show" role="alert" v-if="success">
                    Updated successfully!!
                <button
                    type="button"
                    @click="success = false"
                    class="btn-close"
                    data-bs-dismiss="alert"
                    aria-label="Close"
                ></button>
            </div>
                    <form @submit="Edit">
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

            created(){
                console.log(this.$route.query.name)
                this.name = this.$route.query.name ; 
                this.place = this.$route.query.place


            },

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
                Edit(event){
                    event.preventDefault();
                    console.log(this.$route.params.id);
                    
                    if(!this.validate()){
                        let statuscode ; 
                        fetch(store.getters.BASEURL + "/venue/" + this.$route.params.id+"/edit",{
                            method: "POST",
                            headers: {
                                "Content-Type": "application/json",
                                "Authentication-token": store.getters.getToken
                            },
                            body: JSON.stringify({
                                id: this.id,
                                name: this.name,
                                place: this.place,
                            })
                            
                            }).then(response => {
                                statuscode = response.status; 
                                if (statuscode == 200){
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
    .venue-Edit{
        margin: 20px;
    }
</style>