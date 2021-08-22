<template>
  <div>
    <section class="mt-5">
      <div class="flex">
        <div class="flex-1 text-4xl">
          <div v-if="shipStatus.ship" class="grid grid-cols-2 gap-5">
            <h2>Location:</h2>
            <h2>{{ shipStatus.ship.currentLocation }}</h2>

            <h2>Funds:</h2>
            <h2>HD{{ shipStatus.ship.funds }}</h2>

            <h2>Cups of TEA:</h2>
            <h2>{{ shipStatus.ship.tea }}</h2>

            <h2>Ship Stress:</h2>
            <div class="grid grid-cols-3 gap-2">
              <StressBox
                v-for="(stress, idx) in shipStatus.ship.shipStress"
                :key="idx"
                :checked="stress"
              />
            </div>
          </div>

          <div v-if="shipStatus.ship" class="mt-5">
            <h2 class="my-5">Aspects:</h2>
            <ul class="text-2xl">
              <li
                v-for="(aspect, idx) in shipStatus.ship.aspects"
                :key="idx"
                class="ml-5"
              >
                &check; {{ aspect }}
              </li>
            </ul>
          </div>
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
  computed,
  defineComponent,
  useContext,
  onUnmounted,
} from '@nuxtjs/composition-api';

import { GameState } from '~/store/game';

export default defineComponent({
  setup() {
    const { store } = useContext();

    const shipStatus = computed(
      () => store.getters['game/gameState'] as GameState
    );

    const refresh = () => {
      store.dispatch('game/fetchGameState');
    };

    const refreshInterval = setInterval(refresh, 3000);

    refresh();

    onUnmounted(() => {
      clearInterval(refreshInterval);
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
