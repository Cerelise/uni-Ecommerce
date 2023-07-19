<template>
  <view class="page">
    <view class="successTip">
      <uni-icons type="shop-filled" size="100"></uni-icons>
      <text>感谢您的购买！</text>
      <button @click="toCart()" type="primary">返回购物车</button>
    </view>
  </view>
</template>

<script>
  export default {
    data() {
      return {

      }
    },
    methods: {
      toCart() {
        // this.$store.commit('clearCart')
        uni.switchTab({
          url: '/pages/shopping-car/shopping-car',
        })
      }
    }
  }
</script>

<style scoped>
  .page {
    display: flex;
    align-items: center;
    justify-content: center;
    position: absolute;
    top: 0;
    bottom: 0;
    width: 100%;
    background: #ededed;
  }

  .successTip {
    display: flex;
    flex-direction: column;
    gap: 30rpx;
    /*    justify-content: center;
    align-items: center; */
  }
</style>