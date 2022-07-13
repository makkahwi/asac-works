import api from "./tmdb";

const getAll = params => {
  return api.get(`/trending`, { params });
};

const getFavs = params => {
  return api.get(`/getMovies`, { params });
};

const getFav = id => {
  return api.get(`/getMovie/${id}`);
};

const createFav = data => {
  return api.post(`/addMovie`, data);
};

const updateFav = (id, data) => {
  return api.put(`/update/${id}`, data);
};

const removeFav = id => {
  return api.delete(`/delete/${id}`);
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
