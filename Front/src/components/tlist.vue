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
        },
        loadTrailer(trailerID) {
            this.trailerID = trailerID;
            this.page = 'trailer';
            console.log(this.page);
        },
        print() {
            console.log(this.mouseOn);
        }
    },
    mounted() {
        setInterval(() => {
            this.render = true
        })
    }
}
</script>

<template>
    <Transition>
        <div class="list">
            <div class="title-place">
                <div class="title-holder"><h1 class="div-title">{{ title }}</h1></div>
            </div>
            <div class="holder" @mouseenter="mouseOn = true" @mouseleave="mouseOn = false" :delay="5000">
                <Leftbtn :clickCallback="slideLeft" :display="mouseOn && (displayedItem > 1)" />
                <div class="tlist">
                    <div class="titem-container" v-for="item of itemsList"
                    :style="{ left: `${-1 * (displayedItem - 1) * 61.2}vw` }">
                        <Titem
                        :id="item.id"
                        :title="item.name"
                        :year="item.year"
                        :assetPath1="item.address1"
                        :assetPath2="item.address2"
                        @click.prevent="trailerPageLoader(item.id)"
                        />
                    </div>
                </div>        
                <Rightbtn :clickCallback="slideRight" :display="mouseOn && (displayedItem < itemsNumber)" />
            </div>
        </div>
    </Transition>
</template>