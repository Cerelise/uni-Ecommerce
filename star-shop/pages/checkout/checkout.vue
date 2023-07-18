<template>
  <view class="page">
    <uni-section class="mb-10" type="line" title="订单详情"> </uni-section>
    <view class="cart-area">
      <uni-card v-for="item in cart.items" :title="item.product.name" :sub-title="'x' + item.quantity"
        :extra="`￥${getItemTotal(item).toFixed(2)}`" :thumbnail="item.product.get_thumbnail">
      </uni-card>
    </view>

    <uni-section class="mb-10" type="line" title="付款信息">
      <view class="order-area">
        <text>商品数量 :{{ cartTotalLength }}</text>
        <text>总价:￥{{ cartTotalPrice.toFixed(2) }}</text>
      </view>
    </uni-section>

    <view class="shipping-area">
      <uni-section title="填写运输信息" type="line">
        <uni-forms label-position="left" label-align="center">
          <uni-forms-item label="名字">
            <uni-easyinput type="text" placeholder="请输入名字" v-model="first_name" />
          </uni-forms-item>
          <uni-forms-item label="姓氏">
            <uni-easyinput type="text" placeholder="请输入姓氏" v-model="last_name" />
          </uni-forms-item>
          <uni-forms-item label="Email">
            <uni-easyinput type="text" placeholder="请输入Email" v-model="email" />
          </uni-forms-item>
          <uni-forms-item label="地址">
            <uni-easyinput type="text" placeholder="请输入详细地址" v-model="address" />
          </uni-forms-item>
          <uni-forms-item label="手机">
            <uni-easyinput type="text" placeholder="请输入手机号" v-model="phone" />
          </uni-forms-item>
          <uni-forms-item label="邮编">
            <uni-easyinput type="text" placeholder="请输入所在地的邮政编码" v-model="zipcode" />
          </uni-forms-item>
          <uni-forms-item label="地区">
            <uni-easyinput type="text" placeholder="请输入所在地区" v-model="place" />
          </uni-forms-item>
        </uni-forms>
      </uni-section>
    </view>

    <view class="payment" v-if="cartTotalLength">
      <view id="card-element"></view>
      <button class="commitBtn" type="primary" @click="submitForm">
        提交订单
      </button>
    </view>
  </view>
</template>

<script>
  import axios from 'axios'
  // import Stripe from 'stripe'
  import {
    loadStripe
  } from '@stripe/stripe-js'

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

      // if (this.cartTotalLength > 0) {
      // 	this.stripe = Stripe(
      // 		'sk_test_51NUDmjFYsD1xQvqZQEmgUv8Ag3S8isljJlMxkIzTsTk4isz1LCJ6gWR4wslcBtwNo7GR3vUXNeRbyCMbIAghypgQ00PMTSipPW'
      // 	)
      // 	const elements = this.stripe.elements()
      // 	this.card = elements.create('card', { hidePostalCode: true })

      // 	this.card.mount('#card-element')
      // }
      if (this.cartTotalLength > 0) {
        const stripePromise = loadStripe(
          'pk_test_51NUDmjFYsD1xQvqZ3Q9dZ9pyUbe1bujRtEcKF7hAtlEEGw5XxE1CfJJhIurJxqep3Pfj4pO1VF8NP0OsmyiruKbr00NVpIA4Fk'
        )

        stripePromise.then((stripe) => {
          this.stripe = stripe
          const elements = this.stripe.elements()
          this.card = elements.create('card', {
            hidePostalCode: true,
          })

          this.card.mount('#card-element')
        })
      }
    },
    methods: {
      getItemTotal(item) {
        return item.quantity * item.product.price
      },
      submitForm() {
        this.$store.commit('setIsLoading', true)

        this.stripe.createToken(this.card).then((result) => {
          if (result.error) {
            this.$store.commit('setIsLoading', false)
            console.log(result.error.message)
          } else {
            this.stripeTokenHandler(result.token)
          }
        })
      },
      async stripeTokenHandler(token) {
        const items = []

        for (let i = 0; i < this.cart.items.length; i++) {
          const item = this.cart.items[i]
          const obj = {
            product: item.product.id,
            quantity: item.quantity,
            price: item.product.price * item.quantity,
          }
          items.push(obj)
        }

        const data = {
          first_name: this.first_name,
          last_name: this.last_name,
          email: this.email,
          address: this.address,
          zipcode: this.zipcode,
          place: this.place,
          phone: this.phone,
          items: items,
          stripe_token: token.id,
        }

        await axios
          .post('http://127.0.0.1:8000/api/checkout/', data)
          .then((res) => {
            console.log('res.data :>> ', res.data)
            uni.redirectTo({
              url: '/pages/success/success',
            })
          })
          .catch((error) => {
            console.log(error)
          })
          .finally(() => {
            this.$store.commit('setIsLoading', false);
          });
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

  .order-area {
    padding: 20rpx;
    display: flex;
    flex-direction: column;
    gap: 10rpx;
  }

  .shipping-area {
    width: 100%;
    margin: 10rpx 0;
    padding: 10rpx 0;
  }

  .payment {
    padding: 10rpx 0;
  }

  .commitBtn {
    margin-top: 20rpx;
    width: 50vw;
  }

  .bg {
    width: 540upx;
    height: 582upx;
  }
</style>