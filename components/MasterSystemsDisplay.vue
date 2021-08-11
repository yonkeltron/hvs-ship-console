<template>
  <div>
    <section class="mt-5">
      <div class="flex">
        <div class="flex-1">
          <nuxt-content :document="shipStatus" />
        </div>
        <div class="flex-1">
          <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
          <lottie-player
            src="https://assets5.lottiefiles.com/temp/lf20_adfZjR.json"
            background="transparent"
            speed="1"
            style="width: 300px; height: 300px"
            loop
            autoplay
          ></lottie-player>
        </div>
      </div>
    </section>
  </div>
</template>

<script lang="ts">
import {
  defineComponent,
  onMounted,
  ref,
  useContext,
} from '@nuxtjs/composition-api';

export default defineComponent({
  setup() {
    const { $content } = useContext();

    const shipStatus = ref({});

    onMounted(async () => {
      shipStatus.value = await $content('msd').fetch();
    });

    return { shipStatus };
  },
});
</script>

<style lang="postcss">
.nuxt-content h1 {
  @apply text-4xl mt-5;
}
</style>
