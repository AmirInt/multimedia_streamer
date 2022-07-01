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
		},
		topChartItems: {
			type: Array,
			required: true
		},
		topPickItems: {
			type: Array,
			required: true
		},
		fanFavouriteItems: {
			type: Array,
			required: true
		}
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
			title="Top Picks" />
		</div>
		
		<div>
			<Blist
			:itemsList="fanFavouriteItems"
			title="Fan Favourite" />
		</div>
	</div>
</template>