<script>
export default {
    props: {
        hasError: {
            type: Boolean,
            required: true
        },
        queryItem: {
            type: Object,
            required: false
        }
    },
}
</script>

<template>
    <div class="query-item">
        <div class="query-item-error" v-if="hasError">
            <h2>Failed to search :(</h2>
        </div>
        <div class="query-item-data" v-else>
            <div>
                <img class="query-img" :src="queryItem['image']" />
            </div>
            <div>
                <h3>Film Title: {{ queryItem['title'] }}</h3>
                <h4>Description: {{ queryItem['description'] }}</h4>
            </div>
        </div>
    </div>
</template>