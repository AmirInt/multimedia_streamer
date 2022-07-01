<script setup>
import Bitem from './bitem.vue'
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
        title: {
            type: String,
            required: true
        }
    },
    data() {
        return {
            itemsNumber: this.itemsList.length,
            lastItem: 3,
            mouseOn: false
        }
    },
    methods: {
        slideLeft() {
            if(this.lastItem > 3)
                --this.lastItem;
        },
        slideRight() {
            if(this.lastItem < this.itemsList.length)
                ++this.lastItem;
        }
    },
    mounted() {}
}
</script>


<template>
    <div class="list">
        <div class="title-place">
            <div class="title-holder"><h1 class="div-title">{{ title }}</h1></div>
        </div>
        <div class="holder" @mouseenter="mouseOn = true" @mouseleave="mouseOn = false">
            <div>
                <Leftbtn :clickCallback="slideLeft" :display="mouseOn && (lastItem > 3)" />
            </div>
            <div class="blist">
                <div class="bitem-container" v-for="item of itemsList"
                :style="{ left: `${-1 * (lastItem - 3) * 20}vw` }">
                    <Bitem
                    :id="item.id"
                    :title="item.name"
                    :year="item.year"
                    :assetPath="item.address"
                    />
                </div>
            </div>
            <div>
                <Rightbtn :clickCallback="slideRight" :display="mouseOn && (lastItem < itemsList.length)" />
            </div>
        </div>
    </div>
</template>