import { Team } from '@/types/teams'

export type GameState = {
  firstTeam?: Team
  secondTeam?: Team
  firstTeamGoals: number
  secondTeamGoals: number
}

export enum FirstOrSecond {
  First,
  Second,
}
