<script setup>
import Header from './header.vue'
import Main from './main.vue'
import Trailer from './trailer.vue'
</script>

<script>
export default {
	data() {
		return {
			currentPage: 'home',
			trailerID: ''
		}
	},
	methods: {
		loadTrailerPage(id) {
			this.trailerID = id;
			this.currentPage = 'trailer';
		},
		loadMainPage() {
			this.currentPage = 'home';
		}
	},
	computed: {
		pageMain() {
			return this.currentPage === 'home'
		}
	}
}
</script>

<template>
	<Header :mainPageLoader="loadMainPage" />
	<Main v-if="pageMain" :trailerPageLoader="loadTrailerPage" />
	<Trailer v-else :id="trailerID" />
</template>