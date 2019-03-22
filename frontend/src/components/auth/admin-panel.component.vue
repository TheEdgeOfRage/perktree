<template>
  <v-layout>
    <v-flex md12 lg6 offset-lg3>
      <v-card class="admin-form-card">
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
  // import AuthController from '../../controllers/auth.controller';

  export default {
    name: 'admin-panel',
    data() {
      return {
        username: '',
        password: '',
        passwordConfirm: '',
        admin: false,
        messages: [],
      };
    },
    methods: {
    },
  };
</script>

<style lang="stylus">
/*@import '../../stylus/helpers/messages.styl'*/

.admin-form-card
  padding 2rem
</style>
