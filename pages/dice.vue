<template>
  <section class="p-5 font-mono text-white bg-black h-screen">
    <div class="flex gap-5">
      <DieDisplay :face="roll()" />
      <DieDisplay :face="roll()" />
      <DieDisplay :face="roll()" />
      <DieDisplay :face="roll()" />
    </div>
  </section>
</template>

<script lang="ts">
import { defineComponent } from '@nuxtjs/composition-api';

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

    return { roll };
  },
});
</script>
