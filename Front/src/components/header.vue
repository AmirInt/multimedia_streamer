<script setup>
import Queryitem from './queryitem.vue';
</script>
<script>
export default {
    props: {
        mainPageLoader: {
            type: Function,
            required: true
        }
    },
    data() {
        return {
            query: '',
            hasResult: false,
            queryResult: {},
            hasError: false
        }
    },
    watch: {
        query(newQuery) {
            if(newQuery.length > 0)
                this.getResult();
            else {
                this.hasResult = false;
                this.hasError = false;
            }
        }
    },
    methods: {
        async getResult() {
            let response = await fetch(`https://imdb-api.com/en/API/Search/k_52k0dear/${this.query}`)
                .then((response) => {
                    return response.text();
                })
                .then((html) => {
                    let parser = new DOMParser();
                    let doc = parser.parseFromString(html, 'text/html');
                    let responseJson = JSON.parse(doc.body.innerHTML);
                    this.queryResult = responseJson.results[0];
                    this.hasResult = true;
                    this.hasError = false;
                    console.log(this.queryResult)
                })
                .catch((error) => {
                    this.hasError = true;
                    this.hasResult = true;
                });
        }
    }
}
</script>

<template>
    <header>
        <div>
            <a href="" @click.prevent>
                <div @click="mainPageLoader">
                    <span>Home Page</span>
                    <img class="home-img" src="../assets/logos/home-svgrepo-com.svg" />
                </div>
            </a>
        </div>
        <div>
            <span>Search IMDB:</span>
            <input type="text" placeholder="Search Titles" v-model="query" />
        </div>
        <Transition>
            <Queryitem v-if="hasResult" :hasError="hasError" :queryItem="queryResult" @mouseleave="hasResult = false"/>
        </Transition>
    </header>
</template>