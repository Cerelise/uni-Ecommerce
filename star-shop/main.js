import App from './App'
import store from '@/store/store.js'

// #ifndef VUE3
import Vue from 'vue'
import axios from 'axios'
Vue.config.productionTip = false
App.mpType = 'app'
try {
	function isPromise(obj) {
		return (
			!!obj &&
			(typeof obj === 'object' || typeof obj === 'function') &&
			typeof obj.then === 'function'
		)
	}

	// 统一 vue2 API Promise 化返回格式与 vue3 保持一致
	uni.addInterceptor({
		returnValue(res) {
			if (!isPromise(res)) {
				return res
			}
			return new Promise((resolve, reject) => {
				res.then((res) => {
					if (res[0]) {
						reject(res[0])
					} else {
						resolve(res[1])
					}
				})
			})
		},
	})
} catch (error) {}

axios.defaults.baseURL = 'http://127.0.0.1:8000'

const app = new Vue({
	...App,
	store,
})
app.$mount()
// #endif

// #ifdef VUE3
import { createSSRApp } from 'vue'
import axios from 'axios'
export function createApp() {
	const app = createSSRApp(App)
	app.use(store)
	return {
		app,
	}
}
// #endif
