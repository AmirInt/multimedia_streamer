<script>
export default {
	props: {
		filmData: {
			type: Object,
			required: true
		}
	},
	mounted() {
		console.log("Fetching...");
		fetch("http://localhost:5000/api/movies")
			.then((response) => {
				return response.text();
			})
			.then((responseJson) => {
				console.log(responseJson);
				// this.assetPath = responseJson['assetPath'];
				// this.id = responseJson['id'];
				// this.director = responseJson['director'];
				// this.year = responseJson['year'];
				// this.rating = responseJson['rating'];
			})
			.catch((error) => {
				console.log(error);
			});
		console.log("Fetched");
	}
}
</script>

<template>
	<div class="trailer-container">
		<div class="trailer">
			<div class="title-place">
				<div class="title-holder"><h1 class="div-title" v-html="filmData['title']"></h1></div>
				<div>
					<h2>Director: {{ filmData['director'] }}</h2>
					<h2>Year: {{ filmData['year'] }}</h2>
					<h2>Rating: {{ filmData['rating'] }}</h2>
					<!-- <a href="/api/movies">Here</a> -->
				</div>
			</div>
			<div class="video-container">
			</div>
		</div>
	</div>
</template>