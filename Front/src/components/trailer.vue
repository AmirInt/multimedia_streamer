<!-- FIXME: fetch -->

<script>
export default {
	data() {
		return {
			assetPath: 'Stupid path',
			id: '01',
			director: 'Stupid man',
			year: 'In the year of stupid',
			rating: 'Stupid rating'
		}
	},
	mounted() {
		fetch("server")
			.then((response) => {
				return response.json();
			})
			.then((responseJson) => {
				this.assetPath = responseJson['assetPath'];
				this.id = responseJson['id'];
				this.director = responseJson['director'];
				this.year = responseJson['year'];
				this.rating = responseJson['rating'];
			})
			.catch((error) => {
				console.log(error);
			});
	}
}
</script>

<template>
	<div class="trailer-container">
		<div class="trailer">
			<div class="title-place">
				<div class="title-holder"><h1 class="div-title">Title: {{ assetPath }}</h1></div>
				<div>
					<h2>Director: {{ director }}</h2>
					<h2>Year: {{ year }}</h2>
					<h2>Rating: {{ rating }}</h2>
				</div>
			</div>
			<div class="video-container">
			
			</div>
		</div>
	</div>
</template>