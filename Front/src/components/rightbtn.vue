<script>
export default {
    props: {
        clickCallback: {
            type: Function,
            required: true
        },
        display: {
            type: Boolean,
            required: true
        }
    }
}
</script>

<template>
    <div class="slide-btn-container">
        <Transition>
            <div class="right-btn slide-btn" @click="clickCallback" v-show="display">
                <img src="/public/logos/up-arrow-svgrepo-com.svg" class="slide-btn-img"/>
            </div>
        </Transition>
    </div>
</template>