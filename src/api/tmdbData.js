import api from "./tmdb";

const path = "/trending";

const getAll = params => {
  return api.get(`${path}`, { params });
};

const get = (id) => {
  return api.get(`${path}/${id}`);
};

const create = (data) => {
  return api.post(`${path}`, data);
};

const update = (id, data) => {
  return api.put(`${path}/${id}`, data);
};

const remove = (id) => {
  return api.delete(`${path}/${id}`);
};

const endpoints = {
  getAll,
  get,
  create,
  update,
  remove,
};

export default endpoints;
