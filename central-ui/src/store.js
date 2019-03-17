import Vue from 'vue'
import Vuex from 'vuex'
import {
  SET_APPLICATIONS_DATA,
  GET_APPLICATIONS_BEGIN,
  GET_APPLICATIONS_FAILURE,
  GET_APPLICATIONS_SUCCESS
} from './consts'
import service from './service';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    applications: [],
    loading: false,
    error: false
  },
  actions: {
    getApplications({commit}) {
      commit(GET_APPLICATIONS_BEGIN);
      return service.getApplications()
        .then(data => commit(SET_APPLICATIONS_DATA, data.data))
        .then(() => commit(GET_APPLICATIONS_SUCCESS))
        .catch(() => commit(GET_APPLICATIONS_FAILURE))
    }
  },
  mutations: {
    [GET_APPLICATIONS_BEGIN](state) {
      state.loading = true;
      state.error = false;
    },
    [GET_APPLICATIONS_SUCCESS](state) {
      state.loading = false;
      state.error = false;
    },
    [GET_APPLICATIONS_FAILURE](state) {
      state.loading = false;
      state.error = true;
    },
    [SET_APPLICATIONS_DATA](state, applications) {
      state.loading = false;
      state.error = false;
      state.applications = applications;
    },
  },
})
