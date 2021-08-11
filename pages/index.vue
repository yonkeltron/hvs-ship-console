<template>
  <section class="p-5 font-mono text-white bg-black h-screen">
    <div class="float-right">
      <NavigationLinks />
    </div>
    <h2 class="text-4xl">&rarr; All Aboard!</h2>
    <div class="flex h-1/2 justify-center items-center">
      <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
      <lottie-player
        src="https://assets9.lottiefiles.com/packages/lf20_ZWEJL5.json"
        background="transparent"
        speed="1"
        style="width: 300px; height: 300px"
        loop
        autoplay
      ></lottie-player>
      <!-- <img src="images/new_wave.svg" /> -->
    </div>
  </section>
</template>

<style lang="postcss">
section {
  background-image: url('/images/new_wave.svg');
}
</style>
