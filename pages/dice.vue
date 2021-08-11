<template>
  <section class="p-5 font-mono text-white bg-black h-screen">
    <div class="flex gap-5">
      <DieDisplay :face="d1" />
      <DieDisplay :face="d2" />
      <DieDisplay :face="d3" />
      <DieDisplay :face="d4" />
    </div>

    <div class="mt-5 border-4 border-white rounded">
      <div class="flex h-48 justify-center items-center">
        <button
          class="
            text-9xl text-white
            rounded
            font-bold
            px-8
            transition
            duration-500
            hover:bg-white hover:text-black
          "
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

      let output = ' ';
      if (rand === 0) {
        output = '-';
      } else if (rand === 1) {
        output = '+';
      }

      return output;
    };

    const d1 = ref(' ');
    const d2 = ref(' ');
    const d3 = ref(' ');
    const d4 = ref(' ');

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
