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
  computed,
  defineComponent,
  onMounted,
  useContext,
} from '@nuxtjs/composition-api';
import { GameState } from '~/store/game';

export default defineComponent({
  setup() {
    const { $content, store } = useContext();

    const message = computed(async () => {
      const gameState = store.getters['game/gameState'] as GameState;
      return await $content(gameState.communications.current).fetch();
    });

    onMounted(() => {
      setInterval(() => {
        store.dispatch('game/fetchGameState');
      }, 5000);
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
