<template>
	<view class="logup">
		<form @submit="submitForm()" class="logup-form">
			<view class="title"> 注册 </view>
			<view class="logup-form-item">
				<view class="label"
					>用户名<span style="color: gray">(长度6-20)</span></view
				>
				<input v-model="username" name="username" placeholder="用户名" />
			</view>
			<view class="logup-form-item">
				<view class="label">密码</view>
				<input
					v-model="password"
					name="password1"
					placeholder="密码"
					type="password"
				/>
			</view>
			<view class="logup-form-item">
				<view class="label">重复密码</view>
				<input
					v-model="password2"
					name="password2"
					placeholder="密码"
					type="password"
				/>
			</view>
			<!-- <view class="logup-form-item">
				<picker @change="selectType" :range="userrType">
					<label>请选择用户类型：</label>
					<label class="">{{ types }}</label>
				</picker>
			</view> -->
			<view class="logup-form-item" v-if="errors.length">
				<p v-for="error in errors" :key="error">{{ error }}</p>
			</view>
			<view class="logup-form-item">
				<button form-type="submit">注册</button>
			</view>
		</form>
	</view>
</template>

<script>
export default {
	data() {
		return {
			userrType: ['商家', '普通用户'],
			index: 0,
			types: '普通用户',
			username: '',
			password: '',
			password2: '',
			errors: [],
		}
	},
	methods: {
		submitForm() {
			uni.showLoading({
				title: '注册中...',
				mask: true,
			})
			this.errors = []
			if (this.username === '') {
				this.errors.push('用户名未输入！')
			}

			if (this.password.length < 8) {
				this.errors.push('密码太短')
			}

			if (this.password !== this.password2) {
				this.errors.push('前后密码不匹配！')
			}

			if (!this.errors.length) {
				const formData = {
					username: this.username,
					password: this.password,
				}
				// console.log(formData)
				uni.request({
					url: 'http://127.0.0.1:8000/api/users/',
					method: 'POST',
					data: formData,
					success(res) {
						uni.hideLoading()
						uni.showToast({
							title: `欢迎，${res.data.username}!`,
							duration: 2000,
						})
						// console.log(res.data)  { email: "", username: "stein", id: 2 }
						if (res.data) {
							setTimeout(() => {
								uni.navigateTo({
									url: '/pages/login/login',
								})
							}, 2000)
						}
					},
					fail() {
						uni.hideLoading()
					},
				})
			}
		},
		selectType(e) {
			this.index = e.target.value
			this.types = this.userrType[this.index]
		},
	},
}
</script>

<style>
.logup {
	padding: 80rpx 100rpx;
}

.logup .title {
	font-size: 60rpx;
	text-align: center;
	margin-bottom: 80rpx;
}

/* .logup .logup-form {} */

.logup .logup-form-item {
	margin: 40rpx 0;
}

.logup .logup-form-item input {
	background-color: rgba(0, 0, 0, 0.08);
	height: 80rpx;
	border-radius: 10rpx;
}
</style>
