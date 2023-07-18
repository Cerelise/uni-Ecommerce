<template>
  <view class="page">
    <view class="menu">
      <text class='title'>全部订单</text>
      <!--      <view class="item" v-bind:class="{activeClass: (activeIndex == 1)}" @click="changeType(1)">
        <text>全部</text>
      </view>
      <view class="item" v-bind:class="{activeClass: (activeIndex == 2)}" @click="changeType(2)">
        <text>配送中</text>
      </view>
      <view class="item" v-bind:class="{activeClass: (activeIndex == 3)}" @click="changeType(3)">
        <text>已收货</text>
      </view> -->
    </view>
    <OrderSummary v-for="order in orders" :key="order.id" :order="order"></OrderSummary>
  </view>
</template>

<script>
  import axios from 'axios'
  import OrderSummary from '../../components/OrderSummary.vue'
  export default {
    components: {
      OrderSummary
    },
    data() {
      return {
        activeIndex: 1, //默认高亮全部item
        shopList: [],
        orders: [],

      }
    },

    mounted() {
      this.getMyOrders()
    },
    methods: {
      changeType(index) {
        //取消默认高亮
        this.activeIndex = index;
        if (index == 1) {
          this.shopList = this.data;
        } else if (index == 2) {
          this.shopList = this.data.slice(2);
        } else {
          this.shopList = this.data.slice(0, 2);
        }
      },
      getMyOrders() {
        axios.get('http://127.0.0.1:8000/api/orders/')
          .then(res => {
            this.orders = res.data
            console.log(this.orders)
          }).catch(error => {
            console.log(error)
          })
      },
      //去商品详情
      toGoods(e) {
        let index = e.currentTarget.dataset.index;
        //index处理
        if (this.activeIndex == 1) {
          if (index == 2) {
            index = 3;
          } else if (index == 3) {
            index = 5;
          }
        } else if (this.activeIndex == 2) {
          if (index == 0) {
            index = 3;
          } else {
            index = 5;
          }
        }
        uni.navigateTo({
          url: '/pages/goods/goods?index=' + index
        })
      }
    },
    onLoad() {
      this.shopList = this.data;
    }
  }
</script>

<style>
  @import '../../utils/css/page.css';

  .menu {
    width: 100%;
    height: 100upx;
    background: #B8B8B8;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .title {
    color: #fff;
  }

  .item {
    display: inline-block;
    width: 33.3%;
    height: 100upx;
    text-align: center;
    line-height: 100upx;
    color: white;
    font-size: 32upx;
  }

  .item:active {
    background: #EBEBEB;
  }

  .activeClass {
    border-bottom: solid 8upx #66ffcc;
    box-sizing: border-box;
    color: #66FFCC;
  }

  .shop-item {
    width: 100%;
    height: 240upx;
    align-items: center;
    padding: 30upx 20upx;
    border-bottom: solid 5upx #EDEDED;
  }

  .shop-img {
    height: 100%;
    width: 240upx;
    margin-left: 30upx;
  }

  .shop-desc {
    width: 360upx;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    /*交叉轴的起点对齐*/
    margin-left: 8upx;
  }

  .shop-title {
    width: 360upx;
    color: #666666;
    font-size: 32upx;
    word-break: break-all;
    display: -webkit-box;
    overflow: hidden;
    text-overflow: ellipsis;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 2;
  }

  .shop-action {
    width: 360upx;
    line-height: 60upx;
    margin-top: 26upx;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
  }

  .shop-price {
    color: #E80080;
    font-size: 34upx;
  }

  .count-png {
    margin-left: 130upx;
    width: 50upx;
    height: 50upx;
  }

  .count-desc {
    margin-left: 2upx;
    top: 2upx;
    font-size: 36upx;
    color: #66ffcc;
  }
</style>