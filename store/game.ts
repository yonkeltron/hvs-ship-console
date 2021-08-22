import { GetterTree, ActionTree, MutationTree } from 'vuex';
import * as gameState from '~/content/db.json';

export type GameState = typeof gameState;

export const state = () => ({
  gameState: {} as GameState,
});

export type RootState = ReturnType<typeof state>;

export const getters: GetterTree<RootState, RootState> = {
  gameState: (state) => state.gameState,
};

export const mutations: MutationTree<RootState> = {
  UPDATE_GAME_STATE: (state, newGameState: GameState) =>
    (state.gameState = newGameState),
};

export const actions: ActionTree<RootState, RootState> = {
  async fetchGameState({ commit }) {
    const newGameState = await this.$axios.$get(
      'https://aith.yonkeltron.com/db'
    );
    console.log('Fetched new game state:', newGameState, new Date());
    commit('UPDATE_GAME_STATE', newGameState);
  },
};
