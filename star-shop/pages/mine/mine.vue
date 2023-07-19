<template>
  <view class="page" v-if="username">
    <view class="header">
      <image src="../../static/image/mine-banner.jpg" class="banner"></image>
      <!-- <image src="../../static/image/set.png" class="set-png" @click="handleSet"></image> -->
      <image :src="src ? src : '../../static/image/default-headPic.png'" class="head-portrait" @click="changeHeadPic">
      </image>
      <text class="nick-name">{{ $store.state.username }}</text>
    </view>
    <view class="option first" @click="handleSet">
      <image src="../../static/image/count.png" class="option-img"></image>
      <text class="desc">我的账户</text>
    </view>
    <view class="option" @click="toOrder">
      <image src="../../static/image/order.png" class="option-img bigger"></image>
      <text class="desc">我的订单</text>
    </view>
    <view class="option" @click="logout">
      <image src="../../static/image/about.png" class="option-img"></image>
      <text class="desc">退出登录</text>
    </view>
  </view>
  <view class="login" v-else @click="gotoLogin">
    <text>您还没有登录，点击登录</text>
  </view>
</template>

<script>
  import axios from 'axios'
  import {
    mapState
  } from 'vuex'
  export default {
    data() {
      return {
        src: '', //裁剪后头像路径
        userinfo: {
          username: ''
        },
      }
    },

    computed: {
      ...mapState(['username'])
      // showStatus() {
      //   const status = localStorage.getItem('username')
      //   if (status) {
      //     this.userinfo.username = status
      //     console.log(this.userinfo)
      //     return true
      //   } else {
      //     return false
      //   }
      // }
    },
    methods: {
      logout() {
        axios.defaults.headers.common['Authorization'] = ''
        this.$store.commit('setUsername', '')
        localStorage.removeItem('token')
        localStorage.removeItem('username')
        this.$store.commit('removeToken')
        console.log('exit')

        uni.switchTab({
          url: '/pages/index/index',
        })
      },

      handleSet() {
        uni.navigateTo({
          url: '/pages/set/set',
        })
      },
      gotoLogin() {
        uni.navigateTo({
          url: '/pages/login/login',
        })
      },
      changeHeadPic() {
        let that = this
        uni.chooseImage({
          count: 1,
          sizeType: ['compressed '],
          success: function(res) {
            let tempFilePath = res.tempFilePaths[0]
            that.src = tempFilePath
          },
        })
      },
      toAccount() {
        uni.navigateTo({
          url: '/pages/account/account',
        })
      },
      toOrder() {
        uni.navigateTo({
          url: '/pages/order/order',
        })
      },
      toFootPrint() {
        uni.navigateTo({
          url: '/pages/footprint/footprint',
        })
      },
      toAboutUs() {
        uni.navigateTo({
          url: '/pages/about-us/about-us',
        })
      },
      toFeedBack() {
        uni.navigateTo({
          url: '/pages/feedback/feedback',
        })
      },
    },
    // onLoad() {
    //   this.userinfo = uni.getStorageSync('userinfo') || {}
    // },
  }
</script>

<style>
  @import '../../utils/css/page.css';

  .page {
    background: #ededed;
  }

  .header {
    width: 100%;
    height: 340upx;
  }

  .banner {
    width: 100%;
    height: 340upx;
  }

  .set-png {
    position: absolute;
    width: 60upx;
    height: 60upx;
    top: 30upx;
    left: 84%;
  }

  .head-portrait {
    position: absolute;
    width: 160upx;
    height: 160upx;
    top: 60upx;
    left: calc(50% - 80upx);
    border-radius: 50%;
  }

  .nick-name {
    position: absolute;
    display: block;
    width: 100%;
    text-align: center;
    top: 230upx;
    color: white;
    font-size: 32upx;
  }

  .option {
    width: 100%;
    height: 90upx;
    align-items: center;
    margin-top: 5upx;
    background: white;
  }

  .first {
    margin-top: 30upx;
    margin-bottom: 20upx;
  }

  .option:active {
    background: #b8b8b8;
  }

  .option-img {
    width: 40upx;
    height: 40upx;
    margin-left: 30upx;
  }

  .bigger {
    width: 46upx;
    height: 46upx;
    margin-left: 24upx;
  }

  .desc {
    color: #666666;
    font-size: 32upx;
    margin-left: 30upx;
  }

  .login {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
  }
</style>