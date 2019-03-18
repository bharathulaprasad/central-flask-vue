<template>
    <div>
        <a-row>
            <a-col :span="6" :offset="9">
                <div class="header">Create New Application</div>
                <a-form @submit.prevent="submit" @keyup.enter="create(inputs)">
                    <a-form-item has-feedback :validate-status="status.name">
                        <a-input v-model="inputs.name" @keyup.enter="create(inputs)" type="text"
                                 placeholder="Name">
                            <a-icon slot="prefix" type="user" style="color:rgba(0,0,0,.25)"/>
                        </a-input>
                    </a-form-item>
                    <a-form-item has-feedback :validate-status="status.url">
                        <a-input v-model="inputs.url" @keyup.enter="create(inputs)" type="url"
                                 placeholder="Url">
                            <a-icon slot="prefix" type="lock" style="color:rgba(0,0,0,.25)"/>
                        </a-input>
                    </a-form-item>
                    <a-form-item has-feedback :validate-status="status.name">
                        <a-upload name="logo"
                                  :multiple="false"
                                  action="/api/v1/upload/"
                                  @change="handleChange">
                            <a-button>
                                <a-icon type="upload"/>
                                Upload logo
                            </a-button>
                        </a-upload>
                    </a-form-item>
                    <a-form-item>
                        <a-button type="primary" style="width: 100%; background-color: #013769" @click="create(inputs)">
                            <a-icon type="plus-circle"/>
                            Create
                        </a-button>
                    </a-form-item>
                </a-form>
            </a-col>
        </a-row>
    </div>
</template>

<script>
  import {mapActions} from 'vuex';

  export default {
    name: "Create",
    data() {
      return {
        inputs: {
          name: '',
          url: '',
          logo: '',
        },
        status: {
          name: '',
          url: '',
        },
      }
    },
    methods: {
      ...mapActions(['createApplication']),

      handleChange(info) {
        if (info.file.status !== 'uploading') {
          this.inputs.logo = info.file.response;
        }
        if (info.file.status === 'done') {
          this.$message.success(`${info.file.name} file uploaded successfully`);
        } else if (info.file.status === 'error') {
          this.$message.error(`${info.file.name} file upload failed.`);
        }
      },
      create({name, url, logo}) {
        const payload = {name, url, logo};
        this.status.name = '';
        this.status.url = '';
        if (!name) {
          this.status.name = 'error';
          return
        } else if (!url) {
          this.status.url = 'error';
          return
        }

        this.createApplication(payload).then(() => this.$router.push({name: 'home'}));
      }
    },
  }
</script>

<style scoped>
    .header {
        margin: 5px;
        font-size: 18px;
    }
</style>