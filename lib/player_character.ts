export interface PlayerCharacter {
  name: string;
  refresh: number;
  highConcept: string;
  trouble: string;
  relationship: string;
  otherAspects: string[];
  physicalStress: { current: number; max: number };
  mentalStress: { current: number; max: number };
  stunts: string[];
}
