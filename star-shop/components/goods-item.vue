<template>
  <view class="item">
    <view class="goods" @click="toGoods">
      <view class="left">
        <image :src="item.product.get_thumbnail" mode=""></image>
      </view>
      <view class="right">
        <view class="title">{{item.product.name}}</view>
        <view class="price">￥{{item.product.price}}</view>
      </view>
    </view>
    <!--    <view class="btns">
      
    </view> -->
    <view class="btn">
      <button type="primary" class="btn-item" size="mini" plain @click="incrementQuantity(item)"
        :data-index="index">+</button>
      <text class="shop-count btn-item">{{item.quantity}}</text>
      <button type="primary" class="btn-item" size="mini" plain @click="decrementQuantity(item)"
        :data-index="index">-</button>
      <button type='warn' @click='removeFromCart(item)'>删除</button>
    </view>
  </view>
</template>

<script>
  export default {
    props: {
      initialItem: Object
    },
    data() {
      return {
        item: this.initialItem
      }
    },
    mounted() {
      console.log(this.initialItem)
    },
    methods: {
      getItemTotal(item) {
        return item.quantity * item.product.price
      },
      decrementQuantity(item) {
        item.quantity -= 1

        if (item.quantity === 0) {
          // 数量为0时移除此项
          this.$emit('removeFromCart', item)
        }

        this.updateCart()
      },
      incrementQuantity(item) {
        item.quantity += 1

        this.updateCart()
      },
      // 更新购物车
      updateCart() {
        localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
      },
      // 移除购物车中某一项
      removeFromCart(item) {
        this.$emit('removeFromCart', item)
        this.updateCart()
      },
    },
  }
</script>


<style lang="scss">
  .item {
    padding-top: 30rpx;
    display: flex;
    flex-direction: column;

    .goods {
      display: flex;
      justify-content: space-between;
      align-items: center;

      .left {
        image {
          width: 120rpx;
          height: 120rpx;
        }
      }

      .right {
        margin-left: 40rpx;
        flex: 1;

        .title {
          width: 350rpx;
          font-size: 35rpx;
          font-weight: 500;
        }

        .price {
          color: red;
        }
      }
    }

    .btn {
      display: flex;
      justify-content: flex-end;
      align-items: center;

      .btn-item {
        // margin-left: 20rpx;
        align-items: center;
      }

      .shop-count {
        font-size: 40rpx;
      }
    }
  }
</style>