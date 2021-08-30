<template>
  <div class="text-center">
    <div
      v-if="checked"
      class="w-12 h-12 rounded border-4 border-red-600 text-red-600"
    >
      /
    </div>
    <div
      v-else
      class="w-12 h-12 rounded border-4 border-green-600 text-green-600"
    >
      &check;
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from '@nuxtjs/composition-api';

export default defineComponent({
  props: {
    checked: {
      type: Boolean,
      required: true,
    },
  },
  setup(_props) {},
});
</script>
