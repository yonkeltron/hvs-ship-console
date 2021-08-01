<template>
  <div class="p-5 font-mono text-white bg-black h-full">
    <h2 class="text-2xl">&rarr; Communications</h2>

    <section class="mt-5">
      <div v-if="message" class="my-3">
        <div class="grid grid-cols-2 gap-5 w-1/3">
          <p>To:</p>
          <p>{{ message.to }}</p>

          <p>From:</p>
          <p>{{ message.from }}</p>

          <p>Source:</p>
          <p>{{ message.source }}</p>
        </div>

        <p class="mt-5">=== BEGIN MESSAGE ===</p>

        <div class="w-2/3">
          <nuxt-content :document="message" />
        </div>

        <p class="mb-5">==== END MESSAGE ====</p>
      </div>
      <div v-else>
        <p>NO MESSAGES; COMMUNICATIONS CLEAR</p>
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

    const message = ref({});

    onMounted(async () => {
      message.value = await $content('communications/opening-scene').fetch();
    });

    return { message };
  },
});
</script>

<style lang="postcss">
.nuxt-content p {
  @apply my-2;
}
</style>
