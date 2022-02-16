import api from "./tmdb";

const path = "/trending";

const getAll = params => {
  return api.get(`${path}`, { params });
};

const getFavs = params => {
  return api.get(`${path}/getMovies`, { params });
};

const getFav = id => {
  return api.get(`${path}/getMovie/${id}`);
};

const createFav = data => {
  return api.post(`${path}/addMovie`, data);
};

const updateFav = (id, data) => {
  return api.put(`${path}/update/${id}`, data);
};

const removeFav = id => {
  return api.delete(`${path}/delete/${id}`);
};

const endpoints = {
  getAll,
  getFavs,
  getFav,
  createFav,
  updateFav,
  removeFav,
};

export default endpoints;
