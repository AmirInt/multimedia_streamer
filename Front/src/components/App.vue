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
			trailerID: '',
			topChartItems: [],
			topPickItems: [],
			fanFavouriteItems: []
		}
	},
	methods: {
		loadTrailerPage(id) {
			this.trailerID = id;
			this.currentPage = 'trailer';
		},
		loadMainPage() {
			this.currentPage = 'home';
		},
		async fetchItemsOfCategory(list, path) {
			await fetch(path)
				.then((response) => {
					return response.json();
				})
				.then((responseJson) => {
					responseJson.forEach(item => {
						list.push(item);
					})
				})
				.catch((error) => {
					console.log(error);
				});
		} 
	},
	computed: {
		pageMain() {
			return this.currentPage === 'home'
		},
		trailerIDNum() {
			return parseInt(this.trailerID) - 1;
		}
	},
	mounted() {
		this.fetchItemsOfCategory(this.topChartItems, "http://127.0.0.1:5000/api/movies");
		this.fetchItemsOfCategory(this.topPickItems, "http://127.0.0.1:5000/api/topPicks");
		this.fetchItemsOfCategory(this.fanFavouriteItems, "http://127.0.0.1:5000/api/fanFav");
	}
}
</script>

<template>
	<Header :mainPageLoader="loadMainPage" />
	<Main v-if="pageMain"
	:trailerPageLoader="loadTrailerPage"
	:topChartItems="topChartItems"
	:topPickItems="topPickItems"
	:fanFavouriteItems="fanFavouriteItems" />
	<Trailer v-else :filmData="topChartItems[trailerIDNum]" />
</template>