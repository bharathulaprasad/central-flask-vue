<template>
    <a-layout id="components-layout-demo-fixed">
        <a-layout-header class="layout-header">
            <a-menu
                    theme="light"
                    mode="horizontal"
                    class="menu-wrapper"
                    :defaultSelectedKeys="['1']"
            >
                <a-menu-item key="1">
                    <router-link :to="{name:'home'}">
                        <a-icon type="home"/>
                        <span>Home</span>
                    </router-link>
                </a-menu-item>
                <a-menu-item key="2">
                    <router-link :to="{name:'about'}">
                        <a-icon type="info-circle"/>
                        <span>About</span>
                    </router-link>
                </a-menu-item>
            </a-menu>
        </a-layout-header>
        <a-layout-content class="layout-content">
            <a-breadcrumb class="breadcrumb-wrapper">
                <!--<a-breadcrumb-item>Home</a-breadcrumb-item>-->
                <!--<a-breadcrumb-item>List</a-breadcrumb-item>-->
                <!--<a-breadcrumb-item>App</a-breadcrumb-item>-->
            </a-breadcrumb>
            <div class="layout-content-inner">
                <router-view></router-view>
            </div>
        </a-layout-content>
        <a-layout-footer class="layout-footer">
            Central ©2018 | Created by <a href="http://semiworld.org" target="_blank">@ozcanyarimdunya</a>
        </a-layout-footer>
    </a-layout>
</template>

<style>
    * {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
    }

    .ant-layout-header {
        background: #fff;
        /*background: unset;*/
    }

    .layout-header {
        position: fixed;
        z-index: 1;
        width: 100%;
    }

    .menu-wrapper {
        line-height: 64px;
    }

    .layout-content {
        padding: 0 50px;
        margin-top: 64px;
    }

    .breadcrumb-wrapper {
        margin: 16px 0;
    }

    .layout-content-inner {
        background: #fff;
        padding: 24px;
        min-height: 450px;
    }

    .layout-footer {
        text-align: center;
    }
</style>
