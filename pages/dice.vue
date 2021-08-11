<template>
  <section class="p-5 font-mono text-white bg-black h-screen">
    <div class="flex gap-5">
      <DieDisplay :face="d1" />
      <DieDisplay :face="roll()" />
      <DieDisplay :face="roll()" />
      <DieDisplay :face="roll()" />
    </div>

    <div class="mt-5 border-4 border-white rounded">
      <div class="flex h-48 justify-center items-center">
        <button
          class="text-9xl text-white font-bold focus:text-black focus:bg-white"
          @click="reroll()"
        >
          ROLL
        </button>
      </div>
    </div>
  </section>
</template>

<script lang="ts">
import { defineComponent, ref } from '@nuxtjs/composition-api';

export default defineComponent({
  setup() {
    const roll = () => {
      const rand = Math.floor(Math.random() * 3);

      let output = '';
      if (rand === 0) {
        output = '-';
      } else if (rand === 1) {
        output = '+';
      }

      return output;
    };

    const d1 = ref(roll());
    const d2 = ref(roll());
    const d3 = ref(roll());
    const d4 = ref(roll());

    const reroll = () => {
      d1.value = roll();
      d2.value = roll();
      d3.value = roll();
      d4.value = roll();
    };

    return { d1, d2, d3, d4, roll, reroll };
  },
});
</script>
