<script>
import axios from 'axios'
export default {
	data() {
		return {
			cart: {
				items: [],
			},
		}
	},
	beforeCreate() {
		this.$store.commit('initializeStore')

		const token = this.$store.state.token

		if (token) {
			axios.defaults.headers.common['Authorization'] = 'Token ' + token
		} else {
			axios.defaults.headers.common['Authorization'] = ''
		}
	},
	computed: {
		cartTotalLength() {
			let totalLength = 0

			for (let i = 0; i < this.cart.items.length; i++) {
				totalLength += this.cart.items[i].quantity
			}

			return totalLength
		},
	},
	mounted() {
		this.cart = this.$store.state.cart
	},
	onLaunch: function () {
		console.log('App Launch')
	},
	onShow: function () {
		console.log('App Show')
	},
	onHide: function () {
		console.log('App Hide')
	},
}
</script>

<style>
/*每个页面公共css */
</style>
