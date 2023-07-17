<template>
	<view class="page">
		<view class="swipper-content">
			<swiper
				:indicator-dots="indicatorDots"
				:autoplay="autoplay"
				indicator-active-color="#ffffff"
				class="swipper-content"
			>
				<swiper-item>
					<image :src="goods.get_image" class="swipper-img"></image>
				</swiper-item>
				<swiper-item>
					<image :src="goods.get_image" class="swipper-img"></image>
				</swiper-item>
				<swiper-item>
					<image :src="goods.get_image" class="swipper-img"></image>
				</swiper-item>
			</swiper>
		</view>
		<view class="item fuck">
			<text class="title">{{ goods.name }}</text>
		</view>
		<view class="item limit">
			<text>零售价</text>
			<text>{{ goods.price }} 元</text>
		</view>
		<view class="item limit">
			<text>优惠价</text>
			<text>{{ goods.discount_price }} 元</text>
		</view>
		<!--    <view class="item limit">
      <text>规格</text>
      <text>{{goods.size}}</text>
    </view> -->
		<view class="blank"> </view>
		<view class="footer">
			<view class="count">
				<view class="add" @click="add">
					<text class="center">+</text>
				</view>
				<text class="number">1</text>
				<view class="add" @click="sub">
					<text class="center">-</text>
				</view>
			</view>
			<view class="submit">
				<view class="action" @click="addToCart">
					<text>加入购物车</text>
				</view>
				<view class="action buy" @click="buy">
					<text>立即购买</text>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
export default {
	data() {
		return {
			indicatorDots: true, //显示轮播指示点
			goods: {},
			quantity: 1,
		}
	},
	computed: {
		query() {
			return this.$route.query
		},
	},
	methods: {
		add() {
			this.goods.count += 1
		},
		sub() {
			if (this.goods.count > 1) this.goods.count -= 1
		},
		addToCart() {
			uni.showLoading({
				title: '正在处理中...',
			})
			//TODO:vuex购物车没实现
			if (isNaN(this.quantity) || this.quantity < 1) {
				this.quantity = 1
			}

			const item = {
				product: this.goods,
				quantity: this.quantity,
			}

			this.$store.commit('addToCart', item)
			setTimeout(() => {
				uni.hideLoading()
				uni.showToast({
					title: '已加入购物车',
				})
			}, 1500)
		},
		buy() {
			uni.showLoading({
				title: '请稍后...',
			})
			setTimeout(() => {
				uni.hideLoading()
				uni.showToast({
					title: '购买成功',
				})
			}, 1500)
		},
		async loadData() {
			const category_slug = this.$route.query.type
			const product_slug = this.$route.query.slug
			const res = await uni.request({
				url:
					'http://127.0.0.1:8000/api/products/' +
					category_slug +
					'/' +
					product_slug,
				method: 'GET',
			})
			const product = res.data
			this.goods = product
		},
	},

	onLoad() {
		this.loadData()
	},
}
</script>

<style scoped>
@import '../../utils/css/page.css';

.page {
	background: #ededed;
}

.swipper-content {
	width: 100%;
	height: 700upx;
}

.swipper-img {
	width: 100%;
	height: 700upx;
}

.item {
	width: 100%;
	height: 80upx;
	line-height: 80upx;
	background: white;
	font-size: 34upx;
}

.fuck {
	display: flex;
	flex-direction: row;
	justify-content: center;
}

.title {
	white-space: nowrap;
	overflow: hidden;
	text-overflow: ellipsis;
}

.limit {
	padding: 10upx;
	display: flex;
	flex-direction: row;
	justify-content: space-between;
	margin-top: 2upx;
	color: #666666;
}

.footer {
	background: white;
	position: fixed;
	display: flex;
	flex-direction: row;
	justify-content: space-between;
	bottom: 0;
	width: 100%;
	height: 100upx;
	line-height: 100upx;
	padding-left: 20upx;
}

.count {
	width: 260upx;
	height: 100upx;
}

.add {
	position: relative;
	margin-top: 10upx;
	width: 80upx;
	height: 80upx;
	line-height: 80upx;
	text-align: center;
	border-radius: 10upx;
	background: #ff6633;
	color: white;
	font-size: 50upx;
}

.number {
	display: inline-block;
	width: 70upx;
	height: 100upx;
	line-height: 100upx;
	text-align: center;
	color: #666666;
}

.submit {
	display: flex;
	flex-direction: row;
	height: 100upx;
}

.action {
	display: flex;
	flex-direction: row;
	justify-content: center;
	align-items: center;
	width: 200upx;
	height: 100upx;
	background: #6699ff;
	color: white;
	font-size: 30upx;
}

.buy {
	width: 200upx;
	height: 100upx;
	background: #66ffcc;
}

.center {
	position: absolute;
	top: 50%;
	left: 50%;
	transform: translate(-50%, -50%);
}

.blank {
	height: 180upx;
	width: 100%;
}
</style>
