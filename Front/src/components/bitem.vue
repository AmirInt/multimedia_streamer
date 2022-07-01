<script>
export default {
    props: {
        id: {
            type: String,
            required: true
        },
        title: {
            type: String,
            required: true
        },
        year: {
            type: String,
            required: true
        },
        assetPath: {
            type: String,
            required: true
        },
    },
    data() {
        return {
            displayTrailer: false
        }
    }
}
</script>

<template>
    <div class="bcontainer">
        <div>
            <img class="bposter" v-bind:src="assetPath" />
        </div>
        <div class="text">
            <h1>{{ title }}</h1>
            <h2>{{ year }}</h2>
        </div>
    </div>
</template>