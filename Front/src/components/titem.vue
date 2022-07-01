<!-- FIXME: svg file static path -->

<script>
export default {
    props: {
        id: {
            type: String,
            required: true
        },
        assetPath1: {
            type: String,
            required: true
        },
        assetPath2: {
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
        }
    },
    data() {
        return {
            displayTrailer: false
        }
    }
}
</script>

<template>
    <a href="" @mouseenter="displayTrailer = true" @mouseleave="displayTrailer = false">
        <Transition>
            <div class="play-trailer" v-show="displayTrailer">
                <div class="play-trailer-btn">
                    <img class="play-trailer-img" src="../public/logos/play-button-svgrepo-com.svg" />
                    <span>Play Trailer</span>
                </div>
            </div>
        </Transition>
        <div class="level-1">
            <div class="level-2 left">
                <img class="tposter" v-bind:src="assetPath1" />
            </div>
            <div class="level-2 right">
                <div class="level-3">
                    <img class="thumbnail" v-bind:src="assetPath2" />
                </div>
                <div class="level-3">
                    <h1>{{ title }}</h1>
                    <h2>{{ year }}</h2>
                </div>
            </div>
        </div>
    </a>
</template>