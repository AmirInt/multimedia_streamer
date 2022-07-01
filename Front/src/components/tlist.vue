<script setup>
import Titem from './titem.vue'
import Leftbtn from './leftbtn.vue'
import Rightbtn from './rightbtn.vue'
</script>
<script>
export default {
    props: {
        itemsList: {
            type: Array,
            required: true
        },
        trailerPageLoader: {
            type: Function,
            required: true
        },
        title: {
            type: String,
            required: true
        }
    },
    data() {
        return {
            itemsNumber: this.itemsList.length,
            displayedItem: 1,
            mouseOn: false
        }
    },
    methods: {
        slideLeft() {
            if(this.displayedItem > 1)
                --this.displayedItem;
        },
        slideRight() {
            if(this.displayedItem < this.itemsNumber)
                ++this.displayedItem;
        }
    }
}
</script>

<template>
    <div class="list">
        <div class="title-place">
            <div class="title-holder"><h1 class="div-title">{{ title }}</h1></div>
        </div>
        <div class="holder" @mouseenter="mouseOn = true" @mouseleave="mouseOn = false">
            <div>
                <Leftbtn :clickCallback="slideLeft" :display="mouseOn && (displayedItem > 1)" />
            </div>
            <div class="tlist">
                <div class="titem-container" v-for="item of itemsList"
                :style="{ left: `${-1 * (displayedItem - 1) * 61.2}vw` }">
                    <Titem
                    :id="item.id"
                    :assetPath1="item.assetPath1"
                    :assetPath2="item.assetPath2"
                    :title="item.title"
                    :year="item.year"
                    @click.prevent="trailerPageLoader(item.id)"
                    />
                </div>
            </div>
            <div>
                <Rightbtn :clickCallback="slideRight" :display="mouseOn && (displayedItem < itemsNumber)" />
            </div>
        </div>
    </div>
</template>