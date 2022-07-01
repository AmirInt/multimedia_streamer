<!-- FIXME: fetch -->

<script setup>
import Tlist from './tlist.vue'
import Blist from './blist.vue'
</script>

<script>
export default {
	props: {
		trailerPageLoader: {
			type: Function,
			required: true
		}
	},
	data() {
		return {
			topChartItems: [
				{
					id: '01',
					title: 'The Shawshank Redemption',
					year: '1994'
				},
				{
					id: '02',
					title: 'The Godfather',
					year: '1972'
				},
				{
					id: '03',
					title: 'The Dark Knight',
					year: '2008'
				},
				{
					id: '04',
					title: 'The Godfather Part II',
					year: '1974'
				},
				{
					id: '05',
					title: '12 Angry Men',
					year: '1957'
				},
				{
					id: '06',
					title: "Schindler's List",
					year: '1993'
				}
			],
			topPickItems: [
				{
					id: '01',
					title: 'Good Will Hunting',
					year: '1997'
				},
				{
					id: '02',
					title: 'Inception',
					year: '2010'
				},
				{
					id: '03',
					title: 'Lord Of The Rings: The Fellowship Of The Ring',
					year: '2001'
				},
				{
					id: '04',
					title: 'House Of Gucci',
					year: '2021'
				},
				{
					id: '05',
					title: 'Fight Club',
					year: '1999'
				},
				{
					id: '06',
					title: 'Nightmare Alley',
					year: '2021'
				},
				{
					id: '07',
					title: 'Goodfellas',
					year: '1990'
				}
			],
			fanFavouriteItems: [
				{
					id: '01',
					title: 'Sherlock',
					year: '2010'
				},
				{
					id: '02',
					title: 'Star Wars: Revenge Of The Sith',
					year: '2005'
				},
				{
					id: '03',
					title: 'Stranger Things',
					year: '2016'
				},
				{
					id: '04',
					title: 'The Boys',
					year: '2019'
				},
				{
					id: '05',
					title: 'Top Gun Maverick',
					year: '2022'
				}
			]
		}
	},
	methods: {
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
	mounted() {
		this.fetchItemsOfCategory(this.topChartItems, "http://127.0.0.1:5000/api/movies");
		this.fetchItemsOfCategory(this.topPickItems, "topPickPath");
		this.fetchItemsOfCategory(this.fanFavouriteItems, "fanFavePath");
	}
}
</script>

<template>
	<div class="lists-container">
		<div>
			<Tlist
			:itemsList="topChartItems"
			:trailerPageLoader="trailerPageLoader"
			title="Top Charts" />
		</div>
		
		<div>
			<Blist
			:itemsList="topPickItems"
			:assetPath="topPickPath"
			title="Top Picks" />
		</div>
		
		<div>
			<Blist
			:itemsList="fanFavouriteItems"
			:assetPath="fanFavouritePath"
			title="Fan Favourite" />
		</div>
	</div>
</template>