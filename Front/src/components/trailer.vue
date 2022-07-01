<script>
export default {
	props: {
		filmData: {
			type: Object,
			required: true
		}
	},
	mounted() {
		let url = '';
		let id = this.filmData.id;
		let player = dashjs.MediaPlayer().create();
		let video = document.querySelector(".video");
		switch(id) {
			case '3':
				url = "https://amirint.arvanvod.com/vqLVyd4DNp/XvZQDjr2lV/h_,144_200,240_400,360_800,480_1500,k.mp4.list/manifest.mpd";
				player.initialize(document.querySelector(".video"), url, true);
				break;
			case '4':
				url = "https://amirint.arvanvod.com/vqLVyd4DNp/j9D5Q3rgJA/h_,144_200,240_400,360_800,480_1500,k.mp4.list/manifest.mpd";
				player.initialize(document.querySelector(".video"), url, true);
				break;
			case '5':
				url = "https://amirint.arvanvod.com/vqLVyd4DNp/XMK2kxBgrw/h_,144_200,240_400,360_800,480_1500,k.mp4.list/master.m3u8";
				if (Hls.isSupported()) {
					var hls = new Hls();
					hls.loadSource(url);
					hls.attachMedia(video);
				}
				break;
			case '6':
				url = "https://amirint.arvanvod.com/vqLVyd4DNp/LjlpDke7JO/h_,144_200,240_400,360_800,480_1458,k.mp4.list/master.m3u8";
				if (Hls.isSupported()) {
					var hls = new Hls();
					hls.loadSource(url);
					hls.attachMedia(video);
				}
			break;
			default:
			fetch(`http://localhost:5000/api/stream/${id}`)
				.then((response) => {
					return response.text();
				})
				.then((responseText) => {
					console.log(responseText)
					let player = dashjs.MediaPlayer().create();
					player.initialize(document.querySelector(".video"), responseText, true);
				})
				.catch((error) => {
					console.log(error);
				});
		}
	}
}
</script>

<template>
	<div class="trailer-container">
		<div class="trailer">
			<div class="title-place">
				<div class="title-holder"><h1 class="div-title" v-html="filmData.name"></h1></div>
				<div>
					<h2>Director: {{ filmData.director }}</h2>
					<h2>Year: {{ filmData.year }}</h2>
					<h2>Rating: {{ filmData.score }}</h2>
				</div>
			</div>
			<div class="video-container">
				<video class="video" controls></video>
			</div>
		</div>
	</div>
</template>