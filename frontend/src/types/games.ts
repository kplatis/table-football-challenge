import { Team } from './teams'

export type Game = {
  id: number
  first_team: Team
  second_team: Team
  first_team_goals: number
  second_team_goals: number
}