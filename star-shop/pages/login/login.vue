<template>
  <view class="login">
    <image class="avatar" src="/static/logo.png"></image>
    <!-- <text class="username">{{username}}</text> -->
    <form class="login-form" @submit="submitForm">
      <view class="login-form-item">
        <view class="title">用户名</view>
        <input v-model="username" name="username" placeholder="请输入用户名" />
      </view>
      <view class="login-form-item">
        <view class="title">密码</view>
        <input v-model="password" name="password" type="password" placeholder="请输入密码" />
      </view>
      <view class="login-form-item">
        <button form-type="submit" type="primary">登录</button>
      </view>
    </form>
    <view class="to-logup" @click="toLogUp">
      <text type="default">没有账号？点击注册</text>
    </view>
  </view>
</template>

<script>
  import axios from 'axios'
  export default {
    data() {
      return {
        username: '',
        password: '',
      }
    },
    onLoad() {},
    methods: {
      async submitForm() {
        // uni.showLoading({
        // 	title: '登录中...',
        // 	mask: true,
        // })
        axios.defaults.headers.common['Authorization'] = ''
        localStorage.removeItem('token')
        const formData = {
          username: this.username,
          password: this.password,
        }
        // console.log(formData)
        await axios
          .post('http://127.0.0.1:8000/api/token/login/', formData)
          .then((res) => {
            console.log(res.data)
            const token = res.data.auth_token

            this.$store.commit('setToken', token)

            axios.defaults.headers.common['Authorization'] = 'Token ' + token

            localStorage.setItem('token', token)
            uni.switchTab({
              url: '/pages/mine/mine',
            })
          })
      },
      toLogUp() {
        uni.navigateTo({
          url: '/pages/logup/logup',
        })
      },
    },
  }
</script>

<style>
  .login {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  .avatar {
    height: 128rpx;
    width: 128rpx;
    margin-top: 100rpx;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 10rpx;
  }

  .username {
    font-size: 30rpx;
    color: darkblue;
    font-weight: 600;
    margin-top: 10rpx;
    margin-bottom: 10rpx;
    height: 40rpx;
  }

  .login-form {
    margin-top: 40rpx;
    width: 90vw;
    padding: 0 10vw;
    box-sizing: border-box;
    box-shadow: 0 0 8rpx 6rpx rgba(0, 0, 0, 0.1);
    border-radius: 20rpx;
  }

  .login-form-item {
    margin-top: 60rpx;
    margin-bottom: 60rpx;
  }

  .remember-me {
    display: flex;
    align-items: center;
  }

  .to-logup {
    position: fixed;
    bottom: 100rpx;
  }
</style>