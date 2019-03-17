<template>
    <div>
        <div class="apps-wrapper">
            <h2 class="title">
                <a-icon type="appstore"/>
                Applications
            </h2>
            <a-spin :spinning="loading">
                <a-row :gutter="16" type="flex" align="top">
                    <a-col :xs="24" :sm="12" :md="8" :lg="6" :xl="4"
                           v-for="app in applications"
                    >
                        <app-item :name="app.name" :logo="app.logo" :url="app.url"/>
                    </a-col>
                </a-row>
                <div class="error" v-if="error">
                    <a-alert
                            message="An error occurred!"
                            description="An error occurred and failed to get applications. Probably server is down."
                            type="error"
                            showIcon
                    />
                </div>
            </a-spin>
        </div>
    </div>
</template>

<script>
  import {mapState, mapActions} from 'vuex';

  import AppItem from "../components/AppItem";

  export default {
    name: 'home',
    components: {AppItem},
    mounted() {
      this.initialise();
    },
    computed: {
      ...mapState(['applications', 'loading', 'error'])
    },
    methods: {
      ...mapActions(['getApplications']),

      initialise() {
        this.getApplications()
      }
    },
  }
</script>

<style scoped>
    .title {
        padding-bottom: 5px;
    }
</style>
