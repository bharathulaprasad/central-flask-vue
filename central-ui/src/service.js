import axios from "axios";

console.log(process.env.NODE_ENV);

export const session = axios.create({
  baseURL: process.env.NODE_ENV === 'development' ? 'http://127.0.0.1:5000/api/v1' : '/api/v1',
  withCredentials: false,
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
  }
});

export default {
  getApplications() {
    return session.get('/applications/');
  },
  createApplication(payload) {
    // payload => {name, logo, url}
    return session.post('/create/', payload);
  },
};