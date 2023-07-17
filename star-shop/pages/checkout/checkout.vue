<template>
	<view class="page">
		<h3 class="title">订单详情</h3>
		<view class="cart-area">
			<uni-card
				v-for="item in cart.items"
				:title="item.product.name"
				:sub-title="item.quantity"
				:extra="`￥${getItemTotal(item).toFixed(2)}`"
				:thumbnail="item.product.get_thumbnail"
			>
			</uni-card>
		</view>

		<view class="shipping-area">
			<uni-section title="填写运输信息" type="line">
				<uni-forms label-position="left" label-align="center">
					<uni-forms-item label="名字">
						<uni-easyinput type="text" placeholder="请输入名字" />
					</uni-forms-item>
					<uni-forms-item label="姓氏">
						<uni-easyinput type="text" placeholder="请输入姓氏" />
					</uni-forms-item>
					<uni-forms-item label="Email">
						<uni-easyinput type="text" placeholder="请输入Email" />
					</uni-forms-item>
					<uni-forms-item label="手机">
						<uni-easyinput type="text" placeholder="请输入手机号" />
					</uni-forms-item>
					<uni-forms-item label="邮编">
						<uni-easyinput type="text" placeholder="请输入所在地的邮政编码" />
					</uni-forms-item>
					<uni-forms-item label="地区">
						<uni-easyinput type="text" placeholder="请输入所在地区" />
					</uni-forms-item>
				</uni-forms>
				<view v-if="cartTotalLength">
					<button class="commitBtn" type="primary" @click="submitForm">
						提交订单
					</button>
				</view>
			</uni-section>
		</view>
	</view>
</template>

<script>
import axios from 'axios'
export default {
	onPullDownRefresh() {
		console.log('pull')
	},
	data() {
		return {
			cart: {
				items: [],
			},
			stripe: {},
			card: {},
			first_name: '',
			last_name: '',
			email: '',
			phone: '',
			address: '',
			zipcode: '',
			place: '',
			errors: [],
		}
	},
	mounted() {
		this.cart = this.$store.state.cart
	},
	methods: {
		getItemTotal(item) {
			return item.quantity * item.product.price
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

<style scoped>
.page {
	position: absolute;
	top: 0;
	bottom: 0;
	width: 100%;
	background: #ededed;
}

.title {
	margin-top: 10rpx;
	text-align: center;
}
.cart-area {
	margin: 10rpx 0;
}

.shipping-area {
	width: 100%;
	margin: 10rpx 0;
	padding: 10rpx 0;
}

.commitBtn {
	width: 50vw;
}
.bg {
	width: 540upx;
	height: 582upx;
}
</style>
