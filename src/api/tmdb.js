import axios from "axios";

export const baseURL = process.env.REACT_APP_BACKEND_URL || "http://localhost:1337";

const service = axios.create({
  baseURL,
});

service.interceptors.request.use(
  config => {
    return config;
  },
  error => {
    Promise.reject(error);
  }
);

service.interceptors.response.use(
  response => {
    return response.data;
  },
  error => {
    console.log(error);
  }
);

export default service;