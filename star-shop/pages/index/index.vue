<template>
	<view class="page">
		<uni-search-bar
			placeholder="请输入想要搜索的商品"
			radius="100"
			class="search-bar"
			@confirm="searchConfirm"
			@input="searchInput"
		/>
		<view v-if="showSuggestions">
			<!-- 显示搜索提示的内容 -->
			<view v-for="suggestion in suggestions" :key="suggestion">{{
				suggestion
			}}</view>
		</view>
		<view class="swipper-content">
			<swiper
				:indicator-dots="indicatorDots"
				:autoplay="autoplay"
				indicator-active-color="#ffffff"
				class="swipper-content"
			>
				<swiper-item v-for="item in imgList" :key="item.url">
					<image :src="item.url" class="swipper-img"></image>
				</swiper-item>
			</swiper>
		</view>
		<view class="line-content">
			<view class="line"></view>
			<text class="content">推荐商品</text>
			<view class="line"></view>
		</view>
		<view
			v-for="(product, index) in productList"
			:key="index"
			@click="toGoods(product.category_slug, product.slug)"
			:data-index="index"
		>
			<product
				:image="product.get_thumbnail"
				:title="product.name"
				:originalPrice="product.price"
				:favourPrice="product.discount_price"
				:tip="product.tip"
			></product>
		</view>
	</view>
</template>

<script setup>
import { onLoad, onPullDownRefresh, onReachBottom } from '@dcloudio/uni-app'
import { ref, reactive, toRaw } from 'vue'
import product from '../../components/product.vue'
const showSuggestions = ref(false)
const autoplay = ref(true) //轮播图自动播放
const indicatorDots = ref(true) //显示轮播指示点
const productList = ref([]) //推荐商品
const searchConfirm = (res) => {
	console.log(res.value)
	queryGoods(res.value)
}
const searchInput = (res) => {}

// 搜索商品
const queryGoods = (str) => {
	if (str) {
		let test = productList.value.filter((item, index, arr) => {
			for (let el in item) {
				let searchStr = item[el]
				if (
					(el == 'name' || el == 'tip' || el == 'price') &&
					String(searchStr)
						.toLocaleLowerCase()
						.includes(str.toLocaleLowerCase())
				) {
					return item
				}
			}
		})
		productList.value = [...test]
	} else loadData()
}

const imgList = reactive([
	{
		url: '../../static/image/3.jpg',
	},
	{
		url: '../../static/image/2.jpg',
	},
	{
		url: '../../static/image/1.jpg',
	},
])

// action = 'add'
function loadData() {
	uni.request({
		url: 'http://127.0.0.1:8000/api/latest-products/',
		method: 'GET',
		success(res) {
			productList.value = res.data
		},
	})
}

// function toGoods(e) {
//   let index = e.currentTarget.dataset.index;
//   product.get_absolute_url
//   uni.navigateTo({
//     url: '/pages/goods/goods?index=' + index
//   })
// }

function toGoods(type, slug) {
	// let index = e.currentTarget.dataset.index;
	let type_params = type
	let product_params = slug
	uni.navigateTo({
		url: '/pages/goods/goods?type=' + type_params + '&slug=' + product_params, // /pages/goods/goods?type=phone&slug=ap14
	})
}

onLoad(() => {
	loadData()
})
// onPullDownRefresh(() => {
//   loadData('refresh');
//   // 实际开发中通常是网络请求，加载完数据后就停止。这里仅做演示，加延迟为了体现出效果。
//   setTimeout(() => {
//     uni.stopPullDownRefresh();
//   }, 2000);
// })
</script>

<style scoped>
@import '../../utils/css/page.css';

.search-bar {
	width: 100vw;
}

.swipper-content {
	width: 100%;
	height: 300upx;
	background: #aeeeee;
}

.swipper-img {
	width: 100%;
	height: 300upx;
}

.line-content {
	width: 100%;
	height: 80upx;
	align-items: center;
	justify-content: center;
}

.line {
	width: 36%;
	height: 2upx;
	background: #bababa;
	align-items: center;
	justify-content: center;
}

.content {
	color: #bababa;
	font-size: 32upx;
	margin: 0 20upx;
}
</style>
