import axios from "axios";

export const session = axios.create({
  withCredentials: false,
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
  }
});

export default {
  getApplications() {
    return session.get('/applications/');
    // const data = [
    //   {
    //     'name': 'Material Notes',
    //     'logo': 'https://cookicons.co/images/app-icons/materialnotes.png',
    //     'url': 'https://play.google.com/store/apps/details?id=com.dinosaur.cwfei.materialnotes'
    //   }
    // ];
    // return new Promise((resolve, reject) => resolve({data}));
  },
};