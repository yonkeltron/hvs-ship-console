import { Ship } from './ship';

export interface GameState {
  ship: Ship;
  communications: string;
}
