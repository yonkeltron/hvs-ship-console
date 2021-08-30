<template>
  <div class="p-5 font-mono text-white bg-black h-full">
    <div class="float-right">
      <NavigationLinks />
    </div>
    <h2 class="text-2xl">&rarr; Communications</h2>

    <section class="mt-5">
      <div v-if="message" class="my-3">
        <div class="grid grid-cols-2 gap-5 w-1/3">
          <p class="text-green-400">To:</p>
          <p>{{ message.to }}</p>

          <p class="text-green-400">From:</p>
          <p>{{ message.from }}</p>

          <p class="text-green-400">Source:</p>
          <p>{{ message.source }}</p>
        </div>

        <p class="mt-5">=== BEGIN MESSAGE ===</p>

        <div class="w-2/3">
          <nuxt-content :document="message" />
        </div>

        <p class="mb-5">==== END MESSAGE ====</p>
      </div>
      <div v-else class="text-xl">
        <p>NO MESSAGES; COMMUNICATIONS CLEAR</p>
      </div>
    </section>
  </div>
</template>

<script lang="ts">
import {
  ref,
  defineComponent,
  useContext,
  onUnmounted,
} from '@nuxtjs/composition-api';
import { GameState } from '~/store/game';

export default defineComponent({
  setup() {
    const { $content, store } = useContext();

    const message = ref({});

    const refresh = async () => {
      store.dispatch('game/fetchGameState');
      const gameState = store.getters['game/gameState'] as GameState;
      if (gameState.communications) {
        message.value = await $content(
          gameState.communications.current
        ).fetch();
      }
    };

    const refreshInterval = setInterval(refresh, 3000);

    refresh();

    onUnmounted(() => {
      clearInterval(refreshInterval);
    });

    return { message };
  },
});
</script>

<style lang="postcss">
.nuxt-content p {
  @apply my-2;
}

.nuxt-content h1 {
  @apply my-4 text-3xl;
}

.nuxt-content h2 {
  @apply my-4 text-2xl;
}

.nuxt-content h3 {
  @apply my-4 text-xl;
}

.nuxt-content ul {
  @apply ml-4 mb-4 list-disc;
}
</style>
