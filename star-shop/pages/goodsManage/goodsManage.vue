<template>
	<view class="goods-item">
		<view class="search">
			<button type="primary" size="mini" class="add" @click="addGoods">增加商品</button>
			<uni-search-bar radius="100"  class="search-bar" @confirm="" @input="" v-model="searchValue"/>
		</view>
		
		<view class="item">
			<ShopItem/>
			<ShopItem/>
		</view>
	</view>
</template>

<script setup>
import ShopItem from '../../components/goods-item.vue'
import {ref} from 'vue'

const searchValue = ref('')
</script>

<style lang="scss">
	.goods-item{
		padding: 30rpx;
		.search{
			
			display: flex;
			justify-content: space-around;
			align-items: center;
			.search-bar{
				margin-left: 20rpx;
				flex: 1;
			}
		}
		.item:nth-child(1n){
			margin-bottom: 30rpx;
		}
	}

</style>
