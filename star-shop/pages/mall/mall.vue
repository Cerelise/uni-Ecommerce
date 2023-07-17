<template>
  <view class="page">
    <view class="menu">
      <view class="item" v-bind:class="{activeClass: (activeIndex == 1)}" @click="changeType(1)">
        <text>全部</text>
      </view>
      <view class="item" v-bind:class="{activeClass: (activeIndex == 2)}" @click="changeType(2)">
        <text>电脑</text>
      </view>
      <view class="item" v-bind:class="{activeClass: (activeIndex == 3)}" @click="changeType(3)">
        <text>手机</text>
      </view>
      <view class="item" v-bind:class="{activeClass: (activeIndex == 4)}" @click="changeType(4)">
        <text>平板电脑</text>
      </view>
      <view class="item" v-bind:class="{activeClass: (activeIndex == 5)}" @click="changeType(5)">
        <text>其他</text>
      </view>
    </view>
    <!-- @click="toGoods(product.category_slug,product.slug) -->
    <view v-for="(product,index) in productList" :key="index" @click="toGoods(product.category_slug,product.slug)"
      :data-index="index">
      <product :image="product.get_thumbnail" :title="product.name" :originalPrice="product.price"
        :favourPrice="product.discount_price" :tip="product.tip"></product>

    </view>

  </view>
</template>

<script>
  import product from '../../components/product.vue';
  import store from '../../store/store.js'
  export default {
    data() {
      return {
        productList: [],
        activeIndex: 1, //默认高亮全部item
        data: []
      }
    },
    components: {
      product
    },
    onLoad() {
      this.loadData()
    },

    methods: {
      changeType(index) {
        //取消默认高亮
        this.activeIndex = index;
        this.productList = (index == 1) ? this.data : this.data.filter(item => item.ctype == index);
      },
      changeProductType(type) {
        //取消默认高亮
        this.activeType = type;
        this.productList = (index == 1) ? this.data : this.data.filter(item => item.type == index);
      },
      toGoods(type, slug) {
        // let index = e.currentTarget.dataset.index;
        let type_params = type
        let product_params = slug
        uni.navigateTo({
          url: '/pages/goods/goods?type=' + type_params + '&slug=' +
            product_params // /pages/goods/goods?type=phone&slug=ap14
        })
      },
      async loadData() {
        let products = []
        const res = await uni.request({
          url: "http://127.0.0.1:8000/api/all-products/",
          method: 'GET',
        })
        products = res.data
        this.productList = products
        this.data = products
      }
    },


  }
</script>

<style>
  @import '../../utils/css/page.css';

  .menu {
    width: 100%;
    height: 100upx;
    background: #B8B8B8;
  }

  .item {
    display: inline-block;
    width: 20%;
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
</style>