<template>
    <div>
        <a-card hoverable class="wrapper" @click="cardClicked">
            <img :alt="name" :src="logo" slot="cover"/>
            <a-card-meta :title="name">
                <template slot="description">
                    <span class="link">
                        {{link}}
                    </span>
                </template>
            </a-card-meta>
        </a-card>

        <a-modal :title="name" v-model="visible" :footer="null">
            <div class="modal">
                <img :alt="name" :src="logo" slot="cover"/>
                <a-card>
                    <a-icon type="link"/>
                    <a :href="url" target="_blank" class="modal-url">
                        {{url}}
                    </a>
                </a-card>
            </div>
        </a-modal>
    </div>
</template>

<script>
  export default {
    name: "AppItem",
    props: {
      logo: {
        type: String,
        default: 'https://via.placeholder.com/150?text=No logo',
      },
      name: {
        type: String,
        default: null,
        required: true
      },
      url: {
        type: String,
        default: '#',
      }
    },
    data() {
      return {
        visible: false
      }
    },
    computed: {
      link() {
        return this.url.substring(0, 25) + "...";
      }
    },
    methods: {
      cardClicked() {
        this.visible = !this.visible;
      }
    },
  }
</script>

<style scoped>
    .wrapper {
        margin-bottom: 12px;
    }

    .wrapper img {
        padding: 12px 48px;

    }

    .link {
        text-decoration: none;
        font-size: 12px;
        color: inherit;
    }

    .modal-url {
        text-decoration: none;
    }

    .modal-url:hover {
        color: #1890ff;
        text-decoration: underline;
    }

    .modal {
        text-align: center;
    }

    .modal img {
        padding: 24px;
    }
</style>