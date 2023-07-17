import Vue from 'vue'
import axios from 'axios'

// create an axios instance
// const service = axios.create({
//   baseURL: 'http://127.0.0.1', // url = base url + request url
//   //withCredentials: true, // send cookies when cross-domain requests 注意：withCredentials和后端配置的cross跨域不可同时使用
//   timeout: 6000, // request timeout
//   crossDomain: true
// })