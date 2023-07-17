<template>
	<view class="page">
		<view
			v-for="item in cart.items"
			:key="item.product.id"
			class="shop-item"
			@click="toGoods"
			v-if="cartTotalLength"
		>
			<goodsItem
				:initialItem="item"
				@removeFromCart="removeFromCart"
			></goodsItem>
		</view>
		<view class="blank"></view>
		<view class="account">
			<text class="total">￥{{ cartTotalPrice }}</text>
			<view class="pay" @click="toCheckout">
				<button type="primary">结算</button>
			</view>
		</view>
	</view>
</template>

<script>
import goodsItem from '../../components/goods-item.vue'
export default {
	components: {
		goodsItem,
	},
	data() {
		return {
			cart: {
				items: [],
			},
		}
	},
	mounted() {
		console.log('state => ', this.$store.state.cart.items)
		this.cart = this.$store.state.cart
		console.log('lcart => ', this.cart.items)
	},
	methods: {
		removeFromCart(item) {
			this.cart.items = this.cart.items.filter(
				(i) => i.product.id !== item.product.id
			)
		},
		toCheckout() {
			uni.navigateTo({
				url: '/pages/checkout/checkout',
			})
		},
	},
	computed: {
		cartTotalLength() {
			return this.cart.items.reduce((acc, curVal) => {
				return (acc += curVal.quantity)
			}, 0)
		},
		cartTotalPrice() {
			return this.cart.items.reduce((acc, curVal) => {
				return (acc += curVal.product.price * curVal.quantity)
			}, 0)
		},
	},
}
</script>
<style lang="scss">
.page {
	padding: 30rpx;

	.shop-item {
		display: flex;
		justify-content: space-between;
		align-items: center;
	}

	.account {
		display: flex;
		justify-content: space-between;
		align-items: center;
		padding-top: 100rpx;

		.check-box {
			flex: 2;
		}

		.total {
			flex: 1;
			color: red;
			font-size: 50rpx;
		}

		.pay {
			flex: 1;
			padding-left: 30rpx;
		}
	}
}
</style>
