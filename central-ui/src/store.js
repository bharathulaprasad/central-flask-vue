import Vue from 'vue'
import Vuex from 'vuex'
import {
  SET_APPLICATIONS_DATA,
  GET_APPLICATIONS_BEGIN,
  GET_APPLICATIONS_FAILURE,
  GET_APPLICATIONS_SUCCESS,
  SET_CREATE_APPLICATIONS_DATA,
  GET_CREATE_APPLICATIONS_BEGIN,
  GET_CREATE_APPLICATIONS_FAILURE,
  GET_CREATE_APPLICATIONS_SUCCESS,
} from './consts'
import service from './service';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    applications: [],
    loading: false,
    error: false,
    createApplication: {
      loading: false,
      error: false,
      data: false,
    },
  },
  actions: {
    getApplications({commit}) {
      commit(GET_APPLICATIONS_BEGIN);
      return service.getApplications()
        .then(data => commit(SET_APPLICATIONS_DATA, data.data))
        .then(() => commit(GET_APPLICATIONS_SUCCESS))
        .catch(() => commit(GET_APPLICATIONS_FAILURE))
    },
    createApplication({commit}, payload) {
      commit(GET_CREATE_APPLICATIONS_BEGIN);
      return service.createApplication(payload)
        .then(data => commit(SET_CREATE_APPLICATIONS_DATA, data.data))
        .then(() => commit(GET_CREATE_APPLICATIONS_SUCCESS))
        .catch(() => commit(GET_CREATE_APPLICATIONS_FAILURE));
    },
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
    [GET_CREATE_APPLICATIONS_BEGIN](state) {
      state.createApplication.loading = true;
      state.createApplication.error = false;
    },
    [GET_CREATE_APPLICATIONS_SUCCESS](state) {
      state.createApplication.loading = false;
      state.createApplication.error = false;
    },
    [GET_CREATE_APPLICATIONS_FAILURE](state) {
      state.createApplication.loading = false;
      state.createApplication.error = true;
    },
    [SET_CREATE_APPLICATIONS_DATA](state, data) {
      state.createApplication.loading = false;
      state.createApplication.error = false;
      state.createApplication.data = data;
    },
  },
})
