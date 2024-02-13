export enum StatisticsCategory {
  All = 'all',
  Players = 'players',
  Teams = 'teams',
}

export type StatisticsByTeamOrPlayer = {
  name: string
  wins: number
  losses: number
  win_ratio: number
  goals_for: number
  goals_against: number
  goals_difference: number
}
