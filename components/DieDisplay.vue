<template>
  <div class="flex-1 border-4 border-white rounded bg-black">
    <div class="flex h-48 justify-center items-center">
      <p class="text-9xl text-white font-bold">{{ dieFace }}</p>
    </div>
  </div>
</template>

<script lang="ts">
import { computed, defineComponent } from '@nuxtjs/composition-api';

export default defineComponent({
  props: {
    face: {
      type: String,
      required: true,
    },
  },
  setup(props) {
    const face = computed(() => props.face);
    return {
      dieFace: face,
    };
  },
});
</script>
