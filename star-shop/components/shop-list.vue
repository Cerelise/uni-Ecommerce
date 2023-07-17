<template>
	<view class="shop-list">
		<view class="shop-top">
			<text class="title">{{listTitle}}</text>
			<view class="switch" @click="switchClick">三</view>
		</view>
		<view class="one-column" v-if="column===0">
			<view class="list" v-for="(item,index) in listData">
				<image :src="'http://127.0.0.1:8000/' + item.fields.pic" class="image"></image>
				<view class="content">
					<view class="name">
						{{item.fields.name}}
					</view>
					<view class="items">
						<view class="price">
							价格：{{item.fields.price}}
						</view>
						<view class="stock">
							库存：{{item.fields.stock}}
						</view>
						<view class="like-number">
							点赞：{{item.fields.like_num}}
						</view>
					</view>
				</view>
			</view>
		</view>

		<view class="two-column" v-else-if="column===1">

		</view>
	</view>
</template>

<script>
	export default {
		props:{
			listTitle:'',
			listData:[]
		},
		data() {
			return {
				column: 0,
			}
		},
		methods: {
			switchClick() {
				this.column = ++this.column % 2
				console.log(this.column);
			}
		},
		mounted() {
			console.log(this.listData)
		}
	}
</script>

<style>
	.shop-list .shop-top {
		height: 50px;
		line-height: 50px;
		text-align: center;
		position: relative;
	}

	.shop-list .shop-top .title {
		text-align: center;
		display: inline-block;
		position: relative;
	}

	.shop-list .shop-top .title::before {
		content: "";
		width: 40px;
		height: 1px;
		background-color: lightgray;
		position: absolute;
		left: -60px;
		top: 50%;
	}

	.shop-list .shop-top .title::after {
		content: "";
		width: 40px;
		height: 1px;
		background-color: lightgray;
		position: absolute;
		right: -60px;
		top: 50%;
	}

	.shop-list .shop-top .switch {
		position: absolute;
		background-color: rgba(0, 0, 0, 0.05);
		width: 50px;
		height: 50px;
		right: 0;
		top: 0;
		cursor: pointer;
	}

	.shop-list .one-column {
		height: 140px;
		padding: 10px;
		box-sizing: border-box;
	}

	.shop-list .one-column .list {
		display: flex;
		justify-content: space-between;
		margin: 10px 0;
	}

	.shop-list .one-column .image {
		width: 120px;
		height: 120px;
	}

	.shop-list .one-column .content {
		display: flex;
		flex-direction: column;
	}

	.shop-list .one-column .content .name {
		white-space: nowrap;
		width: calc(100vw - 150px);
		overflow: hidden;
		height: 40px;
		line-height: 40px;
	}

	.shop-list .one-column .content .items {
		display: flex;
		flex-direction: column;
		justify-content: space-between;
	}
</style>