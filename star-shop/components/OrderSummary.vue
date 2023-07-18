<template>
  <view class="summary">
    <uni-section class="mb-10" type="line" :title="'订单 '+'#'+order.id"></uni-section>
    <uni-card v-for="item in order.items" :key="item.product.id" :title="item.product.slug" :isFull="true"
      :sub-title="'x'+item.quantity" :extra="'￥'+getItemTotal(item).toFixed(2)">
      <text>{{ item.product.name }}</text>
    </uni-card>
  </view>
</template>

<script>
  export default {
    name: "OrderSummary",
    props: {
      order: Object
    },
    methods: {
      getItemTotal(item) {
        return item.quantity * item.product.price
      },
      orderTotalLength(order) {
        return order.items.reduce((acc, curVal) => {
          return acc += curVal.quantity
        }, 0)
      },
    }
  }
</script>

<style>
  .summary {
    width: 100%;
    padding: 20rpx 0;
  }
</style>